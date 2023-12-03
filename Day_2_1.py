#12 red cubes, 13 green cubes, and 14 blue cubes
color_dict={
    'red': 12,
    'blue': 14,
    'green': 13
}

games = open(r"C:\Users\Goksu Ozturk\Documents\Python Scripts\github\data\Day2.txt").read()

games = games.split('\n')

for i in range(len(games)):
    games[i] = games[i].lstrip().split(': ')[1]


game_round=[]
for i in range(len(games)):
    round = games[i].split('; ')
    game_round.append(round)

games_list=[]
for i in range(len(game_round)):
    games_l = []
    for j in range(len(game_round[i])):
        games_l.append(game_round[i][j].split(', '))
    games_list.append(games_l)  

games_all = []
for i in range(len(games_list)):
    games_turn = []
    for j in range(len(games_list[i])): 
        game_set = []
        for k in range(len(games_list[i][j])):
            spr = games_list[i][j][k].split(' ')
            value_ = int(spr[0])
            key_ = spr[1]
            game_set.append(value_)   
            game_set.append(key_) 
        games_turn.append(game_set) 
    games_all.append(games_turn) 


def convert(lst):
   res_dict = {}
   for i in range(0, len(lst), 2):
       res_dict[lst[i+1]] = lst[i]
   return res_dict


games_sum = 0
for i in range(len(games_all)):
    set_game = 0
    for j in range(len(games_all[i])):
        dict_set = convert(games_all[i][j])
        set_ = 0
        for o in range(len(list(dict_set.keys()))):
            value_dict = dict_set.get(list(dict_set.keys())[o])
            value_color = color_dict.get(list(dict_set.keys())[o])
            if value_dict <= value_color:
                set_ = set_ + 1
        
        if set_ == len(list(dict_set.keys())):
            set_game = set_game + 1

    if set_game == len(games_all[i]):
        games_sum = games_sum+i+1


print(games_sum)