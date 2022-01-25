'''
Virus Total Hash Uploader
'''

import json
import hashlibgi
from virus_total_apis import PublicApi as VirusTotalPublicApi

# You will need to obtain an API Key from Virus Total
API_KEY = ''

vt = VirusTotalPublicApi(API_KEY)


def get_file():
    file_path = input("Please enter file name. MUST BE IN SAME WORKING DIRECTORY \n ")
    if os.path.isfile(file_path):
        md5checksum(file_path)
    else:
        print("Not a file or couldn't find it")
        get_file()


def md5checksum(file_path):

    md5 = hashlib.md5()

    # handle content in binary form
    f = open(file_path, "rb")

    while chunk := f.read(4096):
        md5.update(chunk)

    hashx = md5.hexdigest()
    print(hashx)
    response = vt.get_file_report(hashx)
    print(json.dumps(response, sort_keys=False, indent=4))


get_file()
