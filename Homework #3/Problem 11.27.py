# Madison Fletcher
# 1868748
def print_menu():
    print("MENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating"
          "\no - Output roster\nq - Quit\n")
    user_input = input('Choose an option:\n')
    return user_input


def original_players():
    for x in range(5):
        jersey = int(input("Enter player {}'s jersey number:\n".format(x + 1)))
        rating = int(input("Enter player {}'s rating:\n\n".format(x + 1)))
        player[jersey] = rating


def output_roster():
    print("ROSTER")
    sorted_list = []
    for y in player.keys():
        sorted_list.append(y)
    sorted_list.sort()
    for z in sorted_list:
        print("Jersey number: {}, Rating: {}".format(z, player[z]))


def a():
    new = int(input())
    new_rating = int(input())
    if new not in player:
        player[new] = new_rating


def d():
    delete = int(input())
    if delete in player:
        del player[delete]


def u():
    update_player = int(input())
    if update_player in player:
        update_rating = int(input())
        player[update_player] = update_rating


def r():
    rate = int(input())
    sorted_list = []
    for y in player.keys():
        sorted_list.append(y)
    sorted_list.sort()
    print("ABOVE {}".format(rate))
    for b in sorted_list:
        if player[b] > rate:
            print("Jersey number: {}, Rating: {}".format(b, player[b]))


player = {}
original_players()
output_roster()
print()

while True:
    user = print_menu()
    if user == 'a':
        a()
    elif user == 'd':
        d()
    elif user == 'u':
        u()
    elif user == 'r':
        r()
        print()
    elif user == 'o':
        output_roster()
        print()
    elif user == 'q':
        exit()
