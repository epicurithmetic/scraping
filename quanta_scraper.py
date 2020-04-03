# Code to scrape information from Quanta magazine.
import requests
from bs4 import BeautifulSoup

# Quanta headlines
def QuantaHeadlines():

    url_quanta = "https://www.quantamagazine.org/"
    response_quanta = requests.get(url_quanta)
    soup_quanta = BeautifulSoup(response_quanta.text, "html.parser")

    headlines = []

    # This gets the primary headline on the homepage.
    main = soup_quanta.find("h1", class_="noe mv0 h0 color-transition hover--orange")
    headlines.append(main.text)

    # This gets the rest of the stories on the homepage.
    sub_headlines = soup_quanta.find_all("h2", class_="card__title noe mv0 theme__accent-hover transition--color")
    for x in sub_headlines:
        headlines.append(x.text)

    return headlines

# Quanta physics headlines
def Quanta_Physics():

    url_quanta = "https://www.quantamagazine.org/physics/"
    response_quanta = requests.get(url_quanta)
    soup_quanta = BeautifulSoup(response_quanta.text, "html.parser")

    headlines = []

    # This gets the primary headline on the homepage.
    main = soup_quanta.find("h1", class_="hero__card__title mv05 noe")
    headlines.append(main.text)

    # This gets the rest of the stories on the homepage.
    sub_headlines = soup_quanta.find_all("h2", class_="card__title noe mv0 theme__accent-hover transition--color")
    for x in sub_headlines:
        headlines.append(x.text)

    return headlines

# Quanta mathematics headlines
def Quanta_Math():

    url_quanta = "https://www.quantamagazine.org/mathematics/"
    response_quanta = requests.get(url_quanta)
    soup_quanta = BeautifulSoup(response_quanta.text, "html.parser")

    headlines = []

    # This gets the primary headline on the homepage.
    main = soup_quanta.find("h1", class_="hero__card__title mv05 noe")
    headlines.append(main.text)

    # This gets the rest of the stories on the homepage.
    sub_headlines = soup_quanta.find_all("h2", class_="card__title noe mv0 theme__accent-hover transition--color")
    for x in sub_headlines:
        headlines.append(x.text)

    return headlines

# Quanta computer science headlines
def Quanta_CS():

    url_quanta = "https://www.quantamagazine.org/computer-science/"
    response_quanta = requests.get(url_quanta)
    soup_quanta = BeautifulSoup(response_quanta.text, "html.parser")

    headlines = []

    # This gets the primary headline on the homepage.
    main = soup_quanta.find("h1", class_="hero__card__title mv05 noe")
    headlines.append(main.text)

    # This gets the rest of the stories on the homepage.
    sub_headlines = soup_quanta.find_all("h2", class_="card__title noe mv0 theme__accent-hover transition--color")
    for x in sub_headlines:
        headlines.append(x.text)

    return headlines
