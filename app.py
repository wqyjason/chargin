from flask import Flask, request, render_template
from forms import SearchForm
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import csv
from collections import defaultdict
import math

app = Flask(__name__)
GoogleMaps(app, key="AIzaSyCSkHsXrtRhNDd-5pn0aLk4l7HjsNUtdQY")

with open('./data2.csv') as csvfile:
    readCsv = csv.reader(csvfile, delimiter=',')
    data_map = defaultdict(list)
    for row in list(readCsv)[1:]:
        data_map["id"].append(row[0])
        data_map["date"].append(row[1])
        data_map["time"].append(row[2])
        data_map["geo_code"].append(row[3])
        data_map["crime_category"].append(row[4])
        data_map["address"].append(row[5])
        data_map['latlng'].append((row[len(row) - 2], row[len(row) - 1]))

with open('./data3.csv') as csvfile:
    readCsv = csv.reader(csvfile, delimiter=',')
    data_map1 = defaultdict(list)
    for row in list(readCsv)[1:]:
        data_map1["id"].append(row[0])
        data_map1["date"].append(row[1])
        data_map1["time"].append(row[2])
        data_map1["geo_code"].append(row[3])
        data_map1["crime_category"].append(row[4])
        data_map1["address"].append(row[5])
        data_map1['latlng'].append((row[len(row) - 2], row[len(row) - 1]))

with open('./data4.csv') as csvfile:
    readCsv = csv.reader(csvfile, delimiter=',')
    data_map2 = defaultdict(list)
    for row in list(readCsv)[1:]:
        data_map2["id"].append(row[0])
        data_map2["date"].append(row[1])
        data_map2["time"].append(row[2])
        data_map2["geo_code"].append(row[3])
        data_map2["crime_category"].append(row[4])
        data_map2["address"].append(row[5])
        data_map2['latlng'].append((row[len(row) - 2], row[len(row) - 1]))

with open('./data5.csv') as csvfile:
    readCsv = csv.reader(csvfile, delimiter=',')
    data_map3 = defaultdict(list)
    for row in list(readCsv)[1:]:
        data_map3["id"].append(row[0])
        data_map3["date"].append(row[1])
        data_map3["time"].append(row[2])
        data_map3["geo_code"].append(row[3])
        data_map3["crime_category"].append(row[4])
        data_map3["address"].append(row[5])
        data_map3['latlng'].append((row[len(row) - 2], row[len(row) - 1]))

with open('./data6.csv') as csvfile:
    readCsv = csv.reader(csvfile, delimiter=',')
    data_map4 = defaultdict(list)
    for row in list(readCsv)[1:]:
        data_map4["id"].append(row[0])
        data_map4["date"].append(row[1])
        data_map4["time"].append(row[2])
        data_map4["geo_code"].append(row[3])
        data_map4["crime_category"].append(row[4])
        data_map4["address"].append(row[5])
        data_map4['latlng'].append((row[len(row) - 2], row[len(row) - 1]))

with open('./data7.csv') as csvfile:
    readCsv = csv.reader(csvfile, delimiter=',')
    data_map5 = defaultdict(list)
    for row in list(readCsv)[1:]:
        data_map5["id"].append(row[0])
        data_map5["date"].append(row[1])
        data_map5["time"].append(row[2])
        data_map5["geo_code"].append(row[3])
        data_map5["crime_category"].append(row[4])
        data_map5["address"].append(row[5])
        data_map5['latlng'].append((row[len(row) - 2], row[len(row) - 1]))


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

apt_locations = [(40.1165, -88.2295), (40.1094, -88.2348), (40.110532, -88.233987), (40.110203, -88.231651), (40.116890, -88.222130)]
danger = [[0 for i in range(5)] for j in range(6)]
for crime in data_map['latlng']:
    lat = apt_locations[0]
    t3 = apt_locations[1]
    here = apt_locations[2]
    skyline = apt_locations[3]
    octave = apt_locations[4]
    if distance(lat, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[0][0] += 1
    if distance(t3, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[0][1] += 1
    if distance(here, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[0][2] += 1
    if distance(skyline, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[0][3] += 1
    if distance(octave, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[0][4] += 1
print(danger[0])

for crime in data_map1['latlng']:
    lat = apt_locations[0]
    t3 = apt_locations[1]
    here = apt_locations[2]
    skyline = apt_locations[3]
    octave = apt_locations[4]
    if distance(lat, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[1][0] += 1
    if distance(t3, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[1][1] += 1
    if distance(here, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[1][2] += 1
    if distance(skyline, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[1][3] += 1
    if distance(octave, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[1][4] += 1
print(danger[1])

for crime in data_map2['latlng']:
    lat = apt_locations[0]
    t3 = apt_locations[1]
    here = apt_locations[2]
    skyline = apt_locations[3]
    octave = apt_locations[4]
    if distance(lat, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[2][0] += 1
    if distance(t3, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[2][1] += 1
    if distance(here, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[2][2] += 1
    if distance(skyline, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[2][3] += 1
    if distance(octave, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[2][4] += 1
print(danger[2])

for crime in data_map3['latlng']:
    lat = apt_locations[0]
    t3 = apt_locations[1]
    here = apt_locations[2]
    skyline = apt_locations[3]
    octave = apt_locations[4]
    if distance(lat, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[3][0] += 1
    if distance(t3, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[3][1] += 1
    if distance(here, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[3][2] += 1
    if distance(skyline, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[3][3] += 1
    if distance(octave, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[3][4] += 1
print(danger[3])

for crime in data_map4['latlng']:
    lat = apt_locations[0]
    t3 = apt_locations[1]
    here = apt_locations[2]
    skyline = apt_locations[3]
    octave = apt_locations[4]
    if distance(lat, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[4][0] += 1
    if distance(t3, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[4][1] += 1
    if distance(here, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[4][2] += 1
    if distance(skyline, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[4][3] += 1
    if distance(octave, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[4][4] += 1
print(danger[4])

for crime in data_map5['latlng']:
    lat = apt_locations[0]
    t3 = apt_locations[1]
    here = apt_locations[2]
    skyline = apt_locations[3]
    octave = apt_locations[4]
    if distance(lat, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[5][0] += 1
    if distance(t3, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[5][1] += 1
    if distance(here, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[5][2] += 1
    if distance(skyline, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[5][3] += 1
    if distance(octave, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[5][4] += 1
print(danger[5])

@app.route('/', methods=['GET', 'POST'])
def hello():

    mymap = Map(
        identifier="view-side",  # for DOM element
        varname="mymap",  # for JS object name
        lat=40.110588,
        lng=-88.20727,
        markers=data_map['latlng'],
        style='height:500px;width:1200px;margin:0;',
        zoom=16,
    )


    input = SearchForm(request.form)
    if request.method == 'POST':
        if "Visualization" in request.form:
            return visual()
        else:
            return results(input)
    return render_template('index.html', form = input, mymap=mymap, danger=danger)

@app.route('/results')
def results(input):
    select = input.data['select']
    start = input.data['start']
    dest  = input.data['dest']
    return render_template('result.html', start=start, dest=dest, name=select)

@app.route('/visualization')
def visual():
    return render_template('visual.html')






if __name__ == '__main__':
    app.run(debug = True)
