import requests
from bs4 import BeautifulSoup

def genius_song_lyrics(artist, album):


    """
        This function takes as input two strings:

            arist = name of the artist
            album = name of the album of which the lyrics are sought

        First the function builds the url based on the manner in which
        genius.com designs their urls for albums. This has to take into account
        their choices for dealing with things like:

            There are is no punctutation in the url i.e. none of:
                        ',().
                    These are simply ignored when building the url.

            & in the name goes to "and" in the url

        After storing the lyrics, this function writes them into individual
        .txt files in the same directory that the code is stored.



    """

    # Firt the names of the artist and album have to be reformatted in order
    # to suit the design style of genius.com URLs.
    artist = str(artist)
    artist = artist.replace(" ","-")
    artist = artist.replace("(","")
    artist = artist.replace(")","")
    artist = artist.replace("'","")
    artist = artist.replace(",","")
    artist = artist.replace("&","and")

    album = str(album)
    album = album.replace(" ","-")
    album = album.replace("(","")
    album = album.replace(")","")
    album = album.replace("'","")
    album = album.replace(",","")
    album = album.replace("&","and")

    # Construct the url.
    url_album = "https://genius.com/albums/" + artist + "/" + album

    # Access the website and get the HTML.
    response_album = requests.get(url_album)
    soup_album = BeautifulSoup(response_album.text, "html.parser")

    # Pick out the list of URLs for the songs on the album.
    song_url_data = (soup_album.find_all("a", class_="u-display_block"))
    song_url_list = []
    for link in song_url_data:
        song_url_list.append(link['href'])

    # Visit the URL and scrape the lyrics, storing them in a list.
    lyrics_list = []
    
    for link in song_url_list:
        # Get the HTML for the song page.
        response_song = requests.get(link)
        soup_song = BeautifulSoup(response_song.text, 'html.parser')
        # Pull the lyrics.
        lyrics = soup_song.find(class_="lyrics")
        lyrics_list.append(lyrics.text)

    print("Lyrics obtained.")

    # Now we need to write the lyrics to .txt files.

    return lyrics_list

print(genius_song_lyrics("disturbed","ten thousand fists"))
