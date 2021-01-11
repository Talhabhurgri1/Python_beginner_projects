import selenium
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException as nse
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import sys

#open the app!

#Automating the mails in python!

def login(email,password):
    try:
        #bypassing the notifications using chrome options
        chrome_options = webdriver.ChromeOptions() 
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        driver = webdriver.Chrome(options=chrome_options)
        wait = WebDriverWait(driver,60)
        url = 'https://passport.yandex.com/auth/add?from=mail&origin=hostroot_homer_auth_L_com&retpath=https%3A%2F%2Fmail.yandex.com%2F&backpath=https%3A%2F%2Fmail.yandex.com%3Fnoretpath%3D1'
        
        driver.get(url)
        '''
        keys like login and textfields and Their XPATH are given below!

        '''
        #logfield = wait.until(ec.element_to_be_selected(By.XPATH,'')) 
        logfield = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="passp-field-login"]')))

        logfield.send_keys(email)

        logbtn = wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@aria-disabled="false"]'))).click()
        passfield = wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="passp-field-passwd"]')))
        passfield.send_keys(password)
        
        loginbtn = wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@class="Button2 Button2_size_l Button2_view_action Button2_width_max Button2_type_submit"]'))).click()
        time.sleep(10)
        sendingmsgs(wait)
    except nse:

        browser.refresh()
        time.sleep(30)
        login(email,password) 

def sendingmsgs(wait):
    try:
        print('Inside Sending msgs')
        receipt = sys.argv[1]
        discription = sys.argv[2]
        if len(receipt)==0 or len(discription)==0:
            print("You did not provide details")

        com_btn = wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@title="Compose (w, c)"]'))).click()
        if len(sys.argv)>3:
            print('Sorry format is not correct')
            driver.quit()

        receipt_btn = wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@class="composeYabbles"]'))).send_keys(receipt)
        
        discription_btn = wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@class="cke_wysiwyg_div cke_reset cke_enable_context_menu cke_editable cke_editable_themed cke_contents_ltr cke_htmlplaceholder"]'))).send_keys(discription)
        submit = wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@aria-disabled="false"]'))).click()
        time.sleep(10)
    except NoSuchElementException:
        print('No element is found')

email ='Your Email'
password = 'Your password'
login(email,password)

