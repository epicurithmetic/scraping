# Scraping information from blogs.
import requests
import webbrowser
from bs4 import BeautifulSoup

# Joel David Hampkins: Mathematics and Philosophy of the infinite.
def jdh_headline():

    url_jdh = "http://jdh.hamkins.org/"
    response_jdh = requests.get(url_jdh)
    soup_jdh = BeautifulSoup(response_jdh.text, "html.parser")

    main_jdh = soup_jdh.find("h1", class_="entry-title")
    title_jdh = main_jdh.text

    return title_jdh

# Matt Baker's blog.
def baker_headline():

    url_baker = "https://mattbaker.blog/"
    response_baker = requests.get(url_baker)
    soup_baker = BeautifulSoup(response_baker.text, "html.parser")

    main_baker = soup_baker.find("h1", class_="entry-title")
    title_baker = main_baker.text

    return title_baker

# Logic Matters

# Godels lost letter

# M - Phi

# Annoying precision

# Full stack python (blog)
