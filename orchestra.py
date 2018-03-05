#!/usr/bin/python
'''This module processes PayPal Instant Payment Notification messages (IPNs).
'''
from random import choice
import string
import wrt_db
#import email_sender
import send_html_email
import sys,urlparse,requests,logging,cgi,logging_config

#def GenPasswd2(length=8, chars=string.letters+string.digits):
  #  return ''.join([choice(chars) for i in range(length)])

#Calling my Custom Logging configuration
logging_config.log()
logging.info('')
logging.info('************* NEW IPN LOG *************')

#Assigning the correct URL
VERIFY_URL_PROD = 'https://www.paypal.com/cgi-bin/webscr'
VERIFY_URL_TEST = 'https://ipnpb.sandbox.paypal.com/cgi-bin/webscr'
VERIFY_URL = VERIFY_URL_PROD

# CGI preamble 
logging.info('Sending the Header to Paypal for Status')
print "content-type: text/plain"
print

# Read and parse query string
logging.info('Reading and Parsing Paypal Info - JSON format')
input = cgi.FieldStorage()
fields = {}
for key in input:
   fields[key] = input[key].value
   logging.debug('Adding to the Fields Dictionarie: %s', key)
   
# Add '_notify-validate' parameter
logging.info('Adding _notify-validate to cmd')
fields["cmd"] = "_notify-validate"

# Post back to PayPal for validation
logging.info('Message prepared... Ready to send it to Paypal!')
headers = {'content-type': 'application/x-www-form-urlencoded', 'host': 'www.paypal.com'}
logging.info('Sending POST to Paypal with Required Parameters to verify the IPN id')
r = requests.post(VERIFY_URL, params=fields, headers=headers, verify=True)
logging.info('Checking if IPN Status is Verified and if the Payment has been Completed')
if r.text == 'VERIFIED' and fields["payment_status"] == 'Completed' :
    logging.info('IPN is Verified and Payment is Completed')
    logging.info('Sending email to Customer')
    send_html_email.send_complex_message(**fields)
    logging.info('Writing all the IPN data into the Database')
    wrt_db.writedb(**fields)
    logging.info('DONE..... Writing all the IPN data into the Database')
    pass

elif r.text == 'INVALID':
    logging.info('IPN Invalid Request')
    pass	

else:
    logging.info('Something happened with the Transaction. Please take a look of the Logs.')
    pass	

logging.info('The CGI Script has finished!')

#Proverbios 16:3
