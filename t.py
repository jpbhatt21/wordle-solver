import random
import pyautogui
import time
import sys
import io
import copy
import os
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from googleapiclient.discovery import build
from google.oauth2 import service_account
import webbrowser
from os import system,name
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
# from tkinter import *
#
# #Create an instance of tkinter frame
# win= Tk()
# print(win.winfo_screenwidth(),win.winfo_screenheight())
url = "https://wordlegame.org/"
webbrowser.open(url)
time.sleep(1)
SCOPES=["https://www.googleapis.com/auth/drive"]
PID='1pIfWJwIf0FK6kPdTbce6yr6XluQfxtdV'
TID='1ApIHD1J1CSS_I7E8R9uulDWRn6q5K8mU'
TName='Track.txt'
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
SFile=resource_path("sa.json")
try:
    os.remove(resource_path(os.path.join("Track.txt")))
except:
    pass
def auth():
    creds=service_account.Credentials.from_service_account_file(SFile , scopes=SCOPES)
    return creds
creds=auth()
service= build('drive','v3',credentials=creds)
def upload(path,name):

    meta={
        'name':name,
        'parents': [PID]
    }
    file= service.files().create(
        body=meta,
        media_body=path
    ).execute()
def update(fileid,content):
    if fileid==TID:
        content=MediaFileUpload("Track.txt",mimetype='text/plain')
    service.files().update(
        fileId=fileid
        ,media_body=content
    ).execute()

def download(fileid,savename):
    if fileid==TID:
        savename=TName
    request=service.files().get_media(fileId=fileid)
    fh=io.BytesIO()
    downloader= MediaIoBaseDownload(fd=fh,request=request)
    done =False
    while not done:
        done=downloader.next_chunk()
    fh.seek(0)
    with open (resource_path(os.path.join(savename)),'wb') as f:
        f.write(fh.read())
        f.close()
download(TID,None)
t=resource_path('wd.png')
t2=resource_path('wd2.png')
# t=(os.path.join(os.getcwd(),'wd.png'))
# t2=(os.path.join(os.getcwd(),'wd2.png'))
lost=resource_path(os.path.join('lost.png'))
real=False
import json
if real:
    with open('real.json','r') as fp:
        data2=json.load(fp)
else:
    with open('best.json','r') as fp:
        data2=json.load(fp)
data=copy.deepcopy(data2)
tb=[0,0,0,0,0]
tba=[0,0,0,0,0]
bw=100
icx=[]
word=''
ft=0
pos='00000'
turns=1
def track():

    try:
        bu = pyautogui.locateOnScreen(lost,confidence=0.8)
        file = open(resource_path('Track.txt'),"r")
        l=(file.read().strip()).split("\n")
        file.close()
        file= open(resource_path('Track.txt'),"w")
        l[1]=str(int(l[1])+1)
        im=pyautogui.screenshot(resource_path(os.path.join("Lost"+l[1]+".png")))
        upload(resource_path(os.path.join("Lost"+l[1]+".png")),"Lost"+l[1])
        for i in l:
            file.write(i+"\n")
        file.close()
        update(TID,None)
        os.remove(resource_path(os.path.join("Lost"+l[1]+".png")))

    except:
        file = open(resource_path('Track.txt'),"r")
        l=(file.read().strip()).split("\n")
        file.close()
        file= open(resource_path('Track.txt'),"w")
        if(len(l)<3):
            l=["0","0","0"]
        l[0]=str(int(l[0])+1)
        l[2]=str(int(l[2])+turns)
        for i in l:
            file.write(i+"\n")
        file.close()
        update(TID,None)


def second():
    global word,pos,ft,data,turns
    Pos = str(pos)
    incl=''
    inclPos=''
    exclude=''
    for i in range(5):
        if(Pos[i]==str(0)):
            exclude+=word[i]
        elif(Pos[i]==str(1)):
            incl+=word[i]
            inclPos+=str(-(i+1))+" "
        elif(Pos[i]==str(2)):
            incl+=word[i]
            inclPos+=str((i+1))+" "

    inclPos=inclPos.split(' ')

    c=0
    for i in incl:
        pos=int(inclPos[c])
        for j in list(data):
            if (pos>=0 and not (j[pos-1]==i)):
                data.pop(j)
            elif (pos<0 and (j.find(i)==abs(pos+1) or j.find(i)== -1 )):
                data.pop(j)
        c+=1

    for i in exclude:
        for j in list(data):
            if not (j.find(i)==-1):
                if ((incl.find(i)==-1)):
                    data.pop(j)
                elif(j.count(i)!=incl.count(i)):
                    data.pop(j)

    l=list(data.values())
    if(len(l)==0):
        return
    else:
        c=5
        while(c<16):
            try:
                key=list(data.keys())[l.index(c)]
                break
            except:
                pass
            c+=2

    if(ft==0):
        word='sloth'
        ft+=1
    else:
        word=key

    time.sleep(.5)
    pyautogui.typewrite(word,interval=0.1)
    time.sleep(.5)
    pyautogui.press("enter")
    time.sleep(.5)
    turns+=1
    print("\n\n-New-")
    for i in data.keys():
        print(i)
    
def main():
    time.sleep(.5)
    pyautogui.typewrite('crane',interval=0.1)
    time.sleep(.5)
    pyautogui.press("enter")
    time.sleep(.5)

    run=True
    global w,word,pos,tb,tba,bw,icx,word,ft,pos,data
    data=copy.deepcopy(data2)
    tb=[0,0,0,0,0]
    tba=[0,0,0,0,0]
    bw=100
    icx=[]
    word=''
    ft=0
    pos='00000'
    x=0
    first_word=1
    base=(25,26,36)
    Name_Editor=['c','r','a','n','e']
    ind=5
    ic=['0','0','0','0','0']
    color=[(25,26,36),(25,26,36),(25,26,36),(25,26,36),(25,26,36)]
    time.sleep(1)
    bu = pyautogui.locateOnScreen(t)
    ix=pyautogui.screenshot()
    c=[]

    for j in range(5):
        c.append(ix.getpixel((bu[0]+20+(bu[3])*j, bu[1]-45)))
        if(c[j]==(243, 194, 55)):
            ic[j]='1'
        elif(c[j]==(121, 184, 81)):
            ic[j]='2'
        else:
            ic[j]='0'

    while(run):

        all2=True
        for i in range(5):
            if ic[i]=='0':
                all2=False
                color[i]=(25,26,36)
            elif ic[i]=='1':
                all2=False
                color[i]=(253,194,55)
            elif ic[i]=='2':
                color[i]=(121, 184, 81)
        if all2 or len(list(data.keys()))==0:
            time.sleep(1)
            bu = pyautogui.locateOnScreen(t2,confidence=0.8)
            ml=pyautogui.position()
            pyautogui.moveTo(bu[0]+10, bu[1]+10,0.5)
            track()
            pyautogui.click()
            pyautogui.moveTo(ml)
            return(True)
        first_word+=1
        word=Name_Editor[0]+Name_Editor[1]+Name_Editor[2]+Name_Editor[3]+Name_Editor[4]
        pos=ic[0]+ic[1]+ic[2]+ic[3]+ic[4]
        second()
        time.sleep(0.2)
        for p in range(5):
            Name_Editor[p]=word[p]
            if(first_word==2):
                icx.append(ic[p])
            if(first_word==3 and icx[p]=='2'):
                ic[p]='2'
            elif (ic[p]=='1') or first_word==2:
                ic[p]='0'
        time.sleep(1)
        try:
            bu = pyautogui.locateOnScreen(t)
        except:
            time.sleep(1)
            bu = pyautogui.locateOnScreen(t2,confidence=0.8)
            ml=pyautogui.position()
            pyautogui.moveTo(bu[0]+10, bu[1]+10,0.2)
            track()
            pyautogui.click()
            pyautogui.moveTo(ml[0],ml[1],0.2)
            
            return(True)


        ix=pyautogui.screenshot()
        c=[]
        for j in range(5):
            c.append(ix.getpixel((bu[0]+20+(bu[3])*j, bu[1]-45)))
            if(c[j]==(243, 194, 55)):
                ic[j]='1'
            elif(c[j]==(121, 184, 81)):
                ic[j]='2'
            else:
                ic[j]='0'

#pyautogui.hotkey('alt','tab')
try:
    while(main()):
        turns=1
except:
    os.remove(resource_path(os.path.join("Track.txt")))