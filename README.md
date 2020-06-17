# CG-AutoAttendance

Needed items:
  a Device to push "signout from attendance" in my case that's my google home.
 
  A Raspberry PI (any versions) in my case 3b+.
    
  A WiFi Router, your PC and RPI should be connected to the same network. 
  
    (If you dont have that u could port forward and have a static ip or use NOIP).
  
  A PC

Prequstics:

Install Pushbullet,wakeonlan using
  "pip install pushbullet.py"
  "pip install wakeonlan"
"Turn on wake on lan in your pc"

Add RPI script to cron on it. So, that it could start automatically and run in background.

REMEMBER: pushbullet has ratelimit. So, continuous get and post may stop it working.
          But dont worry. It will start working again in nearly an hour.
          If you have any doubts or issues definitly there will be a indian video on youtube follow it. ;P
          
                                              HAVE FUN!
