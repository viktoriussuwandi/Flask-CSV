from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import csv
from flask_wtf import FlaskForm
from wtforms import StringField, TimeField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL

# ---------------------------------------------------------------------------------------
# FORM VALIDATION
# ---------------------------------------------------------------------------------------

class AddForm(FlaskForm) :
  
  name     = StringField( label="name", validators=[ DataRequired() ] )
  location = StringField( label="location", validators=[ DataRequired(), URL() ] )
  
  open     = TimeField( label="open", validators=[ DataRequired() ],
                        format='%H:%M:%S', render_kw={"step": "1"} )
  close    = TimeField( label="close", validators=[ DataRequired() ],
                        format='%H:%M:%S', render_kw={"step": "1"} )

  list     = {
    "coffee" : ['✘','☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'],
    "wifi"   : ['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'],
    "power"  : ['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']
  }
  coffee   = SelectField( label="coffee", choices = list["coffee"],
                          validators=[ DataRequired() ] )
  wifi     = SelectField( label="wifi", choices = list["wifi"], 
                           validators=[ DataRequired() ] )
  power    = SelectField( label="power", choices = list["power"], 
                           validators=[ DataRequired() ] )
  
  submit   = SubmitField( label= "Submit")
  pass
  
# ---------------------------------------------------------------------------------------
# FLASK APP
# ---------------------------------------------------------------------------------------

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# ---------------------------------------------------------------------------------------
# ADD NEW CAFE
# ---------------------------------------------------------------------------------------

@app.route("/add", methods = [ "GET", "POST" ] )
def add() :
  add_form = AddForm()
  if add_form.validate_on_submit() :
    registration_data = {
      'name'     : add_form.name.data,
      'location' : add_form.location.data,
      'open'     : add_form.open.data,
      'close'    : add_form.close.data,
      'coffee'   : add_form.coffee.data,
      'wifi'     : add_form.wifi.data,
      'power'    : add_form.power.data
    }
    # Add to CSV  
    return f'<h1> Registration Successfull </h1>\n{registration_data}'
  # else : return '<h1> Registration Failed </h1>'
  return render_template("add.html", form = add_form)

# ---------------------------------------------------------------------------------------
# ALL CAFE
# ---------------------------------------------------------------------------------------
@app.route("/cafes")
def cafes() :
  with open ('cafe-data.csv',newline='') as f :
    file      = csv.reader(f, delimiter = ",")
    file_data = [row for row in file]
  return render_template( "cafes.html", cafes = file_data )

# ---------------------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------------------
@app.route("/")
def home() :
  return render_template("index.html")

# ---------------------------------------------------------------------------------------
# HOST-PORT
# ---------------------------------------------------------------------------------------
if __name__ == "__main__" :
  app.run(debug=True, host="0.0.0.0", port=2000)

# Convert csv data to json format
# rows = len(file_arr) # 5 rows
# cols = len( list(csv_data.keys()) ) # 7 columns
# csv_data = {}
# for c in file_arr[0] : csv_data[c] = []
# for r in range(1,rows) :
#   for c in range(cols) : csv_data[ file_arr[0][c] ].append(file_arr[r][c])
