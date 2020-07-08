import random
import time
import sys
import os
import names
import pycountry
import os, sys
import configparser

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

os.system('cls')
def cardgenerator():
    mmdic = ['01','02','03','04','05','06','07','08','09','10','11','12']
    binn = random.randint(400000,499999)
    mm = random.choice(mmdic)
    yy = random.randint(2020,2026)
    geneccv = random.randint(100,999)
    genenum = random.randint(1000000000,9999999999)
    creditcard = (binn,genenum)
    creditcardstr = "%s%s"%(creditcard)
    all = creditcardstr,"|",mm,"|",yy,"|",geneccv
    allstring = "%s%s%s%s%s%s%s"%(all)
    print(allstring)

rname = names.get_first_name()
rlastname = names.get_last_name()
gmails = ["gmail.com","mail.ru","live.fr","outlook.fr","yahoo.com"]
gmail = random.choice(gmails)
num = random.randint(1900,2020)
allg = (rname,num,"@",gmail)
eall = "%s%s%s%s"%(allg)

cdic =['AF','AL','TR','US','UK','RU','FR','RO','DE','DA','JP','BE','BG','BR','CA','CH','DK','EG','ES','GL','GR','IS','NL',]
rc = random.choice(cdic) 
country = pycountry.countries.get(alpha_2=rc)
randcountry = country.name
ncountry = ("Country : " + randcountry)
card = ("Card : ")

time.sleep(1)
print(f"""
{re}.d88888b  {cy}         dP                   {re} .88888.
{re}88.    "' {cy}         88                   {re}d8'   `88
{re}`Y88888b. {cy}.d8888b. 88 .d8888b. dP.  .dP {re}88
{re}      `8b {cy}88ooood8 88 88'  `88  `8bd8'  {re}88   YP88
{re}d8'   .8P {cy}88.  ... 88 88.  .88  .d88b.  {re}Y8.   .88
{re} Y88888P  {cy}`88888P' dP `88888P8 dP'  `dP {re} `88888'

                        v1.0
                    t.me/selaxg
        {gr}""")
time.sleep(1)
print("Name : " + rname + " " + rlastname)
time.sleep(0.5)
print("E-Mail : " + eall)
time.sleep(0.5)
print(ncountry)
time.sleep(0.5)
print(card),cardgenerator()
time.sleep(120)