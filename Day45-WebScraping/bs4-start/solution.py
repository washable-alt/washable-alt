from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
#article_tag = soup.find(name="a", rel="noreferrer")
# print(article_tag)
# article_text = article_tag.getText()
# print(article_text)
# article_link = article_tag.get("href")
# print(article_link)
# article_upvote = soup.find(name="span", class_="score").getText()
# print(article_upvote)

articles = soup.find_all(name="a", rel="noreferrer")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])

