import json

with open('Task_7.txt', 'r') as f:
    data = list(map(lambda a: a.split(), f.readlines()))
    profit = {comp[0]: int(comp[3]) - int(comp[2]) for comp in data if int(comp[3]) - int(comp[2]) > 0}
    profit['average'] = sum([int(comp[3]) for comp in data])/len(data)

with open('Task_7.json', 'w') as js:
    json.dump(profit, js, indent=4)
