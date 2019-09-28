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

def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

apt_locations = [(40.1165, -88.2295), (40.1094, -88.2348), (40.110532, -88.233987), (40.110203, -88.231651), (40.316541, -88.351220)]
danger = [0, 0, 0, 0, 0]
for crime in data_map['latlng']:
    lat = apt_locations[0]
    t3 = apt_locations[1]
    here = apt_locations[2]
    skyline = apt_locations[3]
    octave = apt_locations[4]
    if distance(lat, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[0] += 1
    if distance(t3, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[1] += 1
    if distance(here, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[2] += 1
    if distance(skyline, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[3] += 1
    if distance(octave, (float(crime[0]), float(crime[1]))) < 0.01:
        danger[4] += 1
print(danger)

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
    return render_template('index.html', form = input, mymap=mymap)

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
