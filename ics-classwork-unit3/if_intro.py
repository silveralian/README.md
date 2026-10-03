robot_location = 40
ball_location = 45
goal_location = 30
have_ball = False

# Q1: An if statement checks a condition.
# If the condition is True, the indented code underneath it runs.

# Q2: Indentation shows which lines belong to the if statement.
# Indented lines are inside the if branch.

if robot_location < ball_location:
    print("Almost at the ball")

if robot_location > goal_location:
    print("You are beyond the goal.")

if robot_location == goal_location:
    print("The robot is at the goal.")

robot_location += 5

if robot_location == goal_location:
    print("At the goal.")

if robot_location == ball_location:
    print("At the ball")
    print("Picking up the ball.")
    have_ball = True
    print("Now make your way to the goal.")

robot_location -= 15

if robot_location < goal_location:
    print("You went too far.")

if robot_location == goal_location and have_ball is True:
    print("You scored a goal!")
    have_ball = False

# Q3:
# I changed the starting locations to:
# robot = 40, ball = 45, goal = 30.
# The program still follows the same path and produces the same results.

# Q4:
# += adds a value to the current value of a variable.
# -= subtracts a value from the current value of a variable.
