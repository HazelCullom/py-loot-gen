
import json, sys

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

Pistol Grip Stats = {"Bandit": {"Stats": {"Mag Size": (MUL, 1.35), "Reload Time": (MUL, 1.1), "Weapon Spread": (MUL,1.15)}, "Matching": {"Bandit": {"Mag Size": (ADD,4), "Reload Time": (DIV, 1.3)}}}}

pg_stats["Bandit"]["Stats"] == {"Mag Size": (MUL, 1.35), "Reload Time": (MUL, 1.1), "Weapon Spread": (MUL,1.15)}
pg_stats["Bandit"]["Matching"] == {"Bandit": {"Mag Size": (ADD,4), "Reload Time": (DIV, 1.3)}}

pistol = ["Grip": "Bandit", "Body": "Dahl", "Rarity": "Rare", "Barrel": "Torgue", "Accessories": [], "Sight": ""]

stats that say "On Zoom" will just add Zoom to the stat name:
ex) 
    On Zoom
    +3 Movement Speed
becomes:
    "Zoom Movement Speed": (ADD, 3)

ex2) 
    On Dahl + Zoom
    +2 Burst Count
becomes:
    {"Matching": {"Dahl": {"Zoom Burst Count": (ADD, 2), ...}}

"""

if len(sys.argv) <= 1:
    print("ERROR: missing input file argument")
    print("Usage: python ./"+__file__.split('\\')[-1].split('/')[-1]+" input_file.txt")
    exit()

READ_FILE = sys.argv[1]
WRITE_FILE = READ_FILE[:-4] + "_stats.json"

operators = ['*', '/', '+', '-', '×', '÷', '−']
operator_match = {'*': "MUL", '/': "DIV", '+': "ADD", '-': "SUB", '×': "MUL", '÷': "DIV", '−': "SUB"}

print("Reading data from:", READ_FILE)
file_str = open(READ_FILE, "r", encoding='utf-8').read()

split_str = file_str.split(',')

stat_obj = {}

for stats in split_str:
    stats = stats.strip().split('\n')

    manufacturer = stats[0]

    stat_obj[manufacturer] = {"Stats": {}, "Matching": {}}

    stat_mode = "Stats"

    for line in stats[1:]:
        if line[0] in operators and len(line) > 1:

            true_stat_mode = stat_mode
            stat_num, stat = line[1:].split(' ', 1)
            operator = operator_match[line[0]]

            if "%" in stat_num:
                # convert % to mult
                stat_num = (float(stat_num[:-1]) / 100)
                if operator == "SUB":
                    stat_num *= -1
                stat_num = 1 + stat_num
                operator = "MUL"
                pass

            if "Zoom" in true_stat_mode:
                true_stat_mode = true_stat_mode[4:]
                stat = "Zoom " + stat

            if "Matching" in true_stat_mode:
                match_manufac = true_stat_mode[8:]
                if not match_manufac in stat_obj[manufacturer]["Matching"]:
                    stat_obj[manufacturer]["Matching"][match_manufac] = {}
                stat_obj[manufacturer]["Matching"][match_manufac][stat] = (operator, float(stat_num))
            else:
                stat_obj[manufacturer]["Stats"][stat] = (operator, float(stat_num))

        elif "on zoom" in line.lower():
            stat_mode = "ZoomStats"
        
        elif "on dahl + zoom" in line.lower():
            stat_mode = "ZoomMatchingDahl"
        
        elif "on" in line[:3].lower():
            # line is "On ___" where ___ is the manufacturer
            stat_mode = "Matching" + line[3:-1]
        


#print("Grip Modifiers:\n", json.dumps(stat_obj, indent=2), end="\n\n")
print("Done, exporting to:", WRITE_FILE)
with open(WRITE_FILE, 'w') as file:
    json.dump(stat_obj, file, indent=2)