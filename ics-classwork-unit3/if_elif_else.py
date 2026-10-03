team_a_points = 25
team_a_wins = 15

team_b_points = 20
team_b_wins = 16

if team_a_points > team_b_points:
    print("Team A wins!")
    team_a_wins += 1
elif team_b_points > team_a_points:
    print("Team B wins!")
    team_b_wins += 1
else:
    print("Tie.")

if team_a_wins > team_b_wins:
    print("Team A has more wins than Team B.")
elif team_b_wins > team_a_wins:
    print("Team B has more wins than Team A.")
else:
    print("Both Teams A and B have the same number of wins.")


# Q1:
# Team A starts with 15 wins and Team B starts with 16 wins.
# Team A wins this game, so team_a_wins increases by 1.
# Team A becomes 16 wins, so both teams now have 16 wins.

# Q2:
# elif checks another condition if the previous if condition was False.
# else runs when none of the previous if or elif conditions are True.

# Q3:
# If I change an elif to if, it becomes a separate condition.
# Python will check it even if the previous if condition was True.
# With elif, Python only checks it if the previous condition was False.
