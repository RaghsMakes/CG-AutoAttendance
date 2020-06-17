# CG-AutoAttendance

Needed items:
  a device to push "signout from attendance" in my case that's my google home,
    Raspberry PI (any versions) in my case 3b+.
  a wifi router ur pc and rpi to connected it the same network. 
    (If you dont have that u could port forward and have a static ip or use noip).
  
  a pc

Prequstics:

Install Pushbullet,wakeonlan using
  pip install pushbullet.py
  pip install wakeonlan
Turn on wake on lan in your pc

Add RPI script to cron on it. So, that it could start automatically and run in background.

REMEMBER: pushbullet has ratelimit. So, continuous get and post may stop it working.
          But dont worry. It will start working again in nearly an hour.
          
  HAVE FUN!
