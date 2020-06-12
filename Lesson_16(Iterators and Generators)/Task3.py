class Team:

    def __init__(self, players):
        self.players = players

    def __iter__(self):
        return self

    def __next__(self):

        for player_num in self.players:
            line_up = int(input("Chose the team line-up number. 1 or 2: "))
            if line_up == 1:
                print("You have chosen the first team line_up. Go to the win: ")
                player_num = 0
                while player_num < 11:
                    player_num += 1
                    print(player_num, "-", self.players[player_num])
            elif line_up == 2:
                print("You have chosen the second team line_up. Fight for the honor: ")
                player_num = 11
                while player_num != 22:
                    player_num += 1
                    print(player_num, "-", self.players[player_num])
        return self.players

    def __setitem__(self, player_num, data):
        self.players[player_num] = data

    def __getitem__(self, player_num):
        return self.players[player_num]

    def __delete__(self, player_num):
        print("Delete this player")
        self.players[player_num] = None



structure = {1: "Goalkeeper", 2: "Sweeper", 3: "Centr_back", 4: "Centr_back", 5: "Wing_back",
             6: "Wing_back (C)", 7: "Centr_midfield", 8: "Centr_midfield", 9: "Centr_midfield", 10: "Forward", 11: "Forward",
             12: "Goalkeeper", 13: "Sweeper", 14: "Centr_back", 15: "Centr_back", 16: "Wing_back",
             17: "Wing_back", 18: "Centr_midfield", 19: "Centr_midfield (C)", 20: "Centr_midfield", 21: "Forward",
             22: "Forward"}

herenven = Team(structure)
# for player in herenven:
#     print(player)

herenven[1] = "refery"

print(structure)