

data = {"Name": ['Clinton', 'Bush', 'Obama', 'Biden'], 
"Terms": [2,2,2,1]}

def years_in_office(dict, multiplier):
    dict["Years"] = list(map(lambda x,y: x*y, dict["Terms"],  multiplier))


multiplier_list = [4,4,4,4]
years_in_office(data, multiplier_list)


