from selenium import webdriver
import numpy as np
import pandas as pd
import time

browser = webdriver.Chrome("C:\Program Files\chromedriver\chromedriver.exe")

f = open("../field/country-names.txt", "r")

for i in f:
    i = i.strip("\n")

    browser.get(f"https://www.cia.gov/the-world-factbook/countries/{i}")

    location = browser.find_element_by_xpath("//*[@id='geography']/div[1]/p")
    geographic_coordinate = browser.find_element_by_xpath("//*[@id='geography']/div[2]/p")
    map_reference = browser.find_element_by_xpath('//*[@id="geography"]/div[4]/p')

    with open("../data/all_data.csv", "a") as dataset_file:
        dataset_file.write(f"'{i}','{geographic_coordinate.text}','{map_reference.text}'\n")

f.close()