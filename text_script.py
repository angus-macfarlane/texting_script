# Import necessary libraries
from twilio.rest import Client
import sys
import numpy as np
import pandas as pd

# Find your Account SID and Auth Token at twilio.com/console
# Add your Twilio number, ex. '+15556667777' 
account_sid = 
auth_token = 
twilio_number = 

client = Client(account_sid, auth_token)

# get the file name from the terminal
filename = sys.argv[-1]

# Type in the message you want to send. 
message_body = input("What would you like your message to say: ") 

# convert the csv into a dataframe
df = pd.read_csv(filename)

#print the head of the df to verify it is the correct file
print(df.head())

# ask user for input about which column number to use
num_col = input("Which column has the phone numbers? ")

# Use iloc to get the column with phone numbers and verify
print(df.loc[:,[num_col]])

#identify name column
name_col = input("Which column contains the names? ")
# print(df.loc[:,[name_col]])

# Create a dictionary with name as key and phone number as value. 
test_key = df.at[df.index[0], name_col]
print(test_key)
dictionary = {}
for i in range(len(df[name_col])):
    key = df.at[df.index[i], name_col]
    i_value =str(df.at[df.index[i], num_col])
    value = '+' + i_value
    dictionary[key] = value 
print(dictionary)

# Create a list of just the phone numbers. 
phone_numbers = list(dictionary.values())
names = list(dictionary.keys())
print(phone_numbers[0])

# This loops through the lists and send a message to each number with the name appended to the front. 
for i in range(len(dictionary)):
    message = client.messages \
     	.create(
     		body=names[i] + ", "  + message_body,
     		from_=twilio_number,
     		to=phone_numbers[i])
    print(message.sid)

