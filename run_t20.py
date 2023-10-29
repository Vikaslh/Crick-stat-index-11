from batsman_t20 import best_batsmen
from bowler_t20 import best_bowler
from keeper_t20 import best_keeper


# def select_player(batsmen_no, bowler_no, keeper_no):
#     # TODO: figure out another method for selecting players.
#     players = []
#     i = 1
#     while i in range(1, batsmen_no+1):
#         temp = best_batsmen['Player Name'].sample().tolist()
#         #! Dont forget temp[0] because temp itself is a list.
#         if not temp[0] in players:  # check for duplicates...
#             players.append(temp[0])
#             i += 1
#     i = 1
#     while i in range(1, bowler_no+1):
#         temp = best_bowler['Player Name'].sample().tolist()
#         if not temp[0] in players:  # check for duplicates...
#             players.append(temp[0])
#             i += 1
#     i = 1
#     while i in range(1, keeper_no+1):
#         temp = best_keeper['Player Name'].sample().tolist()
#         if not temp[0] in players:  # check for duplicates...
#             players.append(temp[0])
#             i += 1
#     return players

def select_player(batsmen_no, bowler_no, keeper_no):
    players = []
    for i in range(0, batsmen_no):
        temp = best_batsmen['Player Name'].tolist()
        players.append(temp[i])
    for i in range(0, bowler_no):
        temp = best_bowler['Player Name'].tolist()
        players.append(temp[i])
    for i in range(0, keeper_no):
        temp = best_keeper['Player Name'].tolist()
        players.append(temp[i])
    return players


player = select_player(4, 4, 3)
print(player)
