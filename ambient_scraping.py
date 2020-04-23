# Music blog scraping.
import requests
from bs4 import BeautifulSoup

def ambient_blog():

    url_ambient = "https://www.ambientblog.net/blog/"
    response_ambient = requests.get(url_ambient)
    soup_ambient = BeautifulSoup(response_ambient.text, "html.parser")

    title_section = soup_ambient.find_all("h2", class_="entry-title", itemprop = "headline")

    blog_entry_data = []

    for entry in title_section:
        entry_info = entry.find("a")
        entry_title = entry_info.text
        entry_url = entry_info["href"]

        blog_entry = [entry_title,entry_url]
        blog_entry_data.append(blog_entry)


    return blog_entry_data

def orbmag_podcast():

    url_orbcast = "https://www.orbmag.com/music/"
    response_orbcast = requests.get(url_orbcast)
    soup_orbcast = BeautifulSoup(response_orbcast.text, "html.parser")

    title_section = soup_orbcast.find("h3")
    orbcast_title = title_section.find("a").text
    orbcast_url = title_section.find("a")["href"]

    return [orbcast_title,orbcast_url]

def orbmag_news():

    url_orbnews = "https://www.orbmag.com/news/"
    response_orbnews = requests.get(url_orbnews)
    soup_orbnews = BeautifulSoup(response_orbnews.text, "html.parser")

    # Single out all of the new stories on the (first) news page.
    articles_orbnews = soup_orbnews.find_all("article")

    # I don't want updates about "EVENTS". I only want "NEWS" articles.
    articles_just_orbnews = []
    for story in articles_orbnews:
        story_type = story.find("a").text
        if story_type ==  "News":
            articles_just_orbnews.append(story)
        else:
            pass

    # Store the articles I am interested in here.
    article_data = []

    # For each "NEWS" story I need to go ahead and get the title and URL.
    for story in articles_just_orbnews:
        story_data = story.find("h3").find("a")
        # Grab the relevant data.
        story_url = story_data["href"]
        story_title = story_data.text
        # Append the data to the list.
        article_data.append([story_url, story_title])

    return article_data


print(len(ambient_blog()))
print(len(orbmag_news()))
print(orbmag_podcast())
