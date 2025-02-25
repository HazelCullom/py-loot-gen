
import json

"""
Convert:

Bandit
Bandit Mesh
*1.35 Mag Size
*1.1 Reload Time
*1.15 Weapon Spread
On Bandit:
+4 Mag Size
/1.3 Reload Time

To: 

Pistol Grip Stats = {"Bandit": {"Mag Size": (MUL, 1.35), "Reload Time": (MUL, 1.1), "Weapon Spread": (MUL,1.15)}}
Pistol Grip Match Bonus = {"Bandit": {"Mag Size": (ADD,4), "Reload Time": (DIV, 1.3)}}

"""

operators = ['*', '/', '+', '-', '×', '÷', '−']
operator_match = {'*': "MUL", '/': "DIV", '+': "ADD", '-': "SUB", '×': "MUL", '÷': "DIV", '−': "SUB"}

file_str = open("pistol_grips.txt", "r").read()

split_str = file_str.split(',')

stat_obj = {}
match_bonus_obj = {}
stat_str = "{"
bonus_str = "{"

for stats in split_str:
    stats = stats.strip().split('\n')

    manufacturer = stats[0]

    stat_obj[manufacturer] = {}
    match_bonus_obj[manufacturer] = {}
    stat_str += "\"" + manufacturer + "\": {"
    bonus_str += "\"" + manufacturer + "\": {"


    matching_bonus = False

    for line in stats[2:]:
        if line[0] in operators:

            # if we are in grip stat
            if not matching_bonus:
                stat_num, stat = line[1:].split(' ', 1)
                stat_obj[manufacturer][stat] = (operator_match[line[0]], float(stat_num))
                stat_str += "\"" + stat + "\": (" + operator_match[line[0]] + ", " + stat_num + "), "

            # else if we are in matching grip bonus
            else:
                stat_num, stat = line[1:].split(' ', 1)
                match_bonus_obj[manufacturer][stat] = (operator_match[line[0]], float(stat_num))
                bonus_str += "\"" + stat + "\": (" + operator_match[line[0]] + ", " + stat_num + "), "
                pass

        elif not matching_bonus:
            # we are now on matching bonus
            matching_bonus = True
            stat_str = stat_str[:-2] + "}, \n"
    
    bonus_str = bonus_str[:-2] + "}, \n"

stat_str = stat_str[:-3] + "}"
bonus_str = bonus_str[:-3] + "}"
print("Grip Modifiers:\n", stat_str, end="\n\n")
print("Grip Bonus Modifiers:\n", bonus_str, end="\n\n")

print("Grip Modifiers:\n", json.dumps(stat_obj, indent=2), end="\n\n")

with open("pistol_grip_stats.json", 'w') as file:
    json.dump(stat_obj, file, indent=2)