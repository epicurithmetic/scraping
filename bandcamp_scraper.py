# This code finds the name of the latest releases from by favourite artists and
# record labels on bandcamp.
import os
import requests
from bs4 import BeautifulSoup

arist_list = ["Ultimae",
              "Synphaera",
              "Exosphere",
              "White Label Records",
              "Carbon Based Lifeforms",
              "Hydrangea",
              "Abul Mogard",
              "Faint",
              "Solar Fields",
              "Trentemoller",
              "Alfa Mist"]

# Read in the data from the last time we checked.
N = len(arist_list)
bandcamp_old_release_data = []
bandcamp_database = open("bandcamp_database.txt","r")

for i in range(0,N):
    data = bandcamp_database.readline()
    data_list = data.split(":& ")
    release_name = data_list[1].replace("\n","")    # Cleans the EOL command.
    bandcamp_old_release_data.append(release_name)

# Close the file.
bandcamp_database.close()

# Now we can obtain the current release information.
def bandcamp_latest_release(url):

    url_artist_discog = url
    response_artist_discog = requests.get(url_artist_discog)
    soup_artist_discog = BeautifulSoup(response_artist_discog.text, "html.parser")

    data_artist_discog = soup_artist_discog.find("p", class_="title")
    newest_artist_discog = data_artist_discog.text

    return newest_artist_discog

# Create a list of URL to loop-through:
bandcamp_list = ["https://ultimae.bandcamp.com/",
                 "https://synphaera.bandcamp.com/",
                 "https://exospheremusic.bandcamp.com/",
                 "https://whitelabrecs.bandcamp.com/music",
                 "https://carbonbasedlifeforms.bandcamp.com/music",
                 "https://hydrangea.bandcamp.com/",
                 "https://abulmogard.bandcamp.com/",
                 "https://faintmusic.bandcamp.com/",
                 "https://solarfields.bandcamp.com/",
                 "https://trentemoller.bandcamp.com/",
                 "https://alfamist.bandcamp.com/music"]

# Clean the format of the scraped release_title
def release_name_clean(raw_release_name):

    """
        This function cleans the release name.

        When I scrape the release name, there is often a lot of
        extra text in the string. For example, the artist name
        and a lot of spaces and new line commands.

    """

    # First remove any newline commands.
    raw_release_name = raw_release_name.replace("\n","")

    # Get rid of the arist name by splitting by a fixed number of spaces.
    split_release_name = raw_release_name.split("              ",1)

    # Get rid of the spaces at the beginning of the release name.
    release_name_string = split_release_name[0]
    release_name_list = list(release_name_string)
    while release_name_list[0] == " ":
        del release_name_list[0]
    # Remove spaces from the start of the release name.

    clean_release_name = ""
    for a in release_name_list:
        clean_release_name += a

    return clean_release_name

# This does the work to get the new information.
newest_releases = []
for url in bandcamp_list:
    raw_release_title = bandcamp_latest_release(url)
    clean_release_title = release_name_clean(raw_release_title)
    newest_releases.append(clean_release_title)

for i in range(0,N):

    if newest_releases[i] == bandcamp_old_release_data[i]:
        print(" "*10 + arist_list[i] +": " + newest_releases[i])
    else:
        print(" "*10 + arist_list[i] +": " + newest_releases[i] + " [New!]")

# Now we can update the database with the new release information.
file = open("bandcamp_database.txt","w")
for i in range(0,N):
    if i == 0:
        new_data = arist_list[i] + ":& " + newest_releases[i]
        file.write(new_data)
    else:
        new_data = "\n" + arist_list[i] + ":& " + newest_releases[i]
        file.write(new_data)


file.close()
