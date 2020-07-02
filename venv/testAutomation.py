from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib3
import re
from selenium.webdriver.common.keys import Keys
import urllib.request
from validate_email import validate_email
import requests
import chardet
def main():
    driver = webdriver.Chrome("C:\\Users\\iovadiax\\Desktop\\itzik\\TASK\\chromedriver\\chromedriver.exe")
    driver.get("https://automation.herolo.co.il/")
    submit_button=driver.find_element_by_xpath('//*[@id="section-inputs"]/*/a')
    user = {
        'name': ['name1', '2323'],
        'company': ['454545'],
        'email': ['test@','@test','test','.co','test@co','2323'],
        'telephone': ['phone1','012345678','012345678a']
    }
    for key,value in user.items():
        checkingOneValueForm(driver,key,value,submit_button)
    for name in user['name']:
        for company, mail, phone in zip(user['company'], user['email'], user['telephone']):
            checkingAllValuesForm(driver, name, company, mail, phone)
    for company in user['company']:
        for name, mail, phone in zip(user['name'], user['email'], user['telephone']):
            checkingAllValuesForm(driver, name, company, mail, phone)
    for mail in user['email']:
        for name, company, phone in zip(user['name'], user['company'], user['telephone']):
            checkingAllValuesForm(driver, name, company, mail, phone)
    for phone in user['telephone']:
        for name,company, mail in zip(user['name'], user['company'],user['email']):
            checkingAllValuesForm(driver, name, company, mail, phone)
    checkingLink(driver)
def checkingLink(driver):
    link_status = dict()
    url_list = driver.find_elements_by_xpath("//a[@href]")
    for url in url_list:
        url = url.get_attribute('href')
        if 'http' in url:
            status = requests.head(url)
            link_status[url] = status.status_code
        if '@' in url:
            match = re.findall(r'\w+@\w+.*',url)
            mail_valid = validate_email(email_address=match[0], check_regex=True,check_mx=False)
def checkingAllValuesForm(driver,name,company,mail,phone):
    driver.find_element_by_id('name').send_keys(Keys.CONTROL + "a")
    driver.find_element_by_id('name').send_keys(Keys.DELETE)
    driver.find_element_by_id('company').send_keys(Keys.CONTROL + "a")
    driver.find_element_by_id('company').send_keys(Keys.DELETE)
    driver.find_element_by_id('email').send_keys(Keys.CONTROL + "a")
    driver.find_element_by_id('email').send_keys(Keys.DELETE)
    driver.find_element_by_id('telephone').send_keys(Keys.CONTROL + "a")
    driver.find_element_by_id('telephone').send_keys(Keys.DELETE)
    driver.find_element_by_id('name').send_keys(name)
    driver.find_element_by_id('company').send_keys(company)
    driver.find_element_by_id('email').send_keys(mail)
    driver.find_element_by_id('telephone').send_keys(phone)
    clik = driver.find_element_by_xpath('//*[@id="section-inputs"]/*/a')
    clik.click()
def checkingOneValueForm(driver, element,values,submit_button):
    for value in values:
        driver.find_element_by_id(element).send_keys(Keys.CONTROL + "a")
        driver.find_element_by_id(element).send_keys(Keys.DELETE)
        driver.find_element_by_id(element).send_keys(value)
        submit_button.click()


if __name__ == "__main__":
    main()