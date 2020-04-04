# Code to scrape information from Quanta magazine.
import requests
from bs4 import BeautifulSoup

# Quanta headlines
def QuantaHeadlines():

    """
        This function gets headlines and the links for the stories
        from the homepage of the Quanta Magazine webpage.

        This function returns a list whose entries are themselves lists
        of the form: [headline, story_url]

    """

    url_quanta = "https://www.quantamagazine.org/"
    response_quanta = requests.get(url_quanta)
    soup_quanta = BeautifulSoup(response_quanta.text, "html.parser")

    headlines = []

                        # Main headline
    # This zeroes in on the HTML for the main headline.
    main_data = soup_quanta.find("div", class_="hero-title pb2")

    # First we can get the headline.
    headline_data = main_data.find("h1", class_="noe mv0 h0 color-transition hover--orange")
    headline_text = headline_data.text

    # Next we can get the link for this story.
    link_data = main_data.find_all("a")                            # Note: We have to do some hack here to get the link
    link_data_relevant = link_data[1]                              #       to the story and not to the "tag" under which
    headline_link = url_quanta[:-1] + link_data_relevant['href']   #       the story is classified e.g. Abstractions blog.
                                                                   #       So I assumed the link for the story will be the
    # Add this to the list of headlines.                           #       second link collected. This may cause trouble!
    headlines.append([headline_text, headline_link])

                    # Next block of stories
    more_data = soup_quanta.find_all("div", class_="card__content")

    for story in more_data:

        # Get the headline.
        more_headline_data = story.find("h2", class_="card__title noe mv0 theme__accent-hover transition--color")
        more_headline = more_headline_data.text

        # Get the URL.
        more_link_data_list = story.find_all("a")
        more_link_data_relevant = more_link_data_list[1]
        more_headline_link = url_quanta[:-1] + more_link_data_relevant["href"]

        # Add this data to the list.
        headlines.append([more_headline, more_headline_link])

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
