import requests
from bs4 import BeautifulSoup
from csv import writer, DictReader

response = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")
results = soup.find_all(class_='quote')
all_quotes = []
with open("myquotes.csv", "w") as csv_file:
	for res in results:
		all_quotes.append({
			"text": res.find(class_='text').get_text(),
			"author": res.find(class_='author').get_text(),
			"bio-link": res.find('a')['href']

			})
	csv_file.write("Text"+ "Author"+ "Link")
	# csv_file.writer([text,author, bio-link])
