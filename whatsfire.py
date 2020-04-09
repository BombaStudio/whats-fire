from os import *
import sys

help = """
    (1)(bomber) whatsapp bomber
"""
inp = "[whats fire]"

def bomb(path):
    driver = webdriver.Chrome(executable_path=path)
    driver.get('https://web.whatsapp.com/')
    victim = input("enter victim:")
    mess = input("message:")
    count = int(input("set count:"))
    kullan = driver.find_element_by_xpath('//span[@title = "{}"]'.format(victim))
    kullan.click()
    messbox = driver.find_element_by_class_name('_3u328')
    for i in range(count):
        messbox.send_keys(msg)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()
    print("mission passed :D")
def main(x):
    if x == "help":
        print(help)
    if x == "1" or x == "bomber":
        path = input("enter partch:")
        bomb(path)
def main3():
    while True:
        x = input(inp)
        main(x)
def setup():
    if sys.version_info.major == 2:
        print("python version is not 3 please install python3")
    elif sys.version_info.major == 3:
        system("pip3 install selenium")
        print("selenium is installed. please install webdriver.")
if __name__ == '__main__':
    try:
        from selenium import webdriver
    except:
        setup()
    if sys.version_info.major == 2:
        print("python version is not 3 please install python3")
    elif sys.version_info.major == 3:
        main3()