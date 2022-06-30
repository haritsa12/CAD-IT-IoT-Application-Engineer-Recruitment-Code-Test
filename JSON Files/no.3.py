import json
import random
import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from statistics import mean
import statistics

# Data to be written
gen_data ={ 'array':[
    {
    "temperature": 0,
      "humidity": 0,
      "roomArea": "roomArea1",
      "timestamp": 1593666000000,
      "time_day": 1593666000000
        }
    ]
}

def rand_humidity():
    return random.uniform(80, 90)


def rand_temperature():
    return random.uniform(15, 30)

plt.rcParams.update({'font.size': 7})

fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
graph_time = []
live_humidity = []
avg_humidity = []
min_humidity = []
max_humidity = []
median_humidity = []

live_temperature = []
avg_temperature = []
min_temperature = []
max_temperature = []
median_temperature = []

def animate(i, graph_time, live_humidity, avg_humidity, max_humidity, min_humidity, median_humidity, live_temperature, avg_temperature, max_temperature, min_temperature, median_temperature):
    
    object_to_append =   {
    "temperature": rand_temperature(),
      "humidity": rand_humidity(),
      "roomArea": "roomArea1",
      "timestamp": str(datetime.datetime.now())[:len(str(datetime.datetime.now()))-7],
      "time_day": datetime.datetime.now().timestamp()
        }

    gen_data['array'].append(object_to_append)

    json_object = json.dumps(gen_data, indent = 4)
  
# Writing to sample.json
    with open("no_3_json.json", "w") as outfile:
        outfile.write(json_object)
     
    humidity = gen_data['array'][-1]['humidity']
    temp = gen_data['array'][-1]['temperature']


    # Add x and y to lists
    live_humidity.append(humidity)
    avg_humidity.append(mean(live_humidity))
    min_humidity.append(min(live_humidity))
    max_humidity.append(max(live_humidity))
    median_humidity.append(statistics.median((live_humidity)))

    live_temperature.append(temp)
    avg_temperature.append(mean(live_temperature))
    min_temperature.append(min(live_temperature))
    max_temperature.append(max(live_temperature))
    median_temperature.append(statistics.median((live_temperature)))

    graph_time.append(datetime.datetime.now().strftime('%H:%M:%S'))
    
    graph_time = graph_time[-20:]
    live_humidity = live_humidity[-20:]
    avg_humidity = avg_humidity[-20:]
    min_humidity = min_humidity[-20:]
    max_humidity = max_humidity[-20:]
    median_humidity = median_humidity[-20:]

    live_temperature = live_temperature[-20:]
    avg_temperature = avg_temperature[-20:]
    min_temperature = min_temperature[-20:]
    max_temperature = max_temperature[-20:]
    median_temperature = median_temperature[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(graph_time, live_humidity, color = 'blue', label = 'live_humidity : '+str(live_humidity[-1]))
    ax.title.set_text('Humidity over Time')
    ax.set_xlabel('Time')
    ax.set_ylabel('Humidity')
    ax.plot(graph_time, avg_humidity, color = 'yellow', label = 'avg_humidity : '+str(avg_humidity[-1]))
    ax.plot(graph_time, min_humidity, color = 'green', label ='min_humidity : '+str(min_humidity[-1]) )
    ax.plot(graph_time, max_humidity, color = 'purple', label = 'max_humidity : ' + str(max_humidity[-1]) )
    ax.plot(graph_time, median_humidity, color = 'orange', label = 'median_humidity : ' + str(median_humidity[-1]))
    ax.legend(bbox_to_anchor=(0.4, 0.2),bbox_transform=fig.transFigure)
    ax.grid()
    
    ax2.clear()
    ax2.plot(graph_time, live_temperature, color = 'red', label = 'live_temperature : '+ str(live_temperature[-1]))
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Temperature')
    ax2.title.set_text('Temperature over Time')
    ax2.plot(graph_time, avg_temperature, color = 'yellow', label = 'avg_temperature : '+ str(avg_temperature[-1]))
    ax2.plot(graph_time, min_temperature, color = 'green', label = 'min_temperature : '+ str(min_temperature[-1]))
    ax2.plot(graph_time, max_temperature, color = 'purple', label = 'max_temperature : '+ str(max_temperature[-1]))
    ax2.plot(graph_time, median_temperature, color = 'orange', label = 'median_temperature : '+ str(median_temperature[-1]))
    ax2.legend(bbox_to_anchor=(0.87, 0.2),bbox_transform=fig.transFigure)    
    ax2.grid()

    plt.subplots_adjust(bottom=0.30)

ani = animation.FuncAnimation(fig, animate, fargs=(graph_time, live_humidity, avg_humidity, max_humidity, min_humidity, median_humidity, live_temperature, avg_temperature, min_temperature, max_temperature, median_temperature), interval=2000)

plt.show()


