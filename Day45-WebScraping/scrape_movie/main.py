import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response=requests.get(URL)
data = response.text
#print(data)

soup = BeautifulSoup(data, "lxml")
pprint(soup.find_all(name="img", class_='landscape'))

contents = soup.find_all(name="img", class_='landscape')
print(contents)
movie_list = []
for content in contents:
    movie = content.get("title")
    movie_list.append(movie)

with open("./scrape_movie/movies.txt",'w', encoding='utf-8') as f:
   for i in reversed(range(len(movie_list))):
    f.writelines(movie_list[i] + "\n")
