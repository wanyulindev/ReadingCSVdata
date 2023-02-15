# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)


# import csv
#
# with open ("weather_data.csv") as file:
#     data = csv.reader(file)
#     # print(data)
#     temperatures = []
#     for data in data:
#         # print(data)
#         if data[1] != "temp":
#             temperatures.append(int(data[1]))
#     print(temperatures)


# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data["temp"]))
# print(type(data))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(type(temp_list[1]))
# temp_sum = 0
# for temp in temp_list:
#     temp_sum += temp
# avg_tmep = temp_sum / len(temp_list)
# # print(len(temp_list))
# print(int(avg_tmep))


# print(int(sum(temp_list) / len(temp_list)))

# max_temp = data["temp"].max
# d = data["temp"]
# print(data["temp"])

# print(data["temp"].max())

# max_temp = data.temp.max()
# print(data[data.temp == max_temp])

#
# monday = data[data.day == "Monday"]
# # print(type(int(monday.temp)))
#
# print(((int(monday.temp)) * 9/5) + 32)


# data_dict = {
#     "char": ["Long", "Nina", "Din"],
#     "sq": [1700, 2000, 1750],
#     "shot": [20, 40, 60]
# }
#
# info = pandas.DataFrame(data_dict)
# # print(info)
# info.to_csv("info.csv")


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data)
# print(type(data["Primary Fur Color"]))

gray = len(data[data["Primary Fur Color"] == "Gray"])
# print(gray)
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
# print(cinnamon)
black = len(data[data["Primary Fur Color"] == "Black"])
# print(black)

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray, cinnamon, black]
}
info = pandas.DataFrame(data_dict)
print(info)
info.to_csv("sq_info.csv")
