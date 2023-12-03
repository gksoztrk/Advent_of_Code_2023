
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



multiplied_values = []
for i in range(len(games_all)):
    max_value_red = 0
    max_value_blue = 0
    max_value_green = 0
    for j in range(len(games_all[i])):
        dict_set = convert(games_all[i][j])
        for o in range(len(list(dict_set.keys()))):
            value_dict = dict_set.get(list(dict_set.keys())[o])
            if list(dict_set.keys())[o] == 'red':
                if value_dict > max_value_red:
                    max_value_red = value_dict

            elif list(dict_set.keys())[o] == 'blue':
                if value_dict > max_value_blue:
                    max_value_blue = value_dict

            elif list(dict_set.keys())[o] == 'green':
                if value_dict > max_value_green:
                    max_value_green = value_dict

    max_multiply = max_value_red*max_value_blue*max_value_green
    multiplied_values.append(max_multiply)

print (sum(multiplied_values))
