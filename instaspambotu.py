Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:19:08) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # coding=utf-8
#!/usr/bin/env python3

""" 

"""

__author__ = "Hichigo TurkHackTeam"
__license__ = "GPLv3"
__version__ = "1.5.0"
__status__ = "Geliþtiriliyor"

from requests.sessions import Session
from requests import get
from random import choice
from multiprocessing import Process
from colorama import init,Style,Fore

BANNER = """
  dBBBBBBP dBP dBP  dBBBBBBP    dBP dBBBBb.dBBBBP dBBBBBBP dBBBBBb       .dBBBBP dBBBBBb dBBBBBb     dBBBBBBb
                                       dBPBP                    BB       BP          dB'      BB      '   dB'
   dBP   dBBBBBP     dBP      dBP dBP dBP `BBBBb   dBP      dBP BB       `BBBBb  dBBBP'   dBP BB   dB'dB'dB' 
  dBP   dBP dBP     dBP      dBP dBP dBP     dBP  dBP      dBP  BB          dBP dBP      dBP  BB  dB'dB'dB'  
 dBP   dBP dBP     dBP      dBP dBP dBP dBBBBP'  dBP      dBBBBBBB     dBBBBP' dBP      dBBBBBBB dB'dB'dB'   
    Yapýmcý: Hichigo THT
"""

USER_AGENTS = ["Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0",
"Mozilla/5.0 (Android 4.4; Tablet; rv:41.0) Gecko/41.0 Firefox/41.0",
"Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0",
"Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0",
"Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0"]

USER_AGENT = choice(USER_AGENTS)

class Client:
    def __init__(self,username,password,proxy):
        self.ses = Session()
        self.loggedIn = False
        self.username = username
        self.password = password
        self.proxy = proxy
    
    def Login(self):
        if self.loggedIn == True:
            return None
        
        loginData = {
            "password":self.password,
            "username":self.username,
            "queryParams":"{}"
        }
        homePageResponse = self.ses.get("https://www.instagram.com/accounts/login/")
        loginHeaders = {
            "Accept":"*/*",
            "Accept-Encoding":"gzip,deflate,br",
            "Accept-Language":"en-US,en;q=0.5",
            "Connection":"keep-alive",
            "Content-Type":"application/x-www-form-urlencoded",
            "Host":"www.instagram.com",
            "Referer":"https://www.instagram.com/accounts/login/",
            "X-Requested-With":"XMLHttpRequest",
            "X-Instagram-AJAX":"1",
            "User-Agent":USER_AGENT,
            "X-CSRFToken":homePageResponse.cookies.get_dict()["csrftoken"],
        }
        loginCookies = {
            "rur":"PRN",
            "csrftoken":homePageResponse.cookies.get_dict()["csrftoken"],
            "mcd":homePageResponse.cookies.get_dict()["mcd"],
            "mid":homePageResponse.cookies.get_dict()["mid"]
        }
        self.ses.headers.update(loginHeaders)
        self.ses.cookies.update(loginCookies)

        loginPostResponse = self.ses.post("https://www.instagram.com/accounts/login/ajax/",data=loginData)
    
        if loginPostResponse.status_code == 200 and loginPostResponse.json()["authenticated"] == True:
            self.loggedIn = True
            mainPageResponse = self.ses.get("https://www.instagram.com/")
            self.ses.cookies.update(mainPageResponse.cookies)
    
    def Spam(self,username,userid):
        if self.loggedIn == False:
            return None   

        link = "https://www.instagram.com/" + username + "/"
        profileGetResponse = self.ses.get(link)
        self.ses.cookies.update(profileGetResponse.cookies)
        spamHeaders = {
            "Accept":"*/*",
            "Accept-Encoding":"gzip,deflate,br",
            "Accept-Language":"en-US,en;q=0.5",
            "Connection":"keep-alive",
            "Content-Type":"application/x-www-form-urlencoded",
            "DNT":"1",
            "Host":"www.instagram.com",
            "X-Instagram-AJAX":"2",
            "X-Requested-With":"XMLHttpRequest",
            "Referer":link,
            "User-Agent":USER_AGENT,
            "X-CSRFToken":profileGetResponse.cookies.get_dict()["csrftoken"],
        }
        "Hichigo was here THT"
        spamData = {
            "reason_id":"1",
            "source_name":"profile"
        }

        self.ses.headers.update(spamHeaders)

        spamPostResponse = self.ses.post("https://www.instagram.com/users/"+ userid +"/report/",data=spamData)
        if spamPostResponse.status_code == 200 and spamPostResponse.json()["description"] == "Your reports help keep our community free of spam.":
            self.ses.close()
            return True
        else:
            return False

def Success(username,shit):
    print(Fore.GREEN +"[" + username +"]" + Style.RESET_ALL
    + " " + shit)

def Fail(username,shit):
    print(Fore.RED +"[" + username +"]" + Style.RESET_ALL
    + " " + shit)

def Status(shit):
    print(Fore.YELLOW +"[ THT Insta SPAM ]" + Style.RESET_ALL
    + " " + shit)

def DoitAnakin(reportedGuy,reportedGuyID,username,password,proxy):
    try:
        insta = None
        if proxy != None:
            insta = Client(username,password,None)
        else:
            insta = Client(username,password,None)
        insta.Login()
        result = insta.Spam(reportedGuy,reportedGuyID)
        if insta.loggedIn == True and result == True:
            Success(username,"Baþarýyla SPAM atýldý!")
        elif insta.loggedIn == True and result == False:
            Fail(username,"Giriþ baþarýlý ama SPAM atýlmasý baþarýsýz!")
        elif insta.loggedIn == False:
            Fail(username,"Giriþ baþarýsýz!")
    except:
        Fail(username,"Giriþ yapýlýrken hata oluþtu!")

if __name__ == "__main__":
    init()
    userFile = open("kullanicilar.txt","r")

    USERS = []
    for user in userFile.readlines():
        if user.replace("\n","").replace("\r","\n") != "":
            USERS.append(user.replace("\n","").replace("\r","\n"))


    print(Fore.RED + BANNER + Style.RESET_ALL)
    Status(str(len(USERS)) + " Adet Kullanýcý Yüklendi!\n")
    reportedGuy = input(Fore.GREEN + "SPAM'lanacak Kiþinin Kullanýcý Adý: " + Style.RESET_ALL)
    reportedGuyID = input(Fore.GREEN + "SPAM'lanacak Kiþinin User ID'si: " + Style.RESET_ALL)
    print("")
    Status("Saldýrý baþlatýlýyor!\n")

    for user in USERS:
        p = Process(target=DoitAnakin,args=(reportedGuy,reportedGuyID,user.split(" ")[0],user.split(" ")[1],None))
        p.start()
