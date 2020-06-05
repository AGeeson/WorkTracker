import time
from datetime import date

today = date.today()
today = today.strftime("%d/%m/%Y")




class WorkTopic:
    def __init__(self, name, time_added, date_added):
        self.name = name
        self.time_added = time_added
        self.date_added = date_added



edd_time = 0.0
end_break = 0.0
start_break = 0.0
start_time = 0.0
end_time = 0.0
breaks = []
print(type(end_time))

inf = print(breaks,",", end_break,",", start_break,",", start_time, ",",)

def timetracker():
    print("what are you working on?")
    work_topic = input()
    print("you are about to working on:" + work_topic)
    readytoWork()


def readytoWork():
    print("are you ready to start timing? [y/n]")
    readycheck = input()
    if readycheck == 'y':
        global start_time 
        start_time=time.time()
        print(str(start_time) + " minutes elapsed")
        ongoing()
    elif readycheck == 'n':
        return timetracker()
    else: 
        print("sorry," + readycheck + "is not a valid input.")
        return readytoWork()

def ongoing():
    print("work period has begun, function: break, endsession")
    ongoing_input = input()
    if ongoing_input == 'break':
        global start_break
        start_break=time.time()
        elapsed = (start_break - start_time)/60
        print("you have done" + str(elapsed) + " minutes of work so far")
        print("Functions: continue, endsession")
        break_input = input()
        if break_input == 'continue':
            global end_break
            end_break == time.time()
            global breaks
            breaks.append(end_break - start_break)
            ongoing()
            print("Work time has started. Functions: break, end")
        elif break_input == 'endsession':
            endsession()
        else:
            print(ongoing_input + ", is not a valid input.")
            print("Functions: continue, endsession")
            return ongoing_input
    elif ongoing_input == 'endsession':
        endsession()
            

def endsession():  
    global end_time, start_time, breaks
    end_time = time.time()
    total_breaks = sum(breaks)
    time_done = (end_time - start_time - total_breaks)/60
    time_done = "{:.2f}".format(time_done)
    time_done = str(time_done).split(".")
    print(inf)
    print("total breaks:", len(breaks))
    print("Well done! You have done " + time_done[0] + ' minutes ' + time_done[1] + ' seconds of work.' )
    print("What did you work on?")
    session_notes = input()
    print("what next? viewsessions, work or quit?")


timetracker()