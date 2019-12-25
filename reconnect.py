import time
import subprocess
import winsound

# these are the settings that you can tweak for yourself
networkName = 'yourNetwork'
domainName = '1.1.1.1' # test with your ping to see which domain gives you the fastest response
pingCount = "3" # in case of loss packet, upping this number maybe good
timeOut = "50" # this depends on the consistency of your internet, 100 maybe too high. again, using another module can make things faster

# you can play the lick if you reconnect, no kidding
winBeep = [440, 250]
errorMessage = ['General failure', 'Destination host unreachable', 'Request timed out']

# some pre-defined commands to run later with subprocess module
pingCommand = f"ping {domainName} -n {pingCount} -w {timeOut}".split()
disconnectCommand = 'netsh wlan disconnect'.split()
reconnectCommand = f'netsh wlan connect name="{networkName}"'.split()

# just a quick head-up
print("Script started")

# script run definitely
while True:
	try:
		# this function starts to ping and "communicate" to pipe an output for calling later
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
				time.sleep(0.5)
				print("Running...")
				continue
			# as mentioned, unless there is 100% packet loss, it wont reconnect
			elif count < int(pingCount):
				time.sleep(0.5)

				continue

	except Exception as e:
		print(e)

		break



