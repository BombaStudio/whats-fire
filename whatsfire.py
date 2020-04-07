from os import *
import sys

help = """
    (1)(bomber) whatsapp bomber
"""
inp = "[whats fire]"

def bomb():
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')
    if sys.version_info.major == 3:
        victim = input("enter victim:")
        mess = input("message:")
        count = int(input("set count:"))
    if sys.version_info.major == 2:
        victim = raw_input("enter victim:")
        mess = raw_input("message:")
        count = input("set count:")
    kullan = driver.find_element_by_xpath('//span[@title = "{}"]'.format(victim))
    kullan.click()
    messbox = driver.find_element_by_class_name('_2bXVy')
    for i in range(count):
        messbox.send_keys(msg)
        button = driver.find_element_by_class_name('_2lktd')
        button.click()
    print("mission passed :D")
def main(x):
    if x == "help":
        print(help)
    if x == "1" or x == "bomber":
        bomb()
def main2():
    while True:
        x = raw_input(inp)
        main(x)
def main3():
    while True:
        x = input(inp)
        main(x)
def setup():
    if sys.version_info.major == 2:
        system("pip2 install selenium")
    elif sys.version_info.major == 3:
        system("pip3 install selenium")
if __name__ == '__main__':
    try:
        from selenium import webdriver
    except:
        setup()
    if sys.version_info.major == 2:
        main2()
    elif sys.version_info.major == 3:
        main3()