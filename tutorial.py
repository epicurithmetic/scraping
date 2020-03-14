# Web Scraping Tutorial
from bs4 import BeautifulSoup
import requests
import os

# Functions for tidying the data scraped from Genius
def genius_song_names(song_list):

    """
        This function is for manipulating the song names from album pages
        on genius.com. Since I can't extract the song name exactly, I have
        to delete all of the surrounding information.

    """
    song_name_list = []
    song_name = ''

    for x in song_list:
        if x == "\n\n":
            pass
        elif x =="\n":
            pass
        elif x == ' ':
            pass
        elif x == '':
            pass
        elif x == 'Lyrics\n\n':
            pass
        else:
            song_name_list.append(x)

    for x in song_name_list:
        if x[-1:] == '\n':
            song_name += x[:-1]
        else:
            song_name = song_name + x + ' '

    # Let's remove the apostrophes (... and other grammar)
    song_name = song_name.replace("'","")
    song_name = song_name.replace("(","")
    song_name = song_name.replace(")","")
    song_name = song_name.replace(",","")
    song_name = song_name.replace(".","")
    song_name = song_name.replace(" - "," ")    
    return song_name

#### Scraping code starts here.
more_lyrics = True

while more_lyrics == True:

    # Ask user for artist name:
    print("Please enter the name of the artist:")
    artist_name = input("")
    print("Do they play 'rap' or 'metal'?")
    genre = input("")

    # Use name from user to look up the list of albums:

    # For each album get the list of songs for the artist:
    print("What is the name of the album that you would like the lyrics of?")
    print("[if you are not sure of the required format, then refer to genius.com]")
    album_name_url = input("")
    album_url = "https://genius.com/albums/" + artist_name + "/" + album_name_url

    album_source = requests.get(album_url).text
    album_soup = BeautifulSoup(album_source, 'lxml')

    album_song_data = album_soup.findAll(class_="u-display_block")

    album_tracklist = []
    for data in album_song_data:
        song_name_data = data.text
        # Some song names have a (Ft. *artist name*) label. So we remove that now.
        song_name_data = song_name_data.split(' ')
        song_name_featured = genius_song_names(song_name_data)
        song_name_featured = song_name_featured.split(' (Ft.')
        song_name_featured = song_name_featured[0]
        song_name_featured = song_name_featured.split(' Ft.')
        song_name = song_name_featured[0]
        # Now that the song name is clean, we add it to the tracklist.
        album_tracklist.append(song_name)

    print(album_tracklist)

    # Loop through the list of songs and create a .txt file of the lyrics:
    def song_url_genius(song_name,artist):

        """
            This song takes in the string of the song name and outputs
            the string corresponding the Genius.com url which contains
            the lyrics of that song.

        """

        base_url = 'https://genius.com/' + artist
        song_name_list = song_name.split(' ')
        for x in song_name_list:
            if x == '&':
                base_url = base_url + '-' + 'and'
            else:
                base_url = base_url + '-' + x

        base_url += '-lyrics'

        return base_url

    print(song_url_genius(album_tracklist[0],artist_name))

    # For each song, scrape the lyrics and store in a .txt file.
    for song in album_tracklist:

        print(song)
        # Get the genius.com url for the lyrics.
        url = song_url_genius(song,artist_name)
        print(url)

        # Get the source HTML for the page.
        source = requests.get(url).text

        # Do some BeautifulSoup magic.
        soup = BeautifulSoup(source, 'lxml')

        # Get the lyrics.
        lyrics = soup.find(class_="lyrics").text
        print('Lyrics obtained.')
        # Set file name.
        file_name = genre + "/"+ album_name_url + str(album_tracklist.index(song)) + ".txt"

        # Write the lyrics to the file.
        lyrics_text_file = open(file_name,"w")
        lyrics_text_file.write(lyrics)
        lyrics_text_file.close()
        print('Lyrics written to file.')
        print('Next song is...\n')

    print('All done.')

    print("Would you like the lyrics of another album? (Y/n)")
    answer = input("")
    if answer == "Y":
        pass
    else:
        more_lyrics = False


# Edge cases to be dealt with in order for this method to work:

#   URL can't contain grammatical symbols. For example, no apostrophes or commas
#   URL can't contain "&" symbols. Nor others.
#           (*) genius.com replaces "&" with "and"
#           (*) genius.com simply ignores apostrophes
