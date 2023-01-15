from bs4 import BeautifulSoup
import requests as rq
response = rq.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
tag = soup.findAll(name="h3", class_="title")
for item in tag[::-1]:
    with open("100movies.txt", mode="a", encoding="utf-8") as file:
        file.write(f"{item.get_text()}\n")


