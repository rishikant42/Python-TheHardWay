from sys import argv

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA256

def genrate_keys():
    random_generator = Random.new().read
    key = RSA.generate(1024)

    pvt_key = key.exportKey()
    pub_key = key.publickey().exportKey()

    f1 = open('pvtkey.pem', 'w')
    f1.write(pvt_key)
    f1.close()

    f2 = open('pubkey.pem', 'w')
    f2.write(pub_key)
    f2.close()


def import_keys():
    pvt = open('pvtkey.pem').read()
    pub = open('pubkey.pem').read()

    pvtkey = RSA.importKey(pvt)
    pubkey = RSA.importKey(pub)

    # print "\n\n"
    # print pvtkey
    # print "\n\n"
    # print pubkey

    # print "\n\n"
    # print pvtkey.exportKey()
    # print "\n\n"
    # print pubkey.exportKey()

    cipher = pubkey.encrypt('Hello world', 32)
    print cipher

    plain = pvtkey.decrypt(cipher)
    print plain


def create_pswd():
    pswd = str(argv[1])
    digest = SHA256.new(pswd).hexdigest()
    print digest


def verify_pswd():
    pswd = str(argv[1])
    digest = SHA256.new(pswd).hexdigest()
    print digest == str(argv[2])

verify_pswd()
