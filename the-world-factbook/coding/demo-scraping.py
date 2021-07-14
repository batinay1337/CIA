from selenium import webdriver
import numpy as np
import pandas as pd
import time

browser = webdriver.Chrome("C:\Program Files\chromedriver\chromedriver.exe")

f = open("../field/country-names.txt", "r")

for i in f:
    i = i.strip("\n")

    browser.get(f"https://www.cia.gov/the-world-factbook/countries/{i}")

    geographic_coordinate = browser.find_element_by_xpath("//*[@id='geography']/div[1]/p")

    print(geographic_coordinate.text)

f.close()