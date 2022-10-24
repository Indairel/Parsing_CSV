import csv

html_output = ''
temps = []

with open('weather.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    # print(list(csv_data))

    for line in csv_data:
        temps.append(f"{line[2]} {line[3]}")

for temp in temps:
    print(temp)