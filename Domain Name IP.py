#Domain Names IP Give Program Using Argparse Argument:- 
#-h for help 
  #It will give -s for SubDomains & -d for Domain Names
  #Eg.Syntax : filename -s subdomain -d domain name
  #          >> test.py -s www -d google.com

import argparse,subprocess as ss

parser = argparse.ArgumentParser(description="This is test tool")

parser.add_argument("-s",type=str, help="Provide -s with SubDomain", required=True)
parser.add_argument("-d",type=str, help="Provide -d with Domain", required=True)

a = parser.parse_args()

print(ss.getoutput("host -t a {}.{}".format(a.s,a.d)))
