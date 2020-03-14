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

# def genius_song_lyrics(artist, song):
#
#
#     """
#         This function takes as input two strings:
#
#             arist = name of the artist
#             song = name of song of which the lyrics are sought
#
#         First the function builds the url based on the manner in which
#         genius.com designs their urls for songs. This has to take into account
#         their choices for dealing with things like:
#
#             There are is no punctutation in the url i.e. none of:
#                         ',().
#                     These are simply ignored when building the url.
#
#             & in the song name goes to "and" in the url
#
#             Any mention of (Ft. ), Featuring etc. does not appear in the url.
#
#     """

# Try to obtain the list of song names from the album page.
url_album = "https://genius.com/albums/Disturbed/Ten-thousand-fists"
response_album = requests.get(url_album)
soup_album = BeautifulSoup(response_album.text, "html.parser")

songs = soup_album.find_all("h3", class_="chart_row-content-title")
# for song in songs:
#     print(song.text)

# Rather than build the url according to the song name and accounting for
# the design style of the website. I can just grab the url from the HTML!
song_url_data = (soup_album.find_all("a", class_="u-display_block"))
song_url_list = []
for link in song_url_data:
    song_url_list.append(link['href'])
