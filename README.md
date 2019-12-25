# reconnect
reconnect to your wifi when your connection drops

only works on windows

~not fully optimized due to the subprocess module is not really quick. i may change it to another module.~

NOT ANYMORE BECAUSE I USE A NEW MODULE FOR THAT. `pip install pythonping` to proceed

right now, there are two methods to do that in the code and I have pythonping as the default. it is simply faster.

**read all the comments to tweak the script**

there is a known issue, if you try to connect to another network while is script is running, there will be dropped packets during the process; and thus, you won't be able to connect back to your network. Right now, turn off the script while using other network or change the name in the script