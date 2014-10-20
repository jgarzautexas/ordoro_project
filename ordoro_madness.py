'''
Ordoro Madness
A big part of what we do at Ordoro is connect to a 3rd-party API, transform their data into a sane format, and save it back to our own API.

Write Python code to make an HTTP request for full.json attached to this gist and then output:

1. list of distinct email addresses.
2. user counts per domain if the domain has more than 1 user.
3. users that logged in during the month of April.

Don't spend more than 1 hour working on the code. Use whatever libraries and code organization you think is best. Give instructions for running your code. If you have a question, just do what you think is right and explain why you did it.

An example might look like this using minimal.json:

>>> python ordoro_madness.py
# uniques
sjobs@apple.com
muaddib@dune.com
admin@nsa.com
richard@piedpiper.com
erlich@piedpiper.com
# domains with > 1 user
('piedpiper.com', 2)
# april logins
{'login_date': '2014-04-01T01:02:03+00:00', 'email': 'richard@piedpiper.com'}
{'login_date': '2014-04-10T11:22:33+00:00', 'email': 'sjobs@apple.com'}
{'login_date': '2014-04-24T14:12:34+00:00', 'email': 'admin@nsa.com'}

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
    api_url = 'https://gist.githubusercontent.com/benweatherman/e25017016bed9625fc03/raw/543ad1119fae380acfe3268e51a5c421c4288cb7/minimal.json'
    ordoro_madness(api_url)
    pass


if __name__ == '__main__':
    main()