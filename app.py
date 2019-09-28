from flask import Flask, request, render_template
from forms import SearchForm
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import csv
from collections import defaultdict

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



@app.route('/', methods=['GET', 'POST'])
def hello():

    mymap = Map(
        identifier="view-side",  # for DOM element
        varname="mymap",  # for JS object name
        lat=40.110588,
        lng=-88.20727,
        markers=data_map['latlng']
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
