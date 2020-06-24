from selenium import webdriver
import time
import requests
import bs4

# new, top, mix, track, and artist urls
top_url = "http://soundcloud.com/charts/top"
new_url = "http://soundcloud.com/charts/new"
track_url = "http://soundcloud.com/search/sounds?q="
artist_url = "http://soundcloud.com/search/people?q="
mix_url_end = "&filter.duration=epic"

# create the selenium browser
browser = webdriver.Safari(executable_path='/usr/bin/safaridriver')
browser.get("https://soundcloud.com")
time.sleep(30)

# main menu
print()
print(">>> python soundcloud scraper!")
print(">>> explore top / new & hot charts for all genres")
print(">>> search for tracks, artist, and mixes")
print()

while True:
    print(">>> menu")
    print(">>> 1 - search for a track")
    print(">>> 2 - search for an artist")
    print(">>> 3 - search for a mix")
    print(">>> 4 - top charts")
    print(">>> 5 - new & hot charts")
    print(">>> 0 - exit")

    choice = int(input(">>> your choice: "))

    if choice == 0:
        browser.quit()
        break
    print()

    # search for a track
    if choice == 1:
        name = input("name of the track: ")
        print()
        "%20".join(name.split(" "))
        browser.get(track_url + name)
        continue

    # search for an artist
    if choice == 2:
        name = input("name of the artist: ")
        print()
        "%20".join(name.split(" "))
        browser.get(artist_url + name)
        continue

    # search for a track
    if choice == 3:
        name = input("name of the mix: ")
        print()
        "%20".join(name.split(" "))
        browser.get(track_url + name + mix_url_end)
        continue

    # get the top 50 tracks for a genre
    if choice == 4:
        request = requests.get(top_url)
        soup = bs4.BeautifulSoup(request.text, "lxml")
        while True:
            print(">>> genres: ")
            print()
            genres = soup.select("a[href*=genre]")[2:]
            genre_links = []

            # print out all of the genres
            for index, genre in enumerate(genres):
                print(str(index) + ": " + genre.text)
                genre_links.append(genre.get("href"))

            print()
            choice = input(">>> your choice (x to go back to the main menu): ")
            print()

            if choice == "x":
                break
            else:
                choice = int(choice)

            url = "http://soundcloud.com" + genre_links[choice]
            request = requests.get(url)
            soup = bs4.BeautifulSoup(request.text, "lxml")

            tracks = soup.select("h2")[3:]
            track_links = []
            track_names = []

            for index, track in enumerate(tracks):
                track_links.append(track.a.get("href"))
                track_names.append(track.text)
                print(str(index + 1) + ": " + track.text)
                print()

            # song selection loop
            while True:
                choice = input(">>> your choice (x to re-select a new genre): ")
                print()

                if choice == "x":
                    break
                else:
                    choice = int(choice) - 1

                print("now playing: " + track_names[choice])
                print()

                browser.get("http://soundcloud.com" + track_links[choice])

    # get the new & hot tracks for a genre
    if choice == 5:
        request = requests.get(new_url)
        soup = bs4.BeautifulSoup(request.text, "lxml")
        while True:
            print(">>> genres: ")
            print()
            genres = soup.select("a[href*=genre]")[2:]
            genre_links = []

            # print out all of the genres
            for index, genre in enumerate(genres):
                print(str(index) + ": " + genre.text)
                genre_links.append(genre.get("href"))

            print()
            choice = input(">>> your choice (x to go back to the main menu): ")
            print()

            if choice == "x":
                break
            else:
                 choice = int(choice)

            url = "http://soundcloud.com" + genre_links[choice]
            request = requests.get(url)
            soup = bs4.BeautifulSoup(request.text, "lxml")

            tracks = soup.select("h2")[3:]
            track_links = []
            track_names = []

            for index, track in enumerate(tracks):
                track_links.append(track.a.get("href"))
                track_names.append(track.text)
                print(str(index + 1) + ": " + track.text)
                print()

            # song selection loop
            while True:
                choice = input(">>> your choice (x to re-select a new genre): ")
                print()

                if choice == "x":
                    break
                else:
                    choice = int(choice) - 1

                print("now playing: " + track_names[choice])
                print()

                browser.get("http://soundcloud.com" + track_links[choice])

print()
print("pce out")
print()
