import datetime
import sys
sys.path.append('../pythonstuff/')
import sendmail

def findLastMinute():
    printline=''
    today = datetime.date.today()
    lastminute = datetime.datetime.now() - datetime.timedelta(minutes=1)
    lastminute = lastminute.strftime('%H:%M')

    dag = today.strftime("%d").lstrip('0')
    maned = today.strftime("%b")
    logfile_open = f"/var/log/auth.log"
    logfile=open(logfile_open).read().splitlines()
    dateinlogfile=f"{maned}  {dag} {lastminute}"    
    dateinlogfile2=f"{maned} {dag} {lastminute}"
    
    for index, line in enumerate(logfile):
        if dateinlogfile in line or dateinlogfile2 in line:
            if  "Accepted" in line and not "192.168." in line and not "127.0.0." in line:
                 printline +=line+"\n"
    print (printline)

#| /bin/grep "Accepted" | /bin/grep "$DATE" | grep -v "192.168.1." | grep -v "127.0.0.1"

    if printline !="" and printline is not None and printline is not "":
        message = f"""\
Subject: Du (forhapentligvis) har logget pa via SSH

{printline}

"""
        mailout= sendmail.Sendmail ("email@youemail.com", "yourpasswordXXXX", "your.smtpserver.com", "587")
        mailout.sendMail("email@youremail.com", "email@youremail.com", message)
    else:
        print ("Ingen nye pålogginger")



findLastMinute()
