from bs4 import BeautifulSoup
import requests
import webbrowser

while True:

    # Retrieve URL, initiate parser, set heading
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, 'html.parser')
    heading = soup.find(class_='firstHeading').text

    # Begin user input
    print(heading, "\nWould you like to open this? (Y/N/EXIT)")
    open = input('').lower()
    if open == 'exit':
        break
    elif open == 'y':
        url = 'https://en.wikipedia.org/wiki/{}'.format(heading)
        webbrowser.open(url)
        continue
    elif open == 'n':
        print("Let's try another!")
        continue
    else:
        print("Invalid input...")
        continue
