# texting_script
this is a script that gets info from a CSV and then connects to the Twilio API to send texts. 

When you run the script, include the csv file. Ex. 'python3 texting_script.py csv_file.csv'
The script will ask you to type out the message you want to send (it will pre-pend a name when it is sent).
Select the column with the phone numbers, they should be formatted '1236780092', the script will add the '+'.
Select the column with the name, this is what will be added to the beginning of the message. 
