from flask import Flask, request, render_template
from forms import SearchForm
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    input = SearchForm(request.form)
    if request.method == 'POST':
        if "Visualization" in request.form:
            return visual()
        else:
            return results(input)
    return render_template('index.html', form = input)

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
