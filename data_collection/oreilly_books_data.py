from collections import Counter
import re
import requests
from time import sleep

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def is_video(td):
    """it'sa video if it has exactly one pricelabel, and if 
    the strip text inside contains 'Video'"""
    pricelabels = td('span', 'pricelabel')
    return (len(pricelabels) == 1 and 
            pricelabels[0].text.strip().startswith("Video"))

def book_info(td):
    """given a BS <td> tag representing a book, 
    extract the book's details and return a dict"""
    title = td.find("div", "thumbheader").a.text.encode('utf-8')
    author_name = td.find("div", "AuthorName").text
    authors = [x.encode('utf-8').strip() for x in re.sub("^By ", "", author_name).split(",")]
    isbn_link = td.find("div", "thumbheader").a.get("href")
    isbn = re.match("/product/(.*)\.do", isbn_link).group(1).encode('utf-8')
    date = td.find("span", "directorydate").text.encode('utf-8').strip()

    return {
        "title": title,
        "authors" : authors,
        "isbn" : isbn,
        "date" : date
    }

def get_year(book):
    """book["date"] looks like 'July 2015, so we need to split on the space
    and then take the second piece"""
    return int(book["date"].split()[1])

base_url = "http://shop.oreilly.com/category/browse-subjects/" + \
          "data.do?sortby=publicationDate&page="

books =[]

NUM_PAGES = 1

for page_num in range(1, NUM_PAGES + 1):
    print("souping page", page_num, ",", len(books), " found so far")
    url = base_url + str(page_num)
    soup = BeautifulSoup(requests.get(url).text, 'html5lib')
    
    for td in soup('td', 'thumbtext'):
        if not is_video(td):
            books.append(book_info(td))
    # sleeping so oreilly don't get mad
    #sleep(31)

year_counts = Counter(get_year(book) for book in books)
years = sorted(year_counts)
books_counts = [year_counts[year] for year in years]
print(years)
print(book_counts) 
