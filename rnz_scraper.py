# Scraping information from RNZ
import requests
from bs4 import BeautifulSoup

# RNZ headlines
def RNZHeadlines():

    """
        This function retrieves all headlines (and the urls of the stories)
        from the homepage of the Radio New Zealand website.

        This function returns a list, the elements of which are lists of the
        form: [headline,url]

    """

    url_rnz = "https://www.rnz.co.nz/"
    response_rnz = requests.get(url_rnz)
    soup_rnz = BeautifulSoup(response_rnz.text, "html.parser")

    headlines = []

    # Grab the headlines.
    main = soup_rnz.find_all("h3", class_="o-digest__headline")

    for story in main:
        headline = story.text
        link_data = story.find("a", class_="faux-link")
        link = url_rnz[:-1] + link_data['href']

        headlines.append([headline,link])


    return headlines

ting = RNZHeadlines()
print(ting[0])
print(ting[0][0])
print(ting[0][1])
