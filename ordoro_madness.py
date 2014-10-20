'''
Ordoro Madness
A big part of what we do at Ordoro is connect to a 3rd-party API, transform their data into a sane format, and save it back to our own API.

Write Python code to make an HTTP request for full.json attached to this gist and then output:

list of distinct email addresses.
user counts per domain if the domain has more than 1 user.
users that logged in during the month of April.

'''

import logging
import requests

import utils

def ordoro_madness(api_url):
    '''
    Main function to initiate fetching parsing login data.
    '''

    res = requests.get(api_url,
                       params={},
                       headers={},
                       verify=False)

    if res.ok and utils.validate_json(res.text):

        master_data = utils.marshal_data(res.json().get("data"))

        print "# Uniques Total {0}".format(len(master_data.get("uniques")))
        for unique in master_data.get("uniques"):
            print unique

        print "# domains with > 1 user"
        for domain in master_data.get("domains"):
            print domain

        print "# April Logins {0}".format(len(master_data.get("april_logins")))
        for login in master_data.get("april_logins"):
            print login

    else:
        logging.error("Bad Request or Invalid json.")
        raise

    return master_data

def main():
    '''
    Main function
    Uncomment to test from module.
    '''
    api_url = "https://gist.githubusercontent.com/benweatherman/e25017016bed9625fc03/raw/145698b6185d1109f7b4a8c1576a4e862b8b52f7/full.json"
    # api_url = 'https://gist.githubusercontent.com/benweatherman/e25017016bed9625fc03/raw/543ad1119fae380acfe3268e51a5c421c4288cb7/minimal.json'
    ordoro_madness(api_url)
    pass


if __name__ == '__main__':
    main()