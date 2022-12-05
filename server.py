from flask import Flask, render_template
from passgen import generate_easy_password, generate_strong_password
import pickle, datetime

app = Flask(__name__, template_folder='templates')

@app.route("/") 
def index():
  return render_template('index.html', password=generate_easy_password(3))

@app.route("/beyond-passwords/") 
def beyond_passwords_page():
  return render_template('beyond-passwords.html')

@app.route("/contact/") 
def contact_page():
  return render_template('contact.html')

@app.route("/attribution/")
def attribution_page():
  return render_template('attribution.html')

@app.route("/site-plan/")
def site_plan_page():
  return render_template('/static/site-plan.html')

@app.route("/strong/") 
def strong_page():
  return render_template('index.html', password=generate_strong_password(32))


# Beep Counter

class BeepCounterClass:

    def __init__(self):
        self.beep_count = 0
        self.beep_stamp = datetime.datetime.now() + datetime.timedelta(hours = 8)
        self.init_stamp = datetime.datetime.now() + datetime.timedelta(hours = 8)

BeepCounter = BeepCounterClass()
BeepCounterFilename = "beepcounter.pickle"

@app.route("/counter/init/")
def counter_init_page():
    counter_init()
    #init_timestamp = str(datetime.datetime.now() + datetime.timedelta(hours = 8))
    return render_template('counter.html', line_1="", line_2="Initalized", line_3=str(datetime.datetime.now() + datetime.timedelta(hours = 8)), line_4="")

@app.route("/counter/beep/")
def beep_page():
    beep_return = beep()
    count = str(beep_return[0])
    timestamp = str(beep_return[1])
    return render_template('counter.html', line_1="", line_2=("beep #" + count), line_3=timestamp, line_4="")

@app.route("/counter/")
def counter_page():

    BeepCounter = BeepCounterClass()

    # load file
    with open(BeepCounterFilename, "rb") as file:
        BeepCounter = pickle.load(file)
    
    str_beepcount = str(BeepCounter.beep_count)
    str_beepstamp = str(BeepCounter.beep_stamp)
    str_initstamp = str(BeepCounter.init_stamp)
    str_runtime = str(BeepCounter.beep_stamp - BeepCounter.init_stamp)

    right_now = datetime.datetime.now() + datetime.timedelta(hours = 8)
    str_sec_ago = str(right_now - BeepCounter.beep_stamp)

    p_1 = "beep count: " + str_beepcount + " (" + str_sec_ago + " ago)"
    p_2 = "timestamp: " + str_beepstamp
    p_3 = "init: " + str_initstamp
    p_4 = "runtime: " + str_runtime

    return render_template('counter.html', line_1=p_1, line_2=p_2, line_3=p_3, line_4 = p_4)

def beep():
    """One beep"""

    BeepCounter = BeepCounterClass()

    # load file
    with open(BeepCounterFilename, "rb") as file:
        BeepCounter = pickle.load(file)

    # update values
    BeepCounter.beep_count = BeepCounter.beep_count + 1
    BeepCounter.beep_stamp = datetime.datetime.now() + datetime.timedelta(hours = 8)

    # write updated file to disk
    with open(BeepCounterFilename, "wb") as write_file:
        pickle.dump(BeepCounter, write_file)

    return [ BeepCounter.beep_count, BeepCounter.beep_stamp ]

def counter_init():
    """Reset the BeepCounter object"""

    # create the BeepCounter object
    BeepCounter = BeepCounterClass()

    BeepCounter.beep_count = 0
    BeepCounter.beep_stamp = datetime.datetime.now() + datetime.timedelta(hours = 8)
    BeepCounter.init_stamp = BeepCounter.beep_stamp

    with open(BeepCounterFilename, "wb") as file:       
        pickle.dump(BeepCounter, file)

if __name__ == "__main__":
  app.run()
