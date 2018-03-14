def getcards():
    file = open('cards.txt', 'r')
    for line in file:
        lines = file.readline()
        print(lines)
getcards()
