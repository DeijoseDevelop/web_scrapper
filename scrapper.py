# selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import errno


variable = input('¿Que vas a investigar? >> ')
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get('http://www.google.com')
driver.find_element(By.TAG_NAME, 'input').send_keys(variable + Keys.ENTER)

ALL_RSO = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.ID, "rso")))


def validate_links(link):
    """
    this function is in charge of making the validations to filter the links.
    """
    if link.text != '' and not 'google' in str(link.get_attribute('href')):
        return True

def save_links():
    """
    this function is in charge
    of searching all the a tags inside all the divs with id 'rso'
    and save all the filtered href attributes inside a list
    and return the list.
    """
    data = []
    links = ''
    for i in ALL_RSO:
        links = i.find_elements(By.TAG_NAME, 'a')
        data = [j.get_attribute('href') for j in links if validate_links(j)]
    return data


def validate_tags_for_div(one, two):
    """
    validate the tags
    """
    if one:
        return one
    elif two:
        return two

def validate_tags_for_main():
    """
    this function is in charge of validating the tags
    """
    content = driver.find_element(By.TAG_NAME, 'main').text
    return content

def create_folder():
    """
    this function make a folders to save the data
    """
    try:
        os.mkdir('save')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def extract_data(n):
    """
    this function extracts data from websites and stores it in .docx files.
    """
    content = validate_tags_for_main()
    create_folder()
    with (open('save/archive_{}.docx'.format(n), 'w')) as FILE:
        FILE.write(content)

def search_links():
    """
    this function is in charge of searching to enter in each one of the links
    """
    links = save_links()
    for i in range(len(links) + 1):
        driver.get(links[i])
        extract_data(i + 1)
        time.sleep(2)

search_links()