from textwrap import indent
import statistics
import json

f = open('sensor_data.json')

data = json.load(f)

def key_func(k):
    return k['roomArea']
def key_func2(k):
    return k['timestamp']

group = {}
 
for day in data['array']:
    day['time_day'] = int(day['timestamp']/86400000)
new_list = sorted(data['array'], key=lambda x: (x['time_day'], x['roomArea'].lower()))

group={}

for day in data['array']:
    if  day['time_day'] not in group.keys():
            group[day['time_day']] = {}
            group[day['time_day']][day['roomArea']] = {
                'time_day':day['time_day'],
                'roomArea': day['roomArea'],
                'humidity':[day['humidity']],
                'temperature' : [day['temperature']]
        }

    else:
        if day['roomArea'] in group[day['time_day']].keys():

            group[day['time_day']][day['roomArea']]['humidity'].append(day['humidity'])
            group[day['time_day']][day['roomArea']]['temperature'].append(day['temperature'])
        else:
            group[day['time_day']][day['roomArea']] = {
                'time_day':day['time_day'],
                'roomArea': day['roomArea'],
                'humidity':[day['humidity']],
                'temperature' : [day['temperature']]
        }

for key_date, value_date in group.items():
    for key_room,value_room in value_date.items():
        print('Day ke :',key_date,'dan Room ke  : ',key_room,)
        min_hum = min(group[day['time_day']][day['roomArea']]['humidity'])
        max_hum = max(value_room['humidity'])
        median_hum = statistics.median(group[day['time_day']][day['roomArea']]['humidity'])
        avg_hum = statistics.mean(group[day['time_day']][day['roomArea']]['humidity'])

        min_temp = min(group[day['time_day']][day['roomArea']]['temperature'])
        max_temp = max(value_room['humidity'])
        median_temp = statistics.median(group[day['time_day']][day['roomArea']]['temperature'])
        avg_temp = statistics.mean(group[day['time_day']][day['roomArea']]['temperature'])

        print('min humidity:',min_hum)
        print('max humidity:',max_hum)
        print('median humidity:',median_hum)
        print('average humidity:',avg_hum,'\n')

        print('min temperature:',min_temp)
        print('max temperature:',max_temp)
        print('median temperature:',median_temp)
        print('average temperature:',avg_temp,'\n')
        print('----------------------------------------')

json_object = json.dumps(new_list,indent = 4)

# Writing to .json
with open("groupby.json", "w") as outfile:
    outfile.write(json_object)