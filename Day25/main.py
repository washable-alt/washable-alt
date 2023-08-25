#import csv
#
#try:    
#    with open(f".\\Day25\weather_data.csv", 'r') as f:
#        # Use csv library
#        data = csv.reader(f)
#        #print(data)
#        temperatures = []
#        # need to have the list in front so that I can append to temperatures
#        for row in list(data)[1:]:
#            # print row[1]
#            temperatures.append(int(row[1]))
#    print(temperatures)
#    print(type(temperatures))
#    for temperature in temperatures:
#        print(temperature)
#        print(type(temperature))            
#except Exception as e:
#    print(e)

import pandas as pd

PRIMARY_FUR_COLOR = "Primary Fur Color"

try:
# TODO 1:
    data = pd.read_csv(f".\\Day25\weather_data.csv")
    #print(data)
    print(type(data))
    #print(data["temp"])
    print(type(data["temp"]))
    #Convert to a dictionary

    #{'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 
    # 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}
    data_dict = data.to_dict()
    print(data_dict)

    # convert to a list
    temp_list = data["temp"].to_list()

    #[12, 14, 15, 14, 21, 22, 24]
    print(temp_list)

    # <class 'list'>
    print(type(temp_list))

    # print mean function
    print(data["temp"].mean())

    # print max function
    print(data['temp'].max())

    # Get Data in columns
    print(data["condition"])
    print(data.condition)

    # Get Data in Row
    data[data.day == "Monday"]

    print(data[data.day=="Monday"])
    print(data[data.temp == data.temp.max()])

    monday = data[data.day == "Monday"]
    monday_temp = int(monday.temp)
    # change it to Farenheits
    monday_temp_F = monday_temp * 9/5 + 32
    print(monday_temp_F)

    #Create a dataframe 
    data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76,56,65]
    }
    data = pd.DataFrame(data_dict)
    print(data)

    #create new csv file
    data.to_csv(f".\\Day25\\new_data.csv")

    # TODO 2:
    data = pd.read_csv(f".\\Day25\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    grey_squirrels = data[data[PRIMARY_FUR_COLOR]=="Gray"]
    print(grey_squirrels)

    grey_squirrels_count = len(data[data[PRIMARY_FUR_COLOR]=="Gray"])
    brownish_orange_squirrels_count = len(data[data[PRIMARY_FUR_COLOR]=="Cinnamon"])
    black_squirrels_count = len(data[data[PRIMARY_FUR_COLOR]=="Black"])

    print(grey_squirrels_count)
    print(brownish_orange_squirrels_count)
    print(black_squirrels_count)

    data_dict = {
        "Fur Color": ["Gray", "Cinnamon", "Black"],
        "Count": [grey_squirrels_count, brownish_orange_squirrels_count, black_squirrels_count]
    }

    df = pd.DataFrame(data_dict)
    df.to_csv(f".\\Day25\\squirrel_count.csv")

except Exception as e:
    print(e)

