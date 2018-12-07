import os
from acrcloud.recognizer import ACRCloudRecognizer
import urllib2
import sys

if __name__ == '__main__':
    config = {
        'host':'identify-ap-southeast-1.acrcloud.com',
        'access_key': os.environ['ACR_KEY'],
        'access_secret': os.environ['ACR_SECRET'],
        'timeout':20 # seconds
    }

    re = ACRCloudRecognizer(config)
    # print re.recognize_by_file(sys.argv[1], 0)

    buf = urllib2.urlopen('https://s3.us-east-2.amazonaws.com/attendance-monitor/Selena+Gomez++The+Scene+-+Who+Says-%5BAudioTrimmer.com%5D.mp3').read()
    print re.recognize_by_filebuffer(buf, 0)
