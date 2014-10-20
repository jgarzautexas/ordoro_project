'''
Utility functions for ordoro madness
'''

from collections import Counter
import datetime
import json
import operator
import re

import dateutil.parser

def print_pretty_json(master_dict):
    '''
    Used for debuging to see python objs in a readable format
    '''
    print json.dumps(master_dict,
                     sort_keys=True,
                     indent=4,
                     separators=(',',': '))
    return

def marshal_data(login_data):
    '''
    Does most of the heavy loading of the ordoro madness main function
    '''
    
    # Initialize parameters
    master_dict = {
        "uniques": {},
        "domains": [],
        "april_logins": [],
        "sorted_domains": []
    }
    email_domain_list = []

    # Debug with python set
    # emails = [d.get("email").strip() for d in login_data if d.get("email")]
    # unique_emails = set(emails)
    
    for login in login_data:
        # print login
        login_date = login.get("login_date")

        if login_date:
            py_dt = convert_json_datetime(login_date)

            email = login.get("email")
            if email:
                # Clean extra whitespace and validate
                strip_email = email.strip()
                if validate_email(strip_email):
                    # This overrides the unique dictionary.
                    # Only used for uniqueness
                    master_dict.get("uniques").update({strip_email: login})
                    
                    email_domain_val = get_email_domain(strip_email)[1:]
                    email_domain_list.append(email_domain_val)
                    email_domain_list.sort()
                    master_dict['sorted_domains'] = email_domain_list

                else:
                    continue

                if check_month_of_april(py_dt):
                    master_dict.get("april_logins").append(login)
            
    if email_domain_list:
        domain_counter = Counter(email_domain_list)
        greater_than_one_list = get_email_domain_greater_than_one(
            domain_counter.most_common()
        )

        master_dict["domains"] = greater_than_one_list

    if master_dict.get("april_logins"):
        master_dict.get("april_logins").sort(
            key=operator.itemgetter('login_date')
        )

    # print print_pretty_json(master_dict)

    return master_dict

def get_email_domain_greater_than_one(email_domain_list):
    '''
    Check if the counter has more than one user per domain
    '''
    greater_than_one = []

    for ed in email_domain_list:

        if ed[1] > 1:
            domain_str = str(ed[0])
            greater_than_one.append((domain_str, ed[1]))
        
    return greater_than_one


def convert_json_datetime(json_date):
    '''
    Creates a datetime object from json_date format.
    '''

    new_date = dateutil.parser.parse(json_date)

    return new_date

def check_month_of_april(dt):
    '''
    Check datetime object for month of April

    '''
    APRIL = 4

    if dt.month == APRIL:
        return True

    return False

def validate_email(email):
    '''
    Simply email validator.
    '''
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    valid_email = re.match(pattern, email)

    return bool(valid_email)

def get_email_domain(email):
    '''
    Regex to find domain of email address.
    '''

    domain = re.search("@.*", email)

    return domain.group()

def main():
    pass

if __name__ == '__main__':
    main()