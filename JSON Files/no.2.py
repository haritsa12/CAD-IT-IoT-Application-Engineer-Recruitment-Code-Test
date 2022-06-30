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
output_data = {'array':[
            {
                'day':0,
                "Room": 0,
                "min humidity": 0,
                "max humidity": 0,
                "mmedian humidity": 0,
                "average humidity": 0,
                "min temperature": 0,
                "max temperature": 0,
                "mmedian temperature": 0,
                "average temperature": 0,
            }
        ]
        }
for key_date, value_date in group.items():
    for key_room,value_room in value_date.items():
        print('Day ke :',key_date,'dan Room ke  : ',key_room,)
        min_hum = min(group[day['time_day']][day['roomArea']]['humidity'])
        max_hum = max(value_room['temperature'])
        median_hum = statistics.median(group[day['time_day']][day['roomArea']]['humidity'])
        avg_hum = statistics.mean(group[day['time_day']][day['roomArea']]['humidity'])

        min_temp = min(group[day['time_day']][day['roomArea']]['temperature'])
        max_temp = max(value_room['humidity'])
        median_temp = statistics.median(group[day['time_day']][day['roomArea']]['temperature'])
        avg_temp = statistics.mean(group[day['time_day']][day['roomArea']]['temperature'])
        for day in data['array']:
            day['min humidity'] = min_hum
            day['max humidity'] = max_hum
            day['median humidity'] = median_hum
            day['average humidity'] = avg_hum

            day['min temperature'] = min_temp
            day['max temperature'] = max_temp
            day['median temperature'] = median_temp
            day['average temperature'] = avg_temp
        output_date = {
                'day':key_date,
                "Room": key_room,
                "min humidity": min_hum,
                "max humidity": max_hum,
                "mmedian humidity": median_hum,
                "average humidity": avg_hum,
                "min temperature": min_temp,
                "max temperature": max_temp,
                "mmedian temperature": median_temp,
                "average temperature": avg_temp,
            }
        output_data['array'].append(output_date)

        print('min humidity:',min_hum)
        print('max humidity:',max_hum)
        print('median humidity:',median_hum)
        print('average humidity:',avg_hum,'\n')

        print('min temperature:',min_temp)
        print('max temperature:',max_temp)
        print('median temperature:',median_temp)
        print('average temperature:',avg_temp,'\n')
        print('----------------------------------------')


        json_object_2 = json.dumps(output_data['array'][1:],indent = 4)

        # Writing to .json
        with open("output_2.json", "w") as outfile:
            outfile.write(json_object_2)


json_object = json.dumps(new_list,indent = 4)

# Writing to .json
with open("groupby.json", "w") as outfile:
    outfile.write(json_object)
