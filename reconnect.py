import time
import subprocess
import winsound

networkName = 'yourNetwork'
winBeep = [440, 250]
domainName = '1.1.1.1'
errorMessage = ['General failure', 'Destination host unreachable', 'Request timed out']
pingCount = "3"
timeOut = "50"

pingCommand = f"ping {domainName} -n {pingCount} -w {timeOut}".split()
disconnectCommand = 'netsh wlan disconnect'.split()
reconnectCommand = f'netsh wlan connect name="{networkName}"'.split()


print("Script started")

while True:
	try:
		result = str(subprocess.Popen(pingCommand,stdout=subprocess.PIPE).communicate())
		print(result)
		for m in errorMessage:

			count = result.count(m)

			if count == int(pingCount):
				subprocess.call(disconnectCommand)
				subprocess.call(reconnectCommand)

				winsound.Beep(winBeep[0], winBeep[1])

				print("Reconnecting...")

				time.sleep(0.5)

				continue

			elif count < int(pingCount):
				time.sleep(0.5)

				continue

	except Exception as e:
		print(e)

		break



