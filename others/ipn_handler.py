import re
import json
import base64
import logging
from urllib2 import urlopen, urlparse
#from urllib import request
from OpenSSL import crypto
#from urllib.error import HTTPError
#from urllib.parse import urlparse
#from amazon_pay.payment_response import PaymentResponse

import xml.etree.ElementTree as et
from collections import defaultdict

class PaymentResponse:

    """
    Base class for all OffAmazonPayments responses

    Parameters
    ----------
    xml : string
        XML response from Amazon.

    response : Response
        Holds the response type for the API call.
    """
    def __init__(self, xml):
        """Initialize response"""
        self.success = True
        self._xml = xml
        try:
            self._root = et.fromstring(xml)
            self._ns = self._namespace(self._root)
            self._response_type = self._root.tag.replace(self._ns, '')
        except:
            raise ValueError('Invalid XML.')

        """
        There is a bug where 'eu' endpoint returns ErrorResponse XML node
        'RequestID' with capital 'ID'. 'na' endpoint returns 'RequestId'
        """
        try:
            if self._root.find('.//{}RequestId'.format(self._ns)) is None:
                self.request_id = self._root.find(
                    './/{}RequestID'.format(self._ns)).text
            else:
                self.request_id = self._root.find(
                    './/{}RequestId'.format(self._ns)).text
        except:
            self.request_id = None

    def _namespace(self, element):
        """Get XML namespace"""
        ns = re.match('\{.*\}', element.tag)
        return ns.group(0) if ns else ''

    def to_xml(self):
        """Return XML"""
        return self._xml

    def to_json(self):
        """Return JSON"""
        return json.dumps(self._etree_to_dict(self._root))

    def to_dict(self):
        """Return Dictionary"""
        return self._etree_to_dict(self._root)

    def _etree_to_dict(self, t):
        """Convert XML to Dictionary"""
        d = {t.tag.replace(self._ns, ''): {} if t.attrib else None}
        children = list(t)
        if children:
            dd = defaultdict(list)
            for dc in map(self._etree_to_dict, children):
                for k, v in dc.items():
                    dd[k].append(v)
            d = {
                t.tag.replace(self._ns, ''): {
                    k: v[0] if len(v) == 1 else v for k,
                    v in dd.items()}}
        if t.attrib:
            d[t.tag.replace(self._ns, '')].update(('@' + k, v)
                                                  for k, v in t.attrib.items())
        if t.text:
            text = t.text.strip()
            if children or t.attrib:
                if text:
                    d[t.tag.replace(self._ns, '')]['#text'] = text
            else:
                d[t.tag.replace(self._ns, '')] = text
        return d


class IpnHandler():
    """
    Instant Payment Notifications (IPN) can be used to monitor the state
    transition of payment objects.

    With each notification receive, configure API endpoint to
    send Amazon a '200 OK' response immediately after receipt. If '200 OK'
    doesn't send or if server is down when the SNS message is sent,
    Amazon SNS will perform retries every hour for 14 days.
    """

    def __init__(self, body, headers):
        """
        Parameters
        ----------
        body : string
            The body of the SNS message.

        headers : dictionary
            The headers of the SNS message.
        """

        self.error = None

        self._root = None
        self._ns = None
        self._response_type = None
        self._headers = headers
        self._payload = json.loads(body.decode('utf-8'))
        self._pem = None

        self._message_encoded = self._payload['Message']
        self._message = json.loads(self._payload['Message'])
        self._message_id = self._payload['MessageId']
        self._topic_arn = self._payload['TopicArn']
        self._notification_data = self._message['NotificationData']
        self._signing_cert_url = self._payload['SigningCertURL']
        self._signature = self._payload['Signature']
        self._timestamp = self._payload['Timestamp']
        self._type = self._payload['Type']
        self._xml = self._notification_data.replace(
            '<?xml version="1.0" encoding="UTF-8"?>\n',
            '')


    def authenticate(self):
        """
        Attempt to validate a SNS-sign received from Amazon
        header, certificate and hostname checks by default.
        """
        self._validate_header()
        self._validate_cert_url()
        self._get_cert()
        self._validate_signature()

        return True

    def _validate_header(self):
        """
        Compare the header topic_arn to the body topic_arn 
        """
        if 'HTTP_X_AMZ_SNS_TOPIC_ARN' in self._headers:
            if self._topic_arn != self._headers.get(
                    'HTTP_X_AMZ_SNS_TOPIC_ARN'):
                self.error = 'Invalid TopicArn.'
                raise ValueError('Invalid TopicArn')
        else:
            self.error = 'Invalid TopicArn'
            raise ValueError('Invalid TopicArn')

        return True

    def _validate_cert_url(self):
        """
        Checks to see if the certificate URL points to a AWS endpoint and
        validates the signature using the .pem from the certificate URL.
        """
        try:
            url_object = urlparse.urlparse(self._signing_cert_url)
        except:
            raise ValueError('Invalid signing cert URL.')

        if url_object.scheme != 'https':
            raise ValueError('Invalid certificate.')

        if not re.search(
                '^sns\.[a-zA-Z0-9\-]{3,}\.amazonaws\.com(\.cn)?$', url_object.netloc):
            raise ValueError('Invalid certificate.')

        if not re.search('^\/(.*)\.pem$', url_object.path):
            raise ValueError('Invalid certificate.')

        return True

    def _get_cert(self):
        try:
            cert_req = urlopen(url=self._signing_cert_url)
        except Exception as ex:
            self.error = 'Error retrieving certificate.'
            raise ValueError(
                'Error retrieving certificate. {}'.format(
                    ex.reason))

        self._pem = str(cert_req.read())
        return True

    def _validate_signature(self):
        """Generate signing string and validate signature"""
        signing_string = '{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(
            'Message',
            self._message_encoded,
            'MessageId',
            self._message_id,
            'Timestamp',
            self._timestamp,
            'TopicArn',
            self._topic_arn,
            'Type',
            self._type)

        crt = crypto.load_certificate(crypto.FILETYPE_PEM, self._pem)
        signature = base64.b64decode(self._signature)

        try:
            crypto.verify(
                crt,
                signature,
                signing_string.encode('utf-8'),
                'sha1')
        except:
            self.error = 'Invalid signature.'
            raise ValueError('Invalid signature.')

        return True

    def to_json(self):
        """Retuns notification message as JSON"""
        return PaymentResponse(self._xml).to_json()

    def to_xml(self):
        """Retuns notification message as XML"""
        return PaymentResponse(self._xml).to_xml()
