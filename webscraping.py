import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_2022"
response = requests.get(url)
print(response.url) # print url
response # response status

songSoup = BeautifulSoup(response.text) # Object of BeautifulSoup

data_dictionary = {}

for song in songSoup.findAll('tr')[1:101]: # loop over index 1 to 101 because the findAll('tr') contains table headers
  # Priting 100 table rows.............
  # print(song)   

  title = song.findAll('a')[0].string

  artist = song.findAll('a')[1].string
  # Printing Titles and Artists.............
  print(title, ',', artist)

  # Printing Dictionary.............
  data_dictionary[title] = [artist]
print(data_dictionary)