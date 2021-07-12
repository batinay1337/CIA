import requests
from bs4 import BeautifulSoup

vgm_url = "https://www.cia.gov/the-world-factbook/countries/"
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))