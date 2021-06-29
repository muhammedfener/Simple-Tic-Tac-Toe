def board():
    global user
    print("---------")
    print("| " + user[0] + " " + user[1] + " " + user[2] + " |")
    print("| " + user[3] + " " + user[4] + " " + user[5] + " |")
    print("| " + user[6] + " " + user[7] + " " + user[8] + " |")
    print("---------")

def check():
    global user
    ls = [user[0:3], user[3:6], user[6:9], user[0] + user[3] + user[6], user[1] + user[4] + user[7], user[2]
          + user[5] + user[8], user[0] + user[4] + user[8], user[6] + user[4] + user[2]]

    if ("XXX" in ls and "OOO" in ls) or abs(user.count("X") - user.count("O")) >= 2:
        return "Impossible"
    elif " " not in user and "XXX" not in ls and "OOO" not in ls:
        return "Draw"
    elif "XXX" in ls:
        return "X wins"
    elif "OOO" in ls:
        return "O wins"
    else:
        return True

def coordinate():
    """Look if the input coordinate is valid. No words or number beyond 1 to 3. Enter 2 numbers within from 1 to 3"""
    global num
    global user
    global location
    if num.isalpha():
        print("You should enter numbers!")
        num = input("Enter the coordinates: ").replace(" ", "")
        return coordinate()
    elif num not in all_coordinate:
        print("Coordinates should be from 1 to 3!")
        num = input("Enter the coordinates: ").replace(" ", "")
        return coordinate()
    elif user[all_coordinate.index(num)] != " ":
        print("This cell is occupied! Choose another one!")
        num = input("Enter the coordinates: ").replace(" ", "")
        return coordinate()
    elif num in all_coordinate:
        return True

user = "         "
side = ["X", "O"]
count = 0
board()
while True:
    if count % 2 == 0:
        gameside = side[0]
    else:
        gameside = side[1]
    num = input("Enter the coordinates: ").replace(" ", "")
    all_coordinate = ['11', '12', '13', '21', '22', '23', '31', '32', '33']

    coordinate()
    location = all_coordinate.index(num)
    if coordinate() is True:
        user = user[:location] + user[location].replace(" ", gameside) + user[location + 1:]
    board()
    checkgame = check()
    if checkgame != True:
        print(checkgame)
        break
    count += 1
