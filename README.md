<h1 align="center">
  <br>
  <a href="https://github.com/anouarbensaad/VulnX"><img src="https://i.ibb.co/kXW18B6/vulnxsmall.png" alt="VulnX"></a>
  <br>
  VulnX
  <br>
</h1>

<h4 align="center">Vulnx 🕷️ Cms And Vulnerabilites Detector And An Intelligent Auto Shell Injector</h4>

<p align="center">
  <a href="https://github.com/anouarbensaad/vulnx/releases">
    <img src="https://img.shields.io/github/release/anouarbensaad/vulnx.svg">
  </a>
  <a href="https://github.com/anouarbensaad/vulnx/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues-closed/anouarbensaad/vulnx.svg">
  </a>
  <a href="https://travis-ci.com/anouarbensaad/vulnx">
    <img src="https://img.shields.io/travis/com/anouarbensaad/vulnx.svg">
  </a>
</p>

![demo](https://i.ibb.co/wrZgjWn/New-Project-2.jpg)

<p align="center">
  <a href="https://github.com/anouarbensaad/vulnx/wiki">VulnX Wiki</a> •
  <a href="https://github.com/anouarbensaad/vulnx/wiki/Usage">How To Use</a> •
  <a href="https://github.com/anouarbensaad/vulnx/wiki/Compatibility-&-Dependencies">Compatibility</a> •
</p>

**Vulnx** is a cms and vulnerabilites detection, an intelligent [exploits injection](https://github.com/anouarbensaad/vulnx/wiki/Usage#run-exploits), fast cms detection of target and fast scanner and informations gathering like subdomains, ipaddresses, country, org, timezone, region, ans and more ...

Instead of injecting shell and checking it works like all the other tools do, vulnx analyses the response with and recieve if shell success uploaded or no. vulnx is searching for urls with [dorks](https://github.com/anouarbensaad/vulnx/wiki/Usage#searching-dorks). 

### Features

- Detect cms (wordpress, joomla, prestashop, drupal, opencart, magento, lokomedia)
- Target informations gatherings
- Target Subdomains gathering
- Multi-threading on demand
- Checks for vulnerabilites
- Auto shell injector
- Exploit dork searcher

### Exploits
<h1 align="center">
<a href="https://github.com/anouarbensaad/VulnX"><img src="https://user-images.githubusercontent.com/23563528/58003677-2e03be80-7ad9-11e9-9774-c69a38248c64.gif" alt="Exploits Running"></a>
</h1>

#### Joomla
- [x] [Com Jce            ]('#')
- [ ] [Com Jwallpapers    ]('#')
- [ ] [Com Jdownloads     ]('#')
- [ ] [Com Weblinks       ]('#')
- [ ] [Com Fabrik         ]('#')
- [ ] [Com Jdownloads Index]('#')
- [ ] [Com Foxcontact     ]('#')
- [ ] [Com Blog           ]('#')
- [ ] [Com Users          ]('#')
- [ ] [Com Ads Manager    ]('#')
- [ ] [Com Sexycontactform]('#')
- [ ] [Com Media          ]('#')
- [ ] [Mod_simplefileupload]('#')
- [ ] [Com Facileforms    ]('#')

#### Wordpress
- [x] [Simple Ads Manager   ](https://www.exploit-db.com/exploits/36614)
- [x] [InBoundio Marketing  ](https://www.rapid7.com/db/modules/exploit/unix/webapp/wp_inboundio_marketing_file_upload) 
- [x] [WPshop eCommerce     ](https://www.rapid7.com/db/modules/exploit/unix/webapp/wp_wpshop_ecommerce_file_upload)
- [x] [Synoptic             ](https://cxsecurity.com/issue/WLB-2017030099) 
- [x] [Showbiz Pro          ](https://www.exploit-db.com/exploits/35385) 
- [x] [Job Manager          ](https://www.exploit-db.com/exploits/45031) 
- [x] [Formcraft            ](https://www.exploit-db.com/exploits/30002)
- [x] [PowerZoom            ](http://www.exploit4arab.org/exploits/399)
- [x] [Download Manager     ](https://www.exploit-db.com/exploits/35533)
- [x] [CherryFramework      ](https://www.exploit-db.com/exploits/45896)
- [x] [Catpro               ](https://vulners.com/zdt/1337DAY-ID-20256)
- [x] [Blaze SlideShow      ](https://0day.today/exploits/18500)
- [x] [Wysija-Newsletters   ](https://www.exploit-db.com/exploits/33991)

#### Drupal
- [ ] [Add Admin            ]('#')
- [ ] [Drupal BruteForcer   ]('#')
- [ ] [Drupal Geddon2       ]('#')

#### PrestaShop
- [ ] [attributewizardpro   ]('#')
- [ ] [columnadverts        ]('#')
- [ ] [soopamobile          ]('#')
- [ ] [pk_flexmenu          ]('#')
- [ ] [pk_vertflexmenu      ]('#')
- [ ] [nvn_export_orders    ]('#')
- [ ] [megamenu             ]('#')
- [ ] [tdpsthemeoptionpanel ]('#')
- [ ] [psmodthemeoptionpanel]('#')
- [ ] [masseditproduct      ]('#')
- [ ] [blocktestimonial     ]('#')
- [ ] [soopabanners         ]('#')
- [ ] [Vtermslideshow       ]('#')
- [ ] [simpleslideshow      ]('#')
- [ ] [productpageadverts   ]('#')
- [ ] [homepageadvertise    ]('#')
- [ ] [homepageadvertise2   ]('#')
- [ ] [jro_homepageadvertise]('#')
- [ ] [advancedslider       ]('#')
- [ ] [cartabandonmentpro   ]('#')
- [ ] [cartabandonmentproOld]('#')
- [ ] [videostab            ]('#')
- [ ] [wg24themeadministration]('#')
- [ ] [fieldvmegamenu       ]('#')
- [ ] [wdoptionpanel        ]('#')

#### Opencart
- [ ] [Opencart BruteForce]('#')

### Available command line options
[`READ VULNX WIKI`](https://github.com/anouarbensaad/vulnx/wiki/Usage)

    usage: vulnx [options]
    
      -u --url              url target to scan
      -D --dorks            search webs with dorks
      -o --output           specify output directory
      -t --timeout          http requests timeout
      -c --cms-info         search cms info[themes,plugins,user,version..]
      -e --exploit          searching vulnerability & run exploits
      -w --web-info         web informations gathering
      -d --domain-info      subdomains informations gathering
      -l, --dork-list       list names of dorks exploits
      --threads             number of threads

### Docker

VulnX can be launched in docker.

```bash
$ git clone https://github.com/anouarbensaad/VulnX.git
$ cd VulnX
$ docker build -t vulnx ./docker/
$ docker run -it --name vulnx vulnx:latest -u http://exemple.com
```

make a local volume to view the results into a logfile

```bash
$ docker run -it --name vulnx -v "$PWD/logs:/VulnX/logs" vulnx:latest -u http://exemple.com
```

### Install VulnX


```bash
$ git clone https://github.com/anouarbensaad/VulnX.git
$ cd VulnX
$ chmod + x install.sh
$ ./install.sh
```

Now run `vulnx`

##### example command with options : settimeout=3 , cms-gathering = all , -d subdomains-gathering , run --exploits
`vulnx -u http://example.com --timeout 3 -c all -d -w --exploit` 

##### example command for searching dorks : -D or --dorks , -l --list-dorks 
`vulnx --list-dorks`
return table of exploits name.
`vulnx -D blaze`
return urls found with blaze dork

### Contribution & License

You can contribute in following ways:

- [Report bugs & add issues](https://github.com/anouarbensaad/VulnX/issues/new)
- Search for new vulnerability

Do you want to have a conversation in private? email me : Bensaad.tig@gmail.com

***VulnX*** is licensed under [MIT License](https://github.com/anouarbensaad/VulnX/blob/master/LICENSE) **

### :warning: Warning !!

***I don't Accept any responsibility for any illegal usage.***
