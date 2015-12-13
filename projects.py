import nflgame
import csv
games = nflgame.games(2015)
players = nflgame.combine_game_stats(games)
rb = csv.writer(open("/projects/python/playerreports/rushing.csv", "wb"))
wr = csv.writer(open("/projects/python/playerreports/receiving.csv", "wb"))
qb = csv.writer(open("/projects/python/playerreports/passing.csv", "wb"))
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
		rush_games = {}
		matchup = {}
	
		week_11 = nflgame.games(2015, week=14)
		for game in week_11:
			
			for p in game.players.rushing().sort("rushing_yds"):
				if p.team == game.home:
					match_opp = game.away
				else:
					match_opp = game.home
				if p.guess_position == 'RB':
					matchup[p.name] = match_opp
			
		
		for game in games:
			def_cp[game.home] = 0
			def_cp[game.away] = 0
			
			for p in game.players.rushing().sort("rushing_yds"):
				rush_games[p.name] = 0
				
		for game in games:



			for p in game.players.rushing().sort("rushing_yds"):


				if p.team == game.home:
					opp = game.away
				else:
					opp = game.home

				if p.rushing_yds > 100:
					def_cp[unicode(opp)] += 1
					rush_games[p.name] += 1
					
		for team in def_cp: 
			rb.writerow([team,def_cp[team]])
		for player in rush_games:
			rb.writerow([player,rush_games[player]])
		

			

			
			
def calc_ppcp_QB():
		def_cp = {}
		rush_games = {}
		matchup = {}
	
		week_10 = nflgame.games(2015, week=14)
		for game in week_10:
			
			for p in game.players.passing().sort("passing_yds"):
				if p.team == game.home:
					match_opp = game.away
				else:
					match_opp = game.home
				if p.guess_position == 'QB':
					matchup[p.name] = match_opp
			
		
		for game in games:
			def_cp[game.home] = 0
			def_cp[game.away] = 0
			
			for p in game.players.passing().sort("passing_yds"):
				rush_games[p.name] = 0
				
		for game in games:



			for p in game.players.passing().sort("passing_yds"):


				if p.team == game.home:
					opp = game.away
				else:
					opp = game.home

				if p.passing_yds > 300:
					def_cp[unicode(opp)] += 1
					rush_games[p.name] += 1
					
		for team in def_cp: 
			qb.writerow([team,def_cp[team]])
		for player in rush_games:
			qb.writerow([player,rush_games[player]])
		
	
			
			
			
			
			
			
			
def calc_ppcp_WR():
		def_cp = {}
		rush_games = {}
		matchup = {}
	
		week_10 = nflgame.games(2015, week=14)
		for game in week_10:
			
			for p in game.players.receiving().sort("receiving_yds"):
				if p.team == game.home:
					match_opp = game.away
				else:
					match_opp = game.home
				if p.guess_position == 'WR':
					matchup[p.name] = match_opp
			
		
		for game in games:
			def_cp[game.home] = 0
			def_cp[game.away] = 0
			
			for p in game.players.receiving().sort("receiving_yds"):
				rush_games[p.name] = 0
				
		for game in games:



			for p in game.players.receiving().sort("receiving_yds"):


				if p.team == game.home:
					opp = game.away
				else:
					opp = game.home

				if p.receiving_yds > 100:
					def_cp[unicode(opp)] += 1
					rush_games[p.name] += 1
					
		for team in def_cp: 
			wr.writerow([team,def_cp[team]])
		for player in rush_games:
			wr.writerow([player,rush_games[player]])
		
		
calc_ppcp_QB()
calc_ppcp_WR()
calc_ppcp_rb()
