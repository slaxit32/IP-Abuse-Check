# IP-Abuse-Check
Simple IP Abuse Checking Script
This application grab IP addresses from a file and give abuse information of that IP. This will output IP address, number of occurrence in the file, related country, abuse confidence and total number of reports. Output will generate table sorted with above catagories.

***** Running Requirement:

    • Python 3

***** Library Requirements:

Use pip (pip3) to install following libraries. (eg. pip install requests )

    • requests
    • json
    • re
    • prettytable

***** API Requirements

https://www.abuseipdb.com API version 2 is used for data query. Create a API v2 key (free account also available. Only 1000 queries per day.) from the site (https://www.abuseipdb.com/account/api) and paste in the code for API_KEY variable.

***** How to run.

From a command line run

python3 ipAbuseCheck.py <file_name_with_extension_that_contain_IP_addresses.>

***** Variables.

MAXIMUM_DAYS_TO_LOOK variable define number of days to check. Maximum is 365 days.

Eg. MAXIMUM_DAYS_TO_LOOK=365

API_KEY variable define the api key.

Eg. API_KEY="jfoij3984jjf43rjlkejf9uefl3jr9843ufje"
