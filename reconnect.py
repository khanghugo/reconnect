import time
import subprocess
import winsound
from pythonping import ping

# these are the settings that you can tweak for yourself
networkName = 'yourNetwork'
domainName = '1.1.1.1' # test with your ping to see which domain gives you the fastest response
pingCount = 2 # thid is the pyping method, unless 100% packet loss or spike in response time, it will reconnect
timeOut = 0.5 # this is in second, reminder: 1s = 1000ms
reconnectTime = 1
ignoreTime = 0.5

# you can play the lick if you reconnect, no kidding
winBeep = [440, 250]
errorMessage = ['General failure', 'Destination host unreachable', 'Request timed out'] # this may not needed because pythonping method doesn't need to check errors


# gimmick finding your network name
showinterfacesCommand = 'netsh wlan show interfaces'.split()
resultNetworkName = str(subprocess.Popen(showinterfacesCommand,stdout=subprocess.PIPE).communicate())

def findNetworkName():
	# I have to cut the list due to ""MATCHES"" in the ketwords. There are two connection types which are Auto Connect (when you tick auto connect in the browsing menu) and Profile (when you don't). So when we try to search for the profile of our network, there should come two results. Therefore, I cut it to get the right one. Alternatively, I can just use the second output but I think is is good enough
	processed = resultNetworkName.split()[-20:]

	for m in processed:
		if "Profile" in m:
			# this is simply trial-and-error. In the output, there are a lot of indentations and new line so skipping output can get us the result.
			return processed[processed.index(m)+2]

# if the networkName is default (yourNetwork) then the finding network name will be called and it will get your network name for the variable for other functions to call from. This is called once so there no need to worry a lot.
if networkName == "yourNetwork" or not networkName:
	networkName = findNetworkName()

disconnectCommand = 'netsh wlan disconnect'.split()
reconnectCommand = f'netsh wlan connect name="{networkName}"'.split() # the variable is still the final one or the one is defined from the very beginning

# just a quick head-up
print("Script started")

# this is the pythonping method, faster because it is a dedicated module just for pinging while subprocess was made for multi-purposes
while True:
	try:
		# this is the pythonping module
		result = str(ping(domainName, count=pingCount, timeout=timeOut))

		#because of how output of this module is entirely different, we can use that to flip the checking mechanism. in short, there will not be any packet loss countinh
		if domainName in result:
			# sleep has to be reasonable enough so the reconnect request won't spam
			time.sleep(ignoreTime)
			continue

		else:
			# the reason why I came across the subprocess method was to hide the command prompt so it will not disturb you. Despite being slow, I think it is fast enough to connect back
			subprocess.Popen(disconnectCommand)
			subprocess.Popen(reconnectCommand)

			winsound.Beep(winBeep[0], winBeep[1])

			# if this is set too fast, it will become a loop.
			time.sleep(reconnectTime)
			print('Running...')
			continue

	except Exception as e:
		# print(e) # I don't understand how it doesn't write down the error before so I need this
		print("Script stopped")
		break
