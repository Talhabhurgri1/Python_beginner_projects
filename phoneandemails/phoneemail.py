import pyperclip
import re 
text = pyperclip.paste()
#Regex to find Phone and mail pattern 
phone_regex =r"[0]+\d{3}[-]?\d{7}" #only pakistan pattern
email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}" #global mail patterns(Standard)Pattern
#compiling phone patterns

phone_pattern =re.compile(phone_regex)
email_pattern=re.compile(email_regex,re.VERBOSE)

#searching 

search_email=email_pattern.findall(text)
search_phone = phone_pattern.findall(text)
#copying results into the clipboard

pyperclip.copy(str(search_email))
pyperclip.copy(str(search_phone))

#last Step= Printing the results(phone and mail separately.)
if len(search_email) >  0 :
    print('Result copied to clip board')
    print(search_email)
else:
    print('No result copied')