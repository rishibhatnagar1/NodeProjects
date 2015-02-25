import requests
import time
import json

''' The following code will be used to send a picture '''
url_image = 'http://localhost:3000/pagemulti'
url_command ='http://localhost:3000/command'
url_ack = 'http://localhost:3000/ack'
####################################### Image Posting #######################################################
def fileName (cur_name,post_name):
	files ={post_name:open(cur_name,'rb')}
	r = requests.post(url_image,files=files)
	if (r.status_code) ==200:
		print "Posted"
	else:
		print r.status_code

#val = raw_input("Enter the current value of the file with the extension: ")
#val1 = raw_input ("Please enter the filename you want to keep after posting: ")
#fileName(val,val1)
####################################### Command Execution ###################################################
''' Next steps is to send an acknowledgement of an activity that has been completed. For the same, I written a server that does that same. 
    When you receive an input from the mobile app/any other source, you have to send an acknowledgement sayin that the command has been executed. To do that we will post a "success" , if not, we will send a "failed" .
    The server, when it receives "success" is going to return 1, else return 0, if you send something else, it is going to return 00 '''

''' Check the link from server if a command has been sent to it, it will be available at localhost:3000/command '''
#get request for receiving the command
def checkCommand():
    r = requests.get(url_command)
    curValue = r.text
    if curValue != "none":
        if "open" in curValue:
        #Open the door
            print "Opening the door"
            ackPost("success")
        #Send the acknowledgement for the same
        elif "close" in curValue and "door" in curValue:
        #Close the door
            print "Closing the door"
            #Send the acknowlegment for the same
            ackPost("failed")

#############################################Send Acknowledgement #############################################
def postRequest(inp):
    headers = {'content-type': 'application/json'} #All provided in the documentation
    r = requests.post(url_ack,data=json.dumps(inp),headers = headers) #All this code has been put on http:// #docs.python-requests.org/en/latest/user/quickstart/#make-a-request
    print (r.text)
    r = requests.get(url_ack)
    r.status_code
    #print curValue
    if (r.status_code==200):
        print "Posted ", r.status_code
    else:
        print "Error Response Code",r.status_code
#You can modify this command based on the type of your use.
def ackPost(cmd):
           postRequest({"value":cmd})


while True:
    checkCommand()