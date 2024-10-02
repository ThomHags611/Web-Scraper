import pandas as pd
import requests

class Player:
    id:int = 0
    number:int = 0
    name:str = "blank"
    team:int = 0
    team_name: chr = 'o'
    games_played:int = 0
    minutes:float = 0
    pts: float = 0
    fgPercent: float = 0
    ftPercent: float = 0
    threesMade: float = 0
    totalRebounds: float = 0
    assist: float = 0
    steal:float = 0
    block:float = 0
    turnover: float = 0
    efficiency:float = 0


    def printInfo(self):
        print(self.name, self.team_name, self.games_played, self.minutes, self.pts, self.fgPercent, self.ftPercent, self.totalRebounds, self.assist, self.steal, self.block, self.turnover, self.efficiency )
        
       

    

    def fill_Player(self, input:any, index:int):
        match index:
            case 0:
                self.id = input
            case 1:
                self.number = input
            case 2:
                self.name = input
            case 3:
                self.name = self.name + ' ' + input
            case 4:
                self.team = input
            case 5:
                self.team_name = input
            case 6:
                self.games_played = input
            case 7:
                self.minutes = input
            case 8:
                self.pts = input
            case 10:
                self.fgPercent = input
            case 11:
                self.threesMade = input
            case 16:
                self.ftPercent = input
            case 19:
                self.totalRebounds = input
            case 20: 
                self.assist = input
            case 21:
                self.steal = input
            case 22:
                self.block = input
            case 23:
                self.turnover = input
            case 25:
                self.efficiency = input

            

    
            


test_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2023-24&SeasonType=Playoffs&StatCategory=PTS"
r = requests.get (url = test_url).json()
table_hedaer = r['resultSet']['headers']
current:str

current = r['resultSet']['rowSet'][1]
current = str(current) # this is one player
test = current.split()
player1 = Player()

counter = 0
for i in test:

    print(counter, '    ', i)
    counter += 1

players_list = []
    
for x in range(counter):
    player1.fill_Player(test[x], x)
    print("EXAMPLE", test[x], x)


#player1.printInfo()
tracker = 0
for i in r['resultSet']['rowSet']:
    current = str(i)
    test = current.split()
    player1 = Player()
    
    for x in range(counter):
        player1.fill_Player(test[x], x)

    players_list.append(player1)
    players_list[tracker].printInfo()
    tracker += 1

















