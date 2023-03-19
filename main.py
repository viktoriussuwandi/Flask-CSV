from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import csv,json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

@app.route("/")
def home() :
  return render_template("index.html")

@app.route("/cafes")
def cafes() :
  with open ('cafe-data.csv',newline='') as f :
    file      = csv.reader(f, delimiter = ",")
    file_data = [row for row in file]
  return render_template( "cafes.html", file_data = file_data )

if __name__ == "__main__" :
  app.run(debug=True, host="0.0.0.0", port=2000)

# Convert csv data to json format
# rows = len(file_arr) # 5 rows
# cols = len( list(csv_data.keys()) ) # 7 columns
# csv_data = {}
# for c in file_arr[0] : csv_data[c] = []
# for r in range(1,rows) :
#   for c in range(cols) : csv_data[ file_arr[0][c] ].append(file_arr[r][c])
