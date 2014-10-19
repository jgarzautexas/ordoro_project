ordoro_project
==============

A big part of what we do at Ordoro is connect to a 3rd-party API, transform their data into a sane format, and save it back to our own API.

Write Python code to make an HTTP request for full.json attached to this gist and then output:

list of distinct email addresses.
user counts per domain if the domain has more than 1 user.
users that logged in during the month of April.
Don't spend more than 1 hour working on the code. Use whatever libraries and code organization you think is best. Give instructions for running your code. If you have a question, just do what you think is right and explain why you did it.

Here are the steps to get started with testing. 
    
    * Create a virtualenv and activate. 
    
    * pip install -r requirements.txt


You can execute the ordoro_madness.py module directly and uncomment the api_url in main function to call the desired json file. 
```
$python ordoro_madness.py
#Sample Output
# Uniques Total 100
vernon.fadel@denesik.com
helyn67@cruickshankmckenzie.com
arice@greenholtconsidine.com
henery76@yahoo.com
....
# domains with > 1 user
('hotmail.com', 24)
('gmail.com', 19)
('yahoo.com', 18)
....
etc

```


Running pytest from the terminal will run some simple test to make sure functionality is working. 
