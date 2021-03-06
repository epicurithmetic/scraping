# Code for scraping information from psychology and meditation focused blogs.
import requests
from bs4 import BeautifulSoup

def HHtDL():

    url_HHtDL = "https://www.dalailama.com/news"
    response_HHtDL = requests.get(url_HHtDL)
    soup_HHtDL = BeautifulSoup(response_HHtDL.text, "html.parser")

    latest_entry_section = soup_HHtDL.find("div", class_="card")
    latest_entry_subsection = latest_entry_section.find("h3")

    latest_entry_url_section = latest_entry_subsection.find("a")
    latest_entry_url = latest_entry_url_section['href']
    latest_entry_title = latest_entry_subsection.text


    return [latest_entry_title,latest_entry_url]

def jungianthology():

    url_jung = "https://jungchicago.org/blog/category/blog-posts/"
    response_jung = requests.get(url_jung)
    soup_jung = BeautifulSoup(response_jung.text, "html.parser")

    data_jung = soup_jung.find("h2",class_="excerpt-title")
    data_jung_finer = data_jung.find("a")

    title_blog = data_jung_finer.text
    url_blog = data_jung_finer["href"]

    return [title_blog, url_blog]

def myth_matters():

    url_mm = "https://mythologymatters.wordpress.com/"
    response_mm = requests.get(url_mm)
    soup_mm = BeautifulSoup(response_mm.text,"html.parser")

    data_mm = soup_mm.find("h2",class_="entry-title")
    data_mm_finer = data_mm.find("a")

    title_blog = data_mm_finer.text
    url_blog = data_mm_finer["href"]

    return [title_blog, url_blog]
