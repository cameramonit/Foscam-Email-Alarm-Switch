import urllib2,sys
#if you have multiple Foscams on different ports, just enter them in this list.
#Of course, this is assuming you've assigned different ports for each Foscam.
myports = ["port1","port2","port3"]

username = sys.argv[1]
password = sys.argv[2]
mailsetting = sys.argv[3]

#your Foscam's IP address
url_base = "http://127.0.0.1"
url_action = "/set_alarm.cgi?user=" + username + "&pwd=" + password + "&mail="

#1 being ON, 2 being OFF
mailon = "1"
mailoff = "0"

def setalarm(onoroff):
    for port in myports:
        fullurl = url_base + port + url_action + onoroff
        #print fullurl
        f = urllib2.urlopen(fullurl)

#the CLI command you need to enter will be something along the lines of:
#"python setalarm.py USERNAME PASSWORD 1" to turn on your Foscam IP Cam or
#"python setalarm.py USERNAME PASSWORD 0" to turn off your Foscam IP Cam.
setalarm(mailsetting)
