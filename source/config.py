import webbrowser
import requests
import os,sys,time
from time import sleep
from os import path
from os import system

AUTHOR = "Anas Y.Bal"
PROGRAM_NAME = "SMTP-Checker"

def social(so):
    if so == "fb":
        webbrowser.open_new("https://www.facebook.com/anasybal.ly/")
    elif so == "gh":
        webbrowser.open_new("https://github.com/anasybal")
    elif so == "tg":
        webbrowser.open_new("https://t.me/anasybal")
        
def check(mail):
    url = "https://validateemailaddress.org/"
    payload="email="+mail.replace("@","%40")
    headers = {
        'User-Agent': 'Mozilla/5.0 ',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '26',
        'Origin': 'https://validateemailaddress.org',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://validateemailaddress.org/',
        'Upgrade-Insecure-Requests': '1',
        'Sec-GPC': '1'
    }
    response = requests.post(url, headers=headers, data=payload)
    return response.text

def file_put_contents(fn,data):
    ck = path.isfile(fn)
    if ck == True or ck == 1:
        do=open(fn,'w')
        do.write(data)
    else:
        do=open(fn,'x')
        do.write(data) 
    sleep(0.4)
    final = path.isfile(fn)
    if final == True or ck == 1:
        return True
    else:
        return False

def file_input_contents(fn,data):
    ck = path.isfile(fn)
    if ck == True or ck == 1:
        li = open(fn, "r").read()
        if li == '':
            return False
        else:
            file_put_contents(fn,li+data)
            sleep(0.4)
            final = path.isfile(fn)
            if final == True or ck == 1:
                return True
            else:
                return False
    else:
        return False

def file_get_contents(fn):
    ck = path.isfile(fn)
    if ck == True or ck == 1:
        li = open(fn, "r").read()
        if li == '':
            return None
        else:
            return li
    else:
        return False