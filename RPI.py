# PUSHBULLET LISTENER AND WAKE PACKET SENDER
# Get the pushbullet api form "pip install pushbullet.py"
from pushbullet import Pushbullet
from wakeonlan import send_magic_packet
import time
pb = Pushbullet("*******************")

# Forever LOOP
while (1 == 1):
    # To wait sometime before another get. because PB has ratelimit.
    time.sleep(15)
    pushes = pb.get_pushes()
    latest = pushes[0]
    # just turn on
    if(latest["body"] == "turn on"):
        send_magic_packet('YO-UR-MAC-ADD-RESS')
        print("yes")
        # To reset the pushbullet last to different note
        pb.push_note("RPI", "LOL")
        break
    # sign out from attendance
    elif(latest["body"] == "signout from attendance"):
        send_magic_packet('YO-UR-MAC-ADD-RESS')
        print("yes")
        # To reset the pushbullet last to different note
        pb.push_note("RPI", "LOL")
        # waits for the pc to turn on
        time.sleep(150)
        # sends push note which will be viewed by the pc and starts attendance script
        pb.push_note("Desktop", "attendance")
        break
    else:
        print("no")

