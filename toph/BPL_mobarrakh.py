t = int(input())

for _ in range(t):
    string = input()
    ballCount = 0
    for i in string:
        if i == 'N'or i == 'W' or i == 'D':
            continue
        else:
            ballCount += 1
    over = int(ballCount / 6)
    ball = ballCount%6
    if over == 0 and ball !=0:
        if ball > 1:
            output = "BALLS"
        else:
            output = "BALL"
        print("{} {}".format(ball, output))
    elif over != 0 and ball == 0:
        if over > 1:
            output = "OVERS"
        else:
            output = "OVER"
        print("{} {}".format(over, output))
    else:
        if over > 1:
            output_over = "OVERS"
        else:
            output_over = "OVER"
        if ball > 1:
            output_ball = "BALLS"
        else:
            output_ball = "BALL"
        print("{} {} {} {}".format(over, output_over, ball, output_ball))