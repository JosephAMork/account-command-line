
# this tool for create account on twitter or any web page 
# we will manage account from command line not GUI
#this simple example


import requests,urllib,urllib2
# next step we will update this script to store all values in parser for dynamic thing 
IP_USERNAME='signup-user-name'    # depend on input name
ID_EMAIL='signup-user-email'
ID_PASSWORD='signup-user-password'
USERNAME='your_username'
EMAIL='you@email.com'
PASSWORD='your_Password'
SIGNUP_URL='https://twitter.com/account/create'

def submit_form():
	payload={ID_USERNAME : USERNAME,ID_EMAIL : EMAIL,ID_PASSWORD : PASSWORD,}
	""" we will try to create account with two method GET and POST  to make sure our account will create  """
	# try with  Get Request
	resp=requests.get(SIGNUP_URL)
	print("Response to Get Request: %s " %resp.content)
	
	# second try with POST method
	resp=requests.post(SIGNUP_URL,payload)
	print("headers from post request : %s " %resp.headers)
	
	print ("html response:%s " %resp.read())
	
if __name__=="__main__":
	submit_form()
