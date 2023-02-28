import pdb
from collections import Counter

teamA = ['kohli', 'dhoni', 'ashwin', 'pujara', 'smith']
teamB = ['gilchrist', 'sachin', 'dravid', 'smith', 'kohli']
player_in_both = []
player = str(input("Enter player to trasnfer: "))

def check_teams(player):
    pdb.set_trace()
    # zip_team = list(zip(teamA, teamB))
    # count_zip_team = Counter(zip_team)
    # print(count_zip_team)

    join_team = teamA + teamB
    print(Counter(join_team))
    print(join_team)

    try:
        if player in teamA and player in teamB:
            print("Player Found")
            # if Counter(join_team) > 2:
            #     player_in_both.append(player)
            #     print("Players play for both teams transfered to teamC", player_in_both)
            for i in join_team:
                if join_team.count(i) > 1:
                    if i not in player_in_both:
                        player_in_both.append(player)
                        print("Players play for both teams transfered to teamC", player_in_both)
                        break
        else:
            print("Player not found")
    except:
        raise ValueError("Player is not a string")

check = check_teams(player)
print(player_in_both)
    
# countTeamA = Counter(teamA)
# countTeamB = Counter(teamB)

# zip_team= dict(zip(countTeamA, countTeamB))
# print(zip_team)

