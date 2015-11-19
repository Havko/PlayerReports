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
				if p.rushing_yds > 100:
					c.writerow([str(p.team), str(p), str(p.rushing_att), str(p.rushing_yds), opp] )
#this method out puts various defensive performance against the rush			
			
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
					
def defense_vs_pass():
	for game in games:
		for p in game.players.rushing().sort("passing_yds"):
				opp = ""
		
				yds_300 = []
				if p.team == game.home:
					opp = game.away
				else:
					opp = game.home
				if p.passing_yds > 300:					
					c.writerow([str(p.team), str(p), str(p.passing_att), str(p.passing_yds), opp] )
					
					
def all_passing():
	for game in games:
		for p in game.players.passing().sort("passing_yds"):
				opp = ""
				if p.team == game.home:
					opp = game.away
				else:
					opp = game.home
				if p.rushing_yds > 300:
					c.writerow([str(p.team), str(p), str(p.rushing_att), str(p.rushing_yds), opp] )
					
def def_vs_receiving():
	for game in games:
		for p in game.players.receiving().sort("receiving_yds"):
				opp = ""
				yds_100 = []
				if p.team == game.home:
					opp = game.away
				else:
					opp = game.home
				if p.receiving_yds > 100:					
					c.writerow([str(p.team), str(p), str(p.receiving_rec), str(p.receiving_yds), opp] )
					
def calc_ppcp_rb():
		def_cp = {}
		for game in games:
			for p in game.players.receiving().sort("receiving_yds"):
				opp = ""
				yds_100 = []
				if p.team == game.home:
					opp = game.away
				else:
					opp = game.home
				def_cp[opp] = 0
				if p.receiving_yds > 100:	
					def_cp[opp] = def_cp[opp] + 1
		c.writerow([def_cp])				
					
calc_ppcp_rb()
