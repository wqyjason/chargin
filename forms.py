from wtforms import Form, StringField, SelectField

class SearchForm(Form):
    choices = [('sexual offense', 'sexual offense'),
               ('robbery', 'robbery'),
               ('assault', 'assault')]
    select = SelectField('Criminal you wish to avoid:', choices=choices)
    start = StringField('')
    dest  = StringField('')
