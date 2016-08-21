from sys import argv
from os import system
from time import sleep
from random import randint
from redis import StrictRedis

bold = "\033[1m"
underline = "\033[4m"
green = "\033[92m"
blue = "\033[94m"
yellow = "\033[93m"
red = "\033[91m"
endcolor = "\033[0m"

def logo():
    system("clear")
    print "--==["+bold+blue+"nickname"+endcolor+"] [ esw0rmer"
    print "--==["+bold+yellow+"MyGitHub"+endcolor+"] [ http://github.com/esw0rmer"
    print "--==["+bold+green+"software"+endcolor+"] [ RanRed"
    print "-"*43

def helpMe():
    print "Using:"
    print "\t"+bold+"~$"+endcolor+" python ranred.py "+green+"-h [host] -k [key]"+endcolor
    print "\t\t<< or >>"
    print "\t"+bold+"~$"+endcolor+" python ranred.py "+green+"-h [host] -k [key] -t [time]"+endcolor
    print "\t\t<< example >>"
    print "\t"+bold+"~$"+endcolor+" python ranred.py "+green+"-h 'localhost'"+endcolor+" "+yellow+"-k 'CWKey'"+endcolor
    print "\t"+bold+"~$"+endcolor+" python ranred.py "+green+"-h 'localhost'"+endcolor+" "+yellow+"-k 'CWKey'"+endcolor+" "+blue+"-t 5"+endcolor
    print ""

def domis(rHost, rKey, rTime):
    while True:
        rds = StrictRedis(host=rHost, port=6379, db=0)
        rNumber = randint(1, 999999999)
        rds.set(rKey, rNumber)
        vData = rds.get(rKey)
        print "Instant Value:",vData
        sleep(int(rTime))

logo()
if len(argv) == 7:
    host, key, time = argv[2], argv[4], argv[6]
    domis(host, key, time)
elif len(argv) == 5:
    host, key, time = argv[2], argv[4], 5
    domis(host, key, time)
else:
    helpMe()

# python ranred.py -h host -k key -t time
