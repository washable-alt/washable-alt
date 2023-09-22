from bs4 import BeautifulSoup
import lxml
import requests
import json
from pprint import pprint
from datetime import datetime, timedelta

def beautiful_soup_parsing():

    try:
        with open("website.html", 'rb') as file:
            contents = file.read()
        #soup = BeautifulSoup(contents, "html.parser")
        soup = BeautifulSoup(contents, "lxml")
        #<title> Angela's Personal Site</title>
        print(soup.title)
        # Angela's Personal Site
        print(soup.title.string)
        # Prettify 
        print(soup.prettify())
        # print paragraph tags (p tags)
        #print(soup.p)

        all_anchor_tags = soup.find_all(name="a")
        
        for tag in all_anchor_tags:
            # print tag
            print(tag)
            # print text embedded between the tags
            print(tag.getText())
            # print the attribute of the tag
            print(tag.get("href"))
        
        # to not clash with the attribute, the class attribute is added with underscore _
        section_heading = soup.find_all(name="h3", class_="heading")
        
        for tag in section_heading:
            print(tag.getText())

        name = soup.select_one(selector="#name")
        print(name)
        
        company_url = soup.select_one(selector="p a")
        print(company_url)

        headings = soup.select(".heading")
        print(headings)
        
        for heading in headings:
            print(heading)
            print(heading.getText())

    except Exception as e:
        print(e)

def main():
    items = []

    response = requests.get("https://news.ycombinator.com/news")
    try:
        yc_webpage = response.text

        soup = BeautifulSoup(yc_webpage, "html.parser")
        #print(soup.title)
        #print(soup)

        numbers = soup.select(".rank")
        # for number in numbers:
            # print(number.getText())
        
        rels = soup.find_all(name="a", rel="noreferrer")
        
        #for rel in rels:
            #pprint(rel.getText())
            #pprint(rel.get("href"))

        scores = soup.select(".score")
        # for score in scores:
        #     pprint(score.getText())
        
        ages = soup.select(".age")
        # for age in ages:
        #     input_str = age.getText()
        #     num = ""
        #     for char in input_str:
        #         if char.isdigit():
        #             num+=char
        #     #print(num)
        #     num = int(num)
        #     dt = (datetime.now() - timedelta(hours=num)).strftime(r"%m/%d/%Y, %H:%M:%S")
        #     #print(dt)
       

        for number, rel, score, age in zip(numbers, rels, scores, ages):
            
            input_str = age.getText()
            num = ""
            for char in input_str:
                if char.isdigit():
                    num+=char
            new_score = ""
            input_string = score.getText()
            for char in input_string:
                if char.isdigit():
                    new_score+=char
            #print(new_score)

            #print(num)
            num = int(num)
            dt = (datetime.now() - timedelta(hours=num)).strftime(r"%m/%d/%Y, %H:%M:%S")
            #print(f"{number.getText()} Brief: {rel.getText()} - Score: {score.getText()} - PublishedAt(GMT+8): {dt} around {age.getText()}" )

            items.append({
            "number": number.getText(),
            "rel": rel.getText(),
            "score": score.getText().split()[0],
            "published_at": dt,
            "age": age.getText(),
            "link": rel.get("href")
            })
        #print(items)
            
        # Sort the items list by scores in descending order
        sorted_items = sorted(items, key=lambda x: int(x["score"]), reverse=True)
        #print(sorted_items)

        for i,item in zip(range(len(sorted_items)),sorted_items):
            print(f"{i+1}. Headline: {item['rel']} - Score: {item['score']} Points - PublishedAt(GMT+8): {item['published_at']} around {item['age']}. Item Number:{item['number']} {item['link']}")
            
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()