from flask import *
import datetime
import database
from TimeSlot import *

database = database.Database()
timeSlot = TimeSlot(database)
app = Flask(__name__)
variable = "Timer not started"
@app.route("/", methods =["GET", "POST"])
def hello_world():
    global timeSlot, variable
    if request.method == 'POST':
        if request.form.get('startTimer') == "Start":
            variable = "Timer started"
            timeSlot.startTime(datetime.datetime.now())
        elif request.form.get('stopTimer') == "Stop":
            variable = "Timer not started"
            timeSlot.endTime(datetime.datetime.now())
        elif request.form.get('getJson') == 'Get Json':
            database.getTableAsJson()
    elif request.method == 'POST':
        return render_template("myPage.html", form=form, variable=variable)
    return render_template("myPage.html", variable=variable)

if __name__ == '__main__':
    app.run(debug=True)