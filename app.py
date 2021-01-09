
from flask import Flask, jsonify, render_template
import datetime
app = Flask(__name__)

@app.route('/getdata', methods = ['GET'])
def stuff():
    last_won=datetime.datetime(2013,3,22,22,0,0)
    now=datetime.datetime.now()
    duration=now-last_won
    days=duration.days
    hour=duration.seconds//3600
    minutes=(duration.seconds//60)%60
    seconds=(duration.seconds)%60
    years=days//365
    rem_days=days%365
    months=rem_days//30
    days=rem_days%30    
    return jsonify(years=years,months=months,days=days,hours=hour,minutes=minutes,seconds=seconds)


@app.route('/')
def index():
   
    return render_template('index.html')

    
#if __name__ == '__main__':
    
 #   app.run()
