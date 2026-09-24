# Store the name of the baseball team
team ="toronto blue jays"

# Store the surrent date 
current_date = "July 18,2021"

# Store the player's name 
player = "vladimir Guerrero Jr."

# Store the number of home runs the player has hit so far 
home_runs_to_date = 31

# Store the number of games already played 
games_played = 88

#Store the total number of games in the season 
total_season_games =162

# Store the current home run record 
home_run_record = 73


# Calulate and store the number of games remaining 
games_remaining = total_season_games - games_played 

# Calculate and store the average number of home runs per hours 
home_runs_per_game = home_runs_to_date / games_played

# Calculate and store the projected number of home runs for the full season 
projected_home_runs = home_runs_per_game * total_season_games

# Calculate and store whether the projected home runs can break the record 
can_break_record = projected_home_runs > home_run_record

print(f"{player}) of the {team}") 
print(f"currently has {home_runs_to_date} home runs as of {current_date}.")
print(f"current MLB record for most home runs in a season is {home_run_record}.")
print(f"with{games_remaining}games remaining and an average of {round(home_runs_per_game, 2)} home runs per game,")
print(f"it is {can_break_record} that he is on pace to break the record.")
print(f"{player} is projected to hit {round(projected_home_runs, 2)}home runs this season.")


# Q.2: the empty lines seperate into sections to make the program easier to read The first group stores the original data, the second group performs calculations,
# and the ast group prints the result
# Q.3 Because the number of games remaining must equal the total number of games in the season minus the number of games already played.