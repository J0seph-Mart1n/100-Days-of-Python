from bs4 import BeautifulSoup
#import lxml
import requests

response = requests.get(url="https://news.ycombinator.com")
yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")
# print(soup.title)
articles = soup.find_all(name="span", class_="titleline")
article_name = []
article_link = []
for article_tags in articles:
    name = article_tags.get_text()
    link = article_tags.a.get("href")
    article_name.append(name)
    article_link.append(link)

article_upvote = [int(upvote.get_text().replace(" points", "")) for upvote in soup.find_all(name="span", class_="score")]
print(article_name)
print(article_link)
print(article_upvote)

max_value = max(article_upvote)
max_value_index = article_upvote.index(max_value)
print(article_name[max_value_index])
print(article_link[max_value_index])




# with open("website.html", "r", encoding="utf-8") as file:
#     contents = file.readlines()
#     contents = "".join(contents)
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.a)
# # anchor_tags = soup.find_all(name="a")
# # print(anchor_tags)
# # for tags in anchor_tags:
# #     print(tags.get_text())
# #
# # heading = soup.find(name="h1", id="name")
# # print(heading)
# # section = soup.find(name="h3", class_="heading")
# # print(section.get_text())
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(selector=".heading")
# print(headings)