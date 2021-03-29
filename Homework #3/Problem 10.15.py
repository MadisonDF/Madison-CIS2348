# Madison Fletcher
# 1868748
class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)


if __name__ == "__main__":
    team = Team()

    name = str(input())
    wins = int(input())
    losses = int(input())

    if wins > losses:
        print("Congratulations, Team", name, "has a winning average!")
    else:
        print("Team", name, "has a losing average.")