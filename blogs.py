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
    title_jdh = main_jdh.find("a").text
    url_blog = main_jdh.find("a")["href"]

    return [title_jdh, url_blog]

# Stephen Wolfram's *writings* blog.
def wolfram_writings():

    url_wolf = "https://writings.stephenwolfram.com/"
    response_wolf = requests.get(url_wolf)
    soup_wolf = BeautifulSoup(response_wolf.text, "html.parser")

    latest_article_data = soup_wolf.find("article").find("a")

    article_title = latest_article_data.text
    article_url = latest_article_data["href"]

    return [article_title,article_url]

# Matt Baker's blog.
def baker_headline():

    url_baker = "https://mattbaker.blog/"
    response_baker = requests.get(url_baker)
    soup_baker = BeautifulSoup(response_baker.text, "html.parser")

    main_baker = soup_baker.find("h1", class_="entry-title")
    title_baker = main_baker.a.text
    article_url = main_baker.a["href"]

    return [title_baker, article_url]

# # Logic Matters
# def logic_matters():
#
#     url_logic = "https://www.logicmatters.net/blogfront/"
#     response_logic = requests.get(url_logic)
#     soup_logic = BeautifulSoup(response_logic.text, "html.parser")
#     print(soup_logic)
#
#     main_logic = soup_logic.find("h2", class_="entry-title")
#     print(type(main_logic))
#     #main_logic_again = main_logic.find("a")
#     #title_logic = main_logic_again.text
#
#     return title_logic


# Godels lost letter
def godel_letter():

    url_godel = "https://rjlipton.wordpress.com/"
    response_godel = requests.get(url_godel)
    soup_godel = BeautifulSoup(response_godel.text, "html.parser")

    # First pick out the section containing recent post.
    section_godel = soup_godel.find("div", id = "content", class_="pad")

    # Now pick out the title part of the HTML.
    main_godel = section_godel.find("h2")
    title_godel = main_godel.text
    article_url = main_godel.find("a")["href"]

    return [title_godel,article_url]

# Annoying precision
def annoying_precision():

    url_annoying_precision = "https://qchu.wordpress.com/"
    response_annoying_precision = requests.get(url_annoying_precision)
    soup_annoying_precision = BeautifulSoup(response_annoying_precision.text, "html.parser")

    # First pick out the section containing recent post.
    section_annoying_precision = soup_annoying_precision.find("div", class_="posttitle")

    # Now pick out the title part of the HTML.
    main_annoying_precision = section_annoying_precision.find("h2")
    title_annoying_precision = main_annoying_precision.text
    article_url = main_annoying_precision.find("a")["href"]

    return [title_annoying_precision,article_url]

# Full stack python (blog)
def fullstack_python():

    url_python = "https://www.fullstackpython.com/blog.html"
    response_python = requests.get(url_python)
    soup_python = BeautifulSoup(response_python.text, "html.parser")

    # Zero in on the information.
    section_python = soup_python.find("div", class_="c9")

    blog_link = url_python + section_python.find("a")["href"]
    blog_title = section_python.find("a").text

    return [blog_title, blog_link]
