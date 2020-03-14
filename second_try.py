import requests
from bs4 import BeautifulSoup

# Define the url in question
url = "https://genius.com/Disturbed-stricken-lyrics"

# Define an object to store the HTML
response = requests.get(url)

# Put HTML through BeautifulSoup to make it nicer to parse.
soup = BeautifulSoup(response.text, "html.parser")

# Find the title of the page.
title = soup.title
title = title.get_text()
print(title)

#stories = soup.find_all('li', class_='o-digest')
lyrics = soup.find(class_="lyrics")
print(lyrics.text)
