import requests
from bs4 import BeautifulSoup

testURL = 'http://www.scrapethissite.com/pages/simple/'

page = requests.get(testURL)
soup = BeautifulSoup(page.text, "html.parser")

country_names = []
capitals = []
populations = []

for names in soup.find_all('h3', class_="country-name"):
    country_names.append( names.text.strip())

    print(country_names)

for capital in soup.find_all('span', class_="country-capital"):
    capitals.append(capital.text.strip())

    print (capitals)


for population in soup.find_all('span', class_="country-area"):
    populations.append(population.text.strip())

    print (populations)

    
