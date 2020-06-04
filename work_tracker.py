import time

print("what are you working on?")
what_work = input()
print("you are about to working on:" + what_work)
print("are you ready to start timing? [y/n]")

readyToWork = input()
end_break = 0.0
start_break = 0.0
start_time = 0.0
end_time = 0.0
print(type(end_time))
if readyToWork == 'y':
    start_time=time.time()
    print(start_time)
    print("Work time has started. Functions: break, end")
    ongoing_input = input()
    if ongoing_input == 'break':
        start_break=time.time()
        elapsed = (start_break - start_time)/60
        print("you have done" + elapsed + " minutes of work so far")
        print("Functions: continue, endsession")
        break_input = input()
        if break_input == 'continue':
            end_break = time.time()
            print("Work time has started. Functions: break, end")
    elif ongoing_input == 'end':
        end_time = time.time()
        time_done = (end_time - start_time - end_break + start_break)/60
        time_done = "{:.2f}".format(time_done)
        time_done = str(time_done).split(".")
        print("Well done! You have done " + time_done[0] + ' minutes ' + time_done[1] + ' seconds of work.' )
        print("What did you work on?")
        session_notes = input()
    else:
        print(ongoing_input + ", is not a valid input.")
# start timer
elif readyToWork == 'n':
    pass
else:
    print("sorry," + readyToWork + "is not a valid input.")
    # return back to readytowork

