# import the library
from appJar import gui
import backend


# handle button events
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        wakeTime = app.getEntry("wakeTime")
        sleepTime = app.getEntry("sleepTime")
        feel = app.getOptionBox("How do you want to feel?")
        makeTime = app.getOptionBox("What do you want to make time for?")
        distracts = app.getOptionBox("What distracts you most?")
        sessionTime = int(app.getEntry("sessionTime"))
        sessionCount = int(app.getEntry("sessionCount"))
       	dateStart = str(app.getDatePicker("dateStart"))
       	wakeTime += ":00"
       	sleepTime += ":00"
        print ("date start: ", dateStart)
        
       	webbrowser.open_new('https://calendar.google.com/')


# create the GUI
app = gui("Habits", "600x700")
app.addLabel("title", "Welcome to Habits!")
app.setFont(18)

app.setFont(12)
app.addMessage("mess", """Please enter the following preferences:""", colspan=2)


app.addLabel("wake", "Wake Time (eg. 07:00, 24hr time)",2,0)
app.addEntry("wakeTime",3,0)

app.addLabel("sleep", "Sleep Time (eg. 22:30, 24hr time)",2,1)
app.addEntry("sleepTime",3,1)

app.addLabelOptionBox("How do you want to feel?", ["energized", "relaxed", "motivated"],colspan=2)

app.addLabelOptionBox("What do you want to make time for?", ["exercise", "sleep", "friends","meals","me-time","reading"],colspan=2)

app.addLabelOptionBox("What distracts you most?", ["phone", "friends", "work", "news"],colspan=2)

app.addLabel("sTime", "Average Session Length (min)",7,0)
app.addNumericEntry("sessionTime",8,0)

app.addLabel("sCount", "Desired Sessions per Week",7,1)
app.addNumericEntry("sessionCount",8,1)


app.addDatePicker("dateStart")
#app.addButton("GET", showDate)
app.setDatePickerRange("dateStart", 1900, 2100)
app.setDatePicker("dateStart")

# link the buttons to the function called press
app.addButtons(["Submit", "Cancel"], press, colspan=2)


# start the GUI
app.go()