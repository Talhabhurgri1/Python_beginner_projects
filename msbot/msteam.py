#importing modules
import selenium
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import datetime
import os
import schedule

def exitbot():
    driver.quit()

''' method to get email and password from the text file '''
def details():
    email = ''
    password =''
    files = open('attendence.txt','r')
    for i in files:
        piece = i.strip(':')
        email = piece[0:i.index(':')]
        password = piece[i.index(':')+1:len(i)-1]
    login(email,password)
    ''' log-in for login to the ms teams!'''

def login(email,password):
    
    time.sleep(2)

    emailsite = driver.find_element_by_xpath('//*[@id="i0116"]')
    emailsite.send_keys(email)
    time.sleep(2)

    nextsite = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
    nextsite.click()
    time.sleep(7)
    
    passwords  = driver.find_element_by_xpath('//*[@id="i0118"]')
    passwords.send_keys(password)
    time.sleep(2)

    signin = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
    signin.click()

    time.sleep(6)
    
    notification = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
    if notification.is_enabled(): # returns true if it is enabled otherwise it will fail
        notification.click()
        time.sleep(7)

    webapp = driver.find_element_by_xpath('//*[@id="download-desktop-page"]/div/a')
    if webapp.is_enabled():
        webapp.click()
        time.sleep(10)
    
    datafromfile() #CALLING FUNCTION

def datafromfile(): #GETTING DATA
    details = {}
    with open(datetime.datetime.today().strftime('%A')+'.txt') as file:
        for line in file:
            key,value = line.split()        
            details[key] = value
    
    list1 =list(details.values())
    return list1
    #joinclass(list1)
    #details()
'''Join Class Method'''

def joinclass(class_name):


    try:

        time.sleep(10)
        print('joined')
        notificationdismiss = driver.find_element_by_xpath('//*[@title="Dismiss"]').click()                
        time.sleep(5)
                
        joinchannel =driver.find_element_by_xpath(f'//*[@title="{class_name}"]')
        joinchannel.click()
        print(f'{class_name}')
        
    except:
        print('Could not find {class_name} Please edit your file')
        time.sleep(10)
        
            #join button 
    time.sleep(5)
    joinclass =driver.find_element_by_xpath('//*[@aria-label="Join"]')    
    if joinclass.is_displayed():

        joinclass.click()
        time.sleep(5)
    
    else:
        print('Class is already finished')
    time.sleep(5)

    mute = driver.find_element_by_xpath('//*[@title="Mute microphone"]').click()
    cameraoff = driver.find_element_by_xpath('//*[@title="Turn camera off"]')

    if cameraoff.is_displayed():
        cameraoff = driver.find_element_by_xpath('//*[@title="Turn camera off"]').click()
        time.sleep(4)
    
    time.sleep(5)

    time.sleep(6)
        
    joinbutton = driver.find_element_by_xpath('//*[@aria-label="Join the meeting"]')

    if joinbutton.is_displayed():
        joinbutton.click()
        time.sleep(15)
    
'''End Class Method'''

def endclass(class_name):
    # End call button
    try:
        elem = driver.find_element_by_id('hangup-button')
        driver.execute_script("$(arguments[0]).click();", elem)

        print(f"{sub_name} ended")
        time.sleep(3)
        try:
            elem = driver.find_element_by_xpath('//*[@aria-label="Dismiss"]').click()
        except:
            pass
    except NoSuchElementException:
        print("Class already ended or didn't start")
        pass
    except:
        print("Class already ended or didn't start")

#ALLOWING MICRPHONE ON CHROME 

#final run
options = Options()
options.add_argument("--use-fake-ui-for-media-stream")
        # open chrome
driver = webdriver.Chrome(options=options)
        # Maximize window
driver.maximize_window()

url='https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=43c754b6-9f90-4193-90e7-e8e1de941569&&client-request-id=46c13c81-5edd-4fa0-acff-23c5c66c3809&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=bd64269d-c0b8-413e-bcfc-077b2517e3cd&domain_hint='
driver.get(url)
details()


list2 = datafromfile()
time.sleep(10)
#SCHEDULED TASKS
i=0
while i < len(list2):
    schedule.every().day.at(f"{list2[i+1]}").do(joinclass,f"{list2[i]}")
    schedule.every().day.at(f"{list2[i+2]}").do(endclass,f"{list2[i]}")

    print('Scheduled')    
    if i==len(list2)-3:  
        schedule.every().day.at(f"{list2[i+2]}").do(exitbot)    
    i=i+3

while True:
    schedule.run_pending()
    time.sleep(1)    
