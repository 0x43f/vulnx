#!/usr/bin/env python
# Title : vulnx
# Author: anouarbensaad
# Desc  : CMS-Detector and Vulnerability Scanner & exploiter
"""The vulnx main part."""

import sys
import argparse
import re
import os
import socket
import common
import warnings
import signal
from common.threading import threads
from common.colors import red, green, bg, G, R, W, Y, G , good , bad , run , info , end
from common.banner import banner
from common.uri_converter import convert_uri as hostd
from common.vxrequest import random_UserAgent
from common.vxrequest import getrequest as vxget
from common.grabwp import (wp_version,wp_plugin,wp_themes,wp_user)
from common.output_wr import writelogs as outlogs
from common.wp_exploits import(   wp_wysija,
                                  wp_blaze,
                                  wp_catpro,
                                  wp_cherry,
                                  wp_dm,
                                  wp_fromcraft,
                                  wp_jobmanager,
                                  wp_showbiz,
                                  wp_synoptic,
                                  wp_shop,
                                  wp_powerzoomer,
                                  wp_revslider,
                                  wp_adsmanager,
                                  wp_inboundiomarketing,
                                  wp_levoslideshow,
                                  wp_adblockblocker,
                                )
from common.joomla_exploits import(joomla_comjce)
#cleaning screen
def parser_error(errmsg):
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print(R + "Error: " + errmsg + W)
    sys.exit()

def parse_args():
    # parse the arguments
    banner()
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -u google.com")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-u', '--url', help="Url scanned for")
    parser.add_argument('-D', '--dorks', help='searching dorks', dest='dorks' , type=str)
    parser.add_argument('-o', '--output', help='output directory',required=False)
    parser.add_argument('-t', '--timeout', help='http request timeout', dest='timeout',type=float)
    parser.add_argument('-c', '--cms-info', help='http request timeout', dest='cms', choices=['user', 'themes','version','plugins','all'])
    parser.add_argument('--threads', help="num threads working", dest='numthread', type=float)
    #Switches
    parser.add_argument('-e','--exploit', help='searching vulnerability & run exploits',
    dest='exploit', action='store_true')
    parser.add_argument('-w','--web-info', help='searching web info',
    dest='webinfo', action='store_true')
    parser.add_argument('-d','--domain-info', help='searching domain info',
    dest='domaininfo', action='store_true')
    parser.add_argument('-l','--dork-list', help='listing names of exploits',
    dest='dorkslist', action='store_true')
    return parser.parse_args()

vulnresults = set()  # results of vulnerability exploits. [success or failed]
grabinfo = set()  # return cms_detected the version , themes , plugins , user .. 
subdomains = set() # return subdomains & ip.
hostinfo = set() # host info
#args declaration
args = parse_args()
#url arg
url = args.url
#dorks arg
dorks = args.dorks
#run exploit
exploit = args.exploit
#cms gathering args
cms = args.cms
# web hosting info
webinfo = args.webinfo
# domain info
domaininfo = args.domaininfo
# dorks search.
dorks = args.dorks
dorkslist = args.dorkslist
# timeout
timeout = args.timeout or 3
#thread
numthread = args.numthread or 1



# Disable SSL related warnings
warnings.filterwarnings('ignore')

def detect_cms():
    id = 0
    lm = url + '/smiley/1.gif'
    lm_content = vxget(lm,headers)
    lm2 = url + '/rss.xml'
    lm2_content = vxget(lm2,headers)
    content=vxget(url,headers)
    try:
        #joomla searching content to detect.
        if  re.search(re.compile(r'<script type=\"text/javascript\" src=\"/media/system/js/mootools.js\"></script>|/media/system/js/|com_content|Joomla!'), content):
            print ('%s[%i] Target -> %s %s CMS : Joomla \n\n%s' % (W,id,url,G,W))
            print (' %s Check Vulnerability' %(run))
            #joomla_exploits imported from folder[./common/joomla_exploits.py]
            if exploit:
                joomla_comjce(url,headers)
        #prestashop searching content to detect.
        elif re.search(re.compile(r'Prestashop|prestashop'), content):
            print ('%s Target[%i] -> %s%s \n\n '% (W,id,url,end))
            print ('------------------------------------------------')
            print (' %s %sCMS :%s Prestashop' % (good,W,end))
            print ('------------------------------------------------')
            prestashop_version()
            domain_info(subdomains)
            print (' %s Check Vulnerability' %(run))
        #wordpress searching content to detect.
        elif re.search(re.compile(r'wp-content|wordpress|xmlrpc.php'), content):
            print ('%s Target[%i] -> %s%s \n\n '% (W,id,url,end))
            print ('------------------------------------------------')
            print (' %s %sCMS :%s Wordpress' % (good,W,end))
            print ('------------------------------------------------')
            if webinfo:
                webhosting_info(hostinfo)
            if domaininfo:
                domain_info(subdomains)
            #wp_grab methods info from (folder)[./common/grapwp.py]
            if cms == 'version':
                print (' %s Check CMS Info' %(run))
                wp_version(url,headers,grabinfo)
                print ("-----------------------------------------------")
            if cms == 'themes':
                print (' %s Check CMS Info' %(run))
                wp_themes(url,headers,grabinfo)
                print ("-----------------------------------------------")
            if cms == 'user':
                print (' %s Check CMS Info' %(run))
                wp_user(url,headers,grabinfo)
                print ("-----------------------------------------------")
            if cms == 'plugins':
                print (' %s Check CMS Info' %(run))
                wp_plugin(url,headers,grabinfo)
                print ("-----------------------------------------------")
            if cms == 'all':
                print (' %s Check CMS Info' %(run))
                wp_version(url,headers,grabinfo)
                wp_themes(url,headers,grabinfo)
                wp_user(url,headers,grabinfo)
                wp_plugin(url,headers,grabinfo)
                print ("-----------------------------------------------")


            # vulnx -u http://example.com -e | vulnx -u http://example --exploit
            if exploit:
                print (' %s Check Vulnerability\n' %(run))
                print (""" %sNAME                      %sSTATUS  %sSHELL"""%(W,W,W))
                #wp_exploit methods from (dolder)[./common/wp_exploits.py]
                wp_wysija(url,headers,timeout,vulnresults)
                wp_blaze(url,headers,timeout,vulnresults)
                wp_synoptic(url,headers,timeout,vulnresults)
                wp_catpro(url,headers,timeout,vulnresults)
                wp_cherry(url,headers,timeout,vulnresults)
                wp_dm(url,headers,timeout,vulnresults)
                wp_fromcraft(url,headers,timeout,vulnresults)
                wp_jobmanager(url,headers,timeout,vulnresults)
                wp_showbiz(url,headers,timeout,vulnresults)      
                wp_shop(url,headers,timeout,vulnresults)
                wp_powerzoomer(url,headers,timeout,vulnresults)
                wp_revslider(url,headers,timeout,vulnresults)
                wp_adsmanager(url,headers,timeout,vulnresults)
                wp_inboundiomarketing(url,headers,timeout,vulnresults)
                wp_adblockblocker(url,headers,timeout,vulnresults)
                wp_levoslideshow(url,headers,timeout,vulnresults)
                print ("-----------------------------------------------")
        #Drupal searching content to detect.
        elif re.search(re.compile(r'Drupal|drupal|sites/all|drupal.org'), content):
            print ('%s Target[%i] -> %s%s \n\n '% (W,id,url,end))
            print ('------------------------------------------------')
            print (' %s CMS : Drupal' % (good))
            print ('------------------------------------------------')
            drupal_version()
            domain_info(subdomains)
            print (' %s Check Vulnerability' %(run))
        #OpenCart detection
        elif re.search(re.compile(r'route=product|OpenCart|route=common|catalog/view/theme'), content):
            print ('%s Target[%i] -> %s%s \n\n '% (W,id,url,end))
            print ('------------------------------------------------')
            print (' %s CMS : OpenCart' % (good))
            print ('------------------------------------------------')
            domain_info(subdomains)
            print (' %s Check Vulnerability' %(run))
        #magento detection
        elif re.search(re.compile(r'Log into Magento Admin Page|name=\"dummy\" id=\"dummy\"|Magento'), content):
            print ('%s Target[%i] -> %s%s \n\n '% (W,id,url,end))
            print ('------------------------------------------------')
            print (' %s CMS : Magento' % (good))
            print ('------------------------------------------------')
            domain_info(subdomains)
        #lokomedia
            print (' %s Check Vulnerability' %(run))
        elif re.search(re.compile(r'image/gif'), lm_content):
            print ('%s Target[%i] -> %s%s \n\n '% (W,id,url,end))
            print ('------------------------------------------------')
            print (' %s CMS : Lokomedia' % (good))
            print ('------------------------------------------------')
            domain_info(subdomains)
            print (' %s Check Vulnerability' %(run))
        elif re.search(re.compile(r'lokomedia'), lm2_content):
            print ('%s Target[%i] -> %s%s \n\n '% (W,id,url,end))
            print ('------------------------------------------------')
            print (' %s CMS : Lokomedia' % (good))
            print ('------------------------------------------------')
            domain_info(subdomains)
            print (' %s Check Vulnerability' %(run))
        else:
            print ('%s Target[%i] -> %s%s \n\n '% (W,id,url,end))
            print ('------------------------------------------------')
            print (' %s CMS : Unknown' % (bad))
            print ('------------------------------------------------')
            webhosting_info(hostinfo)
            domain_info(subdomains)
    except Exception as e:
        print ('%s\n\n error : %s%s' % (R,e,W))

# drupal Version
def drupal_version():
    response = vxget(url,headers,timeout)
    regex = 'Drupal \d{0,10}'
    regex = re.compile(regex)
    matches = regex.findall(response)
    if len(matches) > 0 and matches[0] != None and matches[0] != "":
        version = matches[0]
        print ('%s [+] Drupal Version : %s %s' %(G,version,W))

# Prestashop Version
def prestashop_version():
    response = vxget(url,headers,timeout)
    regex = 'Prestashop \d{0,9}'
    regex = re.compile(regex)
    matches = regex.findall(response.text)
    if len(matches) > 0 and matches[0] != None and matches[0] != "":
        version = matches[0]
        return print ('%s [+] Prestashop Version : %s %s' %(G,version,W))

# scan domain info
def domain_info(subdomains):
    print (' %s Search for SubDomains' % (run))
    searchurl = "https://www.pagesinventory.com/search/?s=" + url
    getinfo = vxget(searchurl,headers,timeout)
    domains = []
    #searching domain from pages inventory
    matches_domain = re.findall(re.compile(r'<td><a href=\"\/domain\/(.*?).html\">'),getinfo)
    match_ip = re.findall(re.compile(r'<a href=\"/ip\/(.*?).html\">'),getinfo)
    if len(matches_domain) > 0:
        for domain in matches_domain:
            if domain not in domains:
                domains.append(domain)
                subdomains.add('domain : '+domain)
    print (' %s SubDomains : %s ' %(good," \n                  ".join(domains)))
    if match_ip and len(match_ip) > 0 and match_ip[0] != None and match_ip[0] != "":
        IP = match_ip[0]
        print (' %s IP : %s' %(good,IP))
        subdomains.add('ip : '+IP)
    print ("-----------------------------------------------")

# Web Hosting Information
def webhosting_info(hostinfo):
    print (' %s Web Hosting Information' % (run))
    urldate = "https://input.payapi.io/v1/api/fraud/domain/age/" + hostd(url)
    getinfo = vxget(urldate,headers,timeout)
    regex_date = r'Date: (.+?)-(.+?)'
    regex_date = re.compile(regex_date)
    matches = re.search(regex_date,getinfo)
    if matches:
        print ( ' %s Domain Created on : %s' % (good,matches.group(1)))
    ip = socket.gethostbyname(hostd(url))
    print ( ' %s CloudFlare IP : %s' % (good,ip))
    ipinfo = "http://ipinfo.io/" + ip + "/json"
    getipinfo = vxget(ipinfo,headers,timeout)
    country = re.search(re.compile(r'country\": \"(.+?)\"'),getipinfo)
    region = re.search(re.compile(r'region\": \"(.+?)\"'),getipinfo)
    latitude = re.search(re.compile(r'latitude: (.+?)'),getipinfo)
    longitude = re.search(re.compile(r'longitude\": \"(.+?)\"'),getipinfo)
    timezone = re.search(re.compile(r'timezone\": \"(.+?)\"'),getipinfo)
    ans = re.search(re.compile(r'ans\": \"(.+?)\"'),getipinfo)
    org = re.search(re.compile(r'org\": \"(.+?)\"'),getipinfo)
    if country:
        print(' %s Country : %s' % (good,country.group(1)))
    if region:
        print(' %s Region : %s' % (good,region.group(1)))
    if latitude:
        print(' %s Latitude : %s' % (good,latitude.group(1)))
    if longitude:
        print(' %s Longitude : %s' % (good,longitude.group(1)))
    if timezone:
        print(' %s Timezone : %s' % (good,timezone.group(1)))
    if ans:
        print(' %s Ans : %s' % (good,ans.group(1)))
    if org:
        print(' %s Org : %s' % (good,org.group(1)))
    print ("-----------------------------------------------")
# output
output_dir = args.output or 'logs'

if not os.path.exists(output_dir): # if the directory doesn't exist
    os.mkdir(output_dir) # create a new directory

data = [ vulnresults, grabinfo, subdomains , hostinfo]

data_names = ['vulnresults', 'grabinfo', 'subdomains' , 'hostinfo']
outlogs(data,data_names,output_dir)
data = {
    'vulnresults':list(vulnresults),
    'grabinfo':list(grabinfo),
    'subdomains':list(subdomains),
}

#clean  
def signal_handler(signal,frame):
    print("%s(ID: {}) Cleaning up...\n Exiting...".format(signal)%(W))
    exit(0)
signal.signal(signal.SIGINT, signal_handler)

#main
if __name__ == "__main__":
    banner()
    if url:
        #default headers.
        headers = {
        'Host' : hostd(url),
        'User-Agent' : random_UserAgent(),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        }
        threads(detect_cms,numthread)
    if dorks:
        from common.vx_dorks import (searchengine,getdorksbyname,wp_contentdorks)
        searchengine(dorks)
    if dorkslist:
        from common.dorks_list import dorkslist as lsdorks
        lsdorks()