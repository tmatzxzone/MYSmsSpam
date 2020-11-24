import requests, os , time

os.system('clear')
c=('\033[1;36m')
r=('\033[1;31m')
g=('\033[1;32m')
w=('\033[1;37m')
print("""%s
             SPAM SMS 68886%s
 ,_     _‚
 |\\\___//|    %sAuthor: TmatzXzonE%s
 |=6   6=|    %sContact: 999%s
 \=._Y_.=/    %sGithub: github.com/tmatzxzone%s
  )  `  (    ,    %sUse Wisely%s
 /       \  ((
 |       |   ))
/| |   | |\_//    %sSPECIAL THANKS TO: API Owner%s
\| |._.| |/-`
 '"'   '"'
"""%(c,r,g,r,g,r,g,r,g,r,w,r))

i=int(0)

no=input("%sMasukan No Target => %s"%(g,w))
msg=input("%sMasukan Mesej => %s"%(g,w))
brpe=input("%sBrpe kali nk spam bang? => %s"%(g,w))
while True:

    idk=('1:')
    r=requests.get('http://broadcast.smsgateway.cc/API/ReceiveSMS.aspx?Username=mikeiso@hotmail.com&password=mikeiso@2020&MobileNumber='+no+'&ContentType=1&MsgText='+msg+'')
    
    if str(idk) in str(r.text):
        print("[+] Success Bang mantap jiwa")
    else:
        print("[-] GAGAL")
        print("%s[!] Account dh limit ni!! "%(r))
        break
    i+=1

    time.sleep(5.0)
    if i == int(brpe):
        print("%s[!] Done !:)"%(r))
        break


