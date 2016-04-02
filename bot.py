import webbrowser
import time
import os

print "BY TURTAPPS"
print "Subscribe to 'open coder' in youtube"
print "GO TO Turtapps.com"

url = raw_input("URL>")
refresh = 10
brow = raw_input("browser>")
views = int(raw_input("view>"))


def bot():
	os.system(" killall -9 " + brow)
	webbrowser.open(url)
	time.sleep(refresh)

for i in range(views):
	bot()
