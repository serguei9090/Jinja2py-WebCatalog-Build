from flask import Flask, render_template
from icalendar import Calendar
from icalendar.cal import Event
import datetime
import urllib3
import requests

app = Flask(__name__)

app.secret_key = 'mysecretkey'

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/show_icals')
def show_icals():
    return render_template('show_icals.html')


@app.route('/get_icals')
def get_icals():
    url_list = [
        "https://es.airbnb.com/calendar/ical/15780667.ics?s=d1e875f1b1354e49268a3fed4fe0777f",
        "https://es.airbnb.com/calendar/ical/15781363.ics?s=f21f3d2768a5d6c02d2ede86ed3b4d4c",
        "https://es.airbnb.com/calendar/ical/15781737.ics?s=f6fbd492e7b47c81515c30a6904b3f51"
        ]
    for url in url_list :
        ical_request = requests.get(url).text
#        print(ical_request)
        cal = Calendar.from_ical(ical_request)
        rows=[]
        for c in cal.walk():
            if isinstance(c, Event):
                dtstart =   c['DTSTART'].dt.strftime('%Y-%m-%d %H:%M:%S')
                dtend   =   c['DTEND'].dt.strftime('%Y-%m-%d %H:%M:%S')
                if c['DTSTART'].dt.year >= 2020 :
#                    and c['DTSTART'].dt.month >= 11:
                    rows.append([ dtstart, dtend, c['SUMMARY'],
                                c['DTEND'].dt - c['DTSTART'].dt])
    return  render_template('show_icals.html', ical_rows = rows)


@ app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(port = 8080, debug = True)
