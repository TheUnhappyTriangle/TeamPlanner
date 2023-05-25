import os

def create_pkmn_folders(root_dir, num_pkmn, game_array):
    for i in range(num_pkmn):
        dexnum = i+1

        dir_name = f"{dexnum}"
        dir_path = os.path.join(root_dir, dir_name)
        os.makedirs(dir_path)
        print(dir_path)
        for idx, games in enumerate(game_array):
            if dexnum > 151 and idx < 3:
                continue
            elif dexnum > 251 and idx < 6:
                continue
            elif dexnum > 386 and idx < 9:
                continue
            elif dexnum > 493 and idx < 12:
                continue
            elif dexnum > 649 and idx < 13:
                continue
            else:
                subdir_name = f"{games}"
                subdir_path = os.path.join(dir_path, subdir_name)
                #os.makedirs(subdir_path)
                #print(subdir_path)
        
root = ".\\teamplanner\\src\\assets\\images\\sprites\\"
total_pkmn = 1010
games = ["RedGreen", "RedBlue", "Yellow", "Gold", "Silver", "Crystal", "RubySapphire", "FireRedLeafGreen", "Emerald", "DiamondPearl", "Platinum", "HeartGoldSoulSilver", "Gen5", "3DS", "PKMNGO", "HOME"]
create_pkmn_folders(root, total_pkmn, games)