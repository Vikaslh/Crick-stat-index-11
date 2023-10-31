from bat import best_batsman
from finalbowl import best_bowler
from finalar import best_allrounder

def select_player(batsmen_no, bowler_no, ar_no):
    players = []
    i = 0
    while i in range(0, batsmen_no):
        temp = best_batsman['Player'].tolist()
        if not temp[i] in players:  # check for duplicates...
            players.append(temp[i])
            i+=1
    i = 0
    while i in range(0, bowler_no):
        temp = best_bowler['Player'].tolist()
        if not temp[i] in players:  # check for duplicates...
            players.append(temp[i])
            i+=1
    i = 0
    while i in range(0, ar_no):
        temp = best_allrounder['Player'].sample().tolist()
        if not temp[0] in players:  # check for duplicates...
            players.append(temp[0])
            i+=1
    i = 0
    return players


player = select_player(4,4,3)
print(player)