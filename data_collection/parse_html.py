from bs4 import BeautifulSoup
import requests

html = requests.get("http://google.com").text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p') # or soup.p
first_paragraph_text = soup.p.text
first_paragraph_words = soup.p.text.split()

first_paragraph_id = soup.p.get('id')

all_paragraphs = soup.find_all('p') # or soup('p')
paragraphs_with_ids = [p for p in soup('p') if p.get('id')]

