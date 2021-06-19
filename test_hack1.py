from app import *
import requests
import pytest
from hack1 import brute_force_login,guess_password,sess_pred,directory_transversal, xss_attack
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from threading import Thread
import os
import time



def setup_module():
    # yeah this is FUGLY. But 20 different ways ot test flask apps, and they have one issue or other
    # I wanted black box testing, but cant get that working
    os.system("python3 app.py &")
    time.sleep(2)

# @pytest.mark.usefixtures('live_server')
def test_guess_password():
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.headless = True
    driver = webdriver.Firefox(options=fireFoxOptions)

    try:
        u,p=guess_password(driver)
        assert(u == "Perry.Platypus")
        assert(p == "ilovefish")
    except:
        assert False , "TEST test_guess_password FAILED"

    finally:
        driver.close()

def test_sess_pred():
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.headless = True
    driver = webdriver.Firefox(options=fireFoxOptions)

    try:
        users=sess_pred(driver)
    except:
        assert False , "TEST test_sess_pred FAILED"
    finally:
        driver.close()
    assert(users == [0,1,2])

@pytest.mark.skip(reason="doesnt work in CI")
def test_directory_transversal():
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.headless = True
    driver = webdriver.Firefox(options=fireFoxOptions)

    try:
        text = directory_transversal(driver)
    except:
        assert False , "TEST test_directory_transversal FAILED"
    finally:
        driver.close()
    assert("root:!" in text)


def test_xss_attack():
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.headless = True
    driver = webdriver.Firefox(options=fireFoxOptions)

    try:
        text = xss_attack(driver)
    except:
        assert False , "TEST test_xss_attack FAILED"
    finally:
        driver.close()
    assert("secret password=1234567" in text)

def teardown_module():

     # yeah this is FUGLY
    os.system("killall python3")
