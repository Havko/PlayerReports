import nflgame
import csv
games = nflgame.games(2015)
players = nflgame.combine_game_stats(games)
c = csv.writer(open("/rushing.csv", "wb"))
#This method outputs All rushing performance of the season and the opponents
def all_rushing():
	for game in games:
		for p in game.players.rushing().sort("rushing_yds"):
				opp = ""
				if p.team == game.home:
					opp = game.away
				else:
					opp = game.home
				c.writerow([str(p.team), str(p), str(p.rushing_att), str(p.rushing_yds), opp] )
				
			
def defense_vs_rush():
	for game in games:
		for p in game.players.rushing().sort("rushing_yds"):
				opp = ""
				yds_100 = []
				if p.team == game.home:
					opp = game.away
				else:
					opp = game.home
				if p.rushing_yds > 100:					
					c.writerow([str(p.team), str(p), str(p.rushing_att), str(p.rushing_yds), opp] )
			
defense_vs_rush()
