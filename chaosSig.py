def chaos():
    x = .3
    for i in range(100000000):
        x = 3.9 * x * (1 - x)
        print(x)
