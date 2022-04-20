

data = {"Name": ['Clinton', 'Bush', 'Obama', 'Biden'], 
"Terms": [2,2,2,1]}

def years_in_office(dict, multiplier):
    dict["Years"] = dict["Terms"]*multiplier


multiplier_list = [4,'4']

for mult in multiplier_list:
    years_in_office(data, mult)