from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_website = response.text

soup = BeautifulSoup(empire_website, "html.parser")
movie_name = soup.find_all(name="h3", class_="title")
movie_list = []
for movie in movie_name:
    movie_list.append(movie.get_text())

print(movie_list)
i = len(movie_list) - 1

with open("movies.txt","w", encoding="utf-8") as file:
    while i>=0:
        file.write(f"{movie_list[i]}\n")
        i = i-1
