import json
import urllib2
import requests
from urlparse import urlparse
from M2Crypto import X509
from base64 import b64decode
from M2Crypto.Err import M2CryptoError
from django.http import JsonResponse

SNS_SUB_UNSUB_NOTIFICATION_FIELDS = ["Message", "MessageId", "SubscribeURL", "Timestamp", "Token", "TopicArn", "Type"]
SNS_MSG_NOTIFICATION_FIELDS = ["Message", "MessageId", "Subject", "Timestamp", "TopicArn", "Type"]
SNS_REGION = "us-east-2"

def create_canonical_msg(content):
    """
    Builds the canonical message to be verified.
    Args:
        content (dict): content that is passed to the verify_aws_sns_sign
    Returns (str):
        canonical message
    """
    message_type = content["Type"]

    # Depending on the message type, canonical message format varies.
    # ref: https://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.verify.signature.html
    if  message_type ==  "SubscriptionConfirmation" or message_type == "UnsubscribeConfirmation":
        msg_fields = SNS_SUB_UNSUB_NOTIFICATION_FIELDS
    elif message_type == "Notification":
       msg_fields = SNS_MSG_NOTIFICATION_FIELDS
    else:
        raise ValueError("Message Type (%s) is not recognized" % message_type)

    msg = ""

    for field in msg_fields:
        try:
            msg += field + "\n" + content[field] + "\n"
        except KeyError:
            # Build with what you have
            pass

    return str(msg)

def verify_aws_sns_sign(content):
    """
    Takes body-content of post-request of AWS-SNS service and verifies the host & signature
    Args:
        content (json): The request body content that was passed to the view function
        content = json.loads(request.body)
    Returns (bool):
        True if the message passes the verification, False otherwise
    """
    response_dict = {}

    certificate_hostname = urlparse(str(content["SigningCertURL"])).hostname
    aws_sns_hostname = "sns.{}.amazonaws.com".format(SNS_REGION)

    # Verify that certificate is received from AWS-SNS.
    if certificate_hostname != aws_sns_hostname:
        raise ValueError("Warning! Someone attempted to make chumbak's server fool")

    canonical_message = create_canonical_msg(content)
    decoded_signature = b64decode(content["Signature"])

    # Load the certificate and extract the public key
    certificate = X509.load_cert_string(str(urllib2.urlopen(content["SigningCertURL"]).read()))
    pubkey = certificate.get_pubkey()
    pubkey.reset_context(md='sha1')
    pubkey.verify_init()

    # Feed the canonical message to sign it with the public key from the certificate
    pubkey.verify_update(canonical_message)

    # M2Crypto users EVP_VerifyFinal() from openssl that returns 1 for a correct sign, 0 for failure and -1 if some other error occurred."
    # ref: https://www.openssl.org/docs/manmaster/man3/EVP_VerifyInit.html
    verification_result = pubkey.verify_final(decoded_signature)

    if verification_result == 1:
        response_dict['status'] = 200
        response_dict['message'] = "AWS-SNS signature successfully varified"
        response_dict['SNS-Msg'] = content.get('Message', None)
        response_dict['SNS-MsgID'] = content.get('MessageId', None)
        response_dict['SNS-Subject'] = content.get('Subject', None)
        suburl =  content.get('SubscribeURL', None)
        if suburl: requests.get(suburl)
    elif verification_result == 0:
        response_dict['status'] = 400
        response_dict['message'] = "Invalid signature"
    else:
        raise M2CryptoError("Some error occured while verifying the signature.")

    return JsonResponse(response_dict)

