# SDP Generator by Jonathan Ferraro
## Small Python Script that will build bulk SDPs for -20, -30, and -40 into one file per signal group. 
NOTE: Might require some modfication to the master.sdp file to get the format of audio and video just right. This current Master branch is set 720p59.94 for video and 125us packet time for audio.

### How to use: 

1: Delete .demo. from the signals csv file name and use it to build names and multicast IP addresses. 
2: Fill in all columns for every row. 
3: Modify the master.sdp file if you need to change the format of Video or Audio. 
3: Create a directory called "SDP_Files", the Python script will dump your new SDP files here. 
