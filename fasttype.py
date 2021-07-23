from types import WrapperDescriptorType
from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get("https://10fastfingers.com/typing-test/english")
sleep(5)
word_list = driver.execute_script("return document.getElementById('wordlist').innerHTML")
words = word_list.split("|")
for i in range(len(words)):
    driver.find_element_by_id("inputfield").send_keys(words[i] + " ")
    sleep(0.15)