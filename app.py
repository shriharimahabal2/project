from flask import Flask, render_template

app = Flask(__name__)

data = [{
    'title': 'Data Analyst',
    'location': 'Delhi',
    'salary': '100000'
}, {
    'title': 'Data Scientist',
    'location': 'Mumbai',
    'salary': '200000'
}, {
    'title': 'Developer',
    'location': 'Chennai',
    'salary': '500000'
}]


@app.route('/')
def home():
  return render_template('home.html', data=data)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
