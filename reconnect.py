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

#both of these values are for the subprocess method
#pingCount = "3" # in case of loss packet, upping this number maybe good
#timeOut = "50" # this was in milisecond. this depends on the consistency of your internet, 100 maybe too high. again, using another module can make things faster


# you can play the lick if you reconnect, no kidding
winBeep = [440, 250]
errorMessage = ['General failure', 'Destination host unreachable', 'Request timed out'] # this may not needed because pythonping method doesn't need to check errors

# some pre-defined commands to run later with subprocess module
# pingCommand = f"ping {domainName} -n {pingCount} -w {timeOut}".split() # this is for subprocess method
disconnectCommand = 'netsh wlan disconnect'.split()
reconnectCommand = f'netsh wlan connect name="{networkName}"'.split()

# just a quick head-up
print("Script started")

# script run definitely
# if you run with subprocess method then just remove the comments
'''
while True:
	try:
		# this function starts to ping and "communicate" to pipe an output for calling later. this doesn't require any extra module. If i try to use os module, command prompt will pop ups
		result = str(subprocess.Popen(pingCommand,stdout=subprocess.PIPE).communicate())
		# print(result)

		for m in errorMessage:

			#while I was writing this, I thought about packet loss so I made this small mechanism to avoid it
			count = result.count(m)

			# in short, if all the packet fails, it guarantee a reconnect, while <100% will be ignored
			if count == int(pingCount):
				subprocess.call(disconnectCommand)
				subprocess.call(reconnectCommand)
				print("Reconnecting...")

				# just a head up
				winsound.Beep(winBeep[0], winBeep[1])
				
				# these sleep to prevent running to fast, but the module itself is slow anyway
				time.sleep(reconnectTime)
				print("Running...")
				continue
			# as mentioned, unless there is 100% packet loss, it wont reconnect
			elif count < int(pingCount):
				time.sleep(ignoreTime)

				continue

	except Exception as e:
		#print(e)
		print("Script stopped")
		break
'''

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
			subprocess.call(disconnectCommand)
			subprocess.call(reconnectCommand)

			winsound.Beep(winBeep[0], winBeep[1])

			# if this is set too fast, it will become a loop.
			time.sleep(reconnectTime)
			print('Running...')
			continue

	except Exception as e:
		# print(e) # I don't understand how it doesn't write down the error before so I need this
		print("Script stopped")
		break
