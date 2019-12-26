# reconnect

**THIS CAN DO**

Reconnect to your wifi when your connection drops

**HOW TO USE**

Right now, it only works on Windows due to the differences of network driver.

In order to run the script, open Command Prompt and `pip install pythonping`

It is expected to run out of the box, you can do some modifications if you want because I leave lots of comments for you to read

**KNOWN ISSUES**

When the script is running, if you connect to another network, you won't be able to do so because that makes the connection drops for a brief moment, which triggers a reconnect to the (previous) network

`pythonping` method is dedicated to ping domains, I have tried to use more organic methods like `subprocess` but it is simply too slow. Maybe I will develop one for my own in the future

Notice how I rhymes these headings