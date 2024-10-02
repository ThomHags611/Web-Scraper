from bs4 import BeautifulSoup
import requests


url = "https://www.espn.com/nfl/boxscore/_/gameId/401671789"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

player = soup.findAll("a", attrs= {"class" : "AnchorLink Boxscore__Athlete_Name truncate db"})

print(player)
for i in player:
   print(i.text)