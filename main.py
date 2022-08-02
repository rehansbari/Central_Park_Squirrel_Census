import csv
import pandas

#Create a CSV which only contains only fur color and count
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])

#Creating a new data frame in order to create the new csv file
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}

#Creating the csv file
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")


