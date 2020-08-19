#!/usr/bin/python

import re,os,requests,json,sys
from prettytable import PrettyTable


API_KEY=""
MAXIMUM_DAYS_TO_LOOK=365


print("\n\nForensic Abuse IP Check by")

print("""
 ____  ____  __    __  __  ___  _   _    __   
(  _ \(_  _)(  )  (  )( ) / __)( )_( )  /__\  
 )(_) )_)(_  )(__  )(__)( \__ \ ) _ (  /(__)\ 
(____/(____)(____)(______)(___/(_) (_)(__)(__)
""")


if not API_KEY:
        print("\n** ERROR ** Enter API v2 from abuseipdb.com \n")
else:

        #get the firts argument: file name
        input_xml_file_name=sys.argv[1]

        f = open(input_xml_file_name, 'r')
        raw_text = str(f.readlines())
        f.close()

        #find ip addresses using reg ex
        ip_address = r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})'
        foundip = re.findall( ip_address, raw_text )

        uniqIpList=list(set(foundip))

        print("\nSelecting unique ",len(uniqIpList),"ip addresses from ",len(foundip),". Daily check limit is 1000 IPs for free account.")
        print("\nData fetching from abuseipdb.com from last ",MAXIMUM_DAYS_TO_LOOK," days")


        number_of_occurence_ip=[]

        for i in uniqIpList:
                count=raw_text.count(i)
                number_of_occurence_ip.append(count)

        t = PrettyTable()
        t.add_column('IP', uniqIpList)
        t.add_column('Count',number_of_occurence_ip)


        countryCode=[]
        abuseConfidenceScore=[]
        totalReports=[]

        print("\nGetting Data, Please Wait ....\n")


        count=0
        for i in uniqIpList:

                count=count+1


                url = 'https://api.abuseipdb.com/api/v2/check'

                querystring = {
                    'ipAddress': i,
                    'maxAgeInDays': MAXIMUM_DAYS_TO_LOOK
                }

                headers = {
                    'Accept': 'application/json',
                    'Key': API_KEY
                }

                response = requests.request(method='GET', url=url, headers=headers, params=querystring)

                # Formatted output
                decodedResponse = json.loads(response.text)

                try:
                        countryCode.append((decodedResponse.get('data').get('countryCode')).strip("<"))
                except:
                        countryCode.append("ERR")

                try:
                        abuseConfidenceScore.append((decodedResponse.get('data').get('abuseConfidenceScore')))
                except:
                        abuseConfidenceScore.append(0)

                try:
                        totalReports.append((decodedResponse.get('data').get('totalReports')))
                except:
                        totalReports.append(0)



                print(int(count*100/len(uniqIpList)),"% ",sep=' ', end='', flush=True)


        #print(countryCode)

        t.add_column('Country',countryCode)
        t.add_column('Abuse Confidence',abuseConfidenceScore)
        t.add_column('Total Reports',totalReports)


        print("\n\n+++++++++++++++ Sort by Count +++++++++++++++\n")
        t.sortby = "Count"
        t.reversesort = True
        print(t)


        print("\n\n+++++++++++++++ Sort by Country +++++++++++++++\n")
        t.sortby = "Country"
        print(t)


        print("\n\n+++++++++++++++ Sort by Abuse Confidence +++++++++++++++\n")
        t.sortby = "Abuse Confidence"
        print(t)


        print("\n\n+++++++++++++++ Sort by Total Reports +++++++++++++++\n")
        t.sortby = "Total Reports"
        print(t)
