import json

from bs4 import BeautifulSoup
import requests

connect = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best"
                       "-movies-2/")

connect_webpage = connect.text

soup = BeautifulSoup(connect_webpage, "html.parser")

the_movies = []
best_movies = soup.find_all(name="h3", class_="title")
for movies in best_movies:
    the_movies.append(movies.text)
    movies1 = the_movies[::-1]
print(movies1)

with open("my best movies", "w",  encoding="utf-8") as file:
    for all_movies in movies1:
        file.write(f"{all_movies}\n")



