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
        neighborhood = app.getOptionBox("neighborhood")
        sessionPeriod = app.getOptionBox("sessionPeriod")
        sessionGoal = app.getOptionBox("sessionGoal")
        sessionTime = int(app.getEntry("sessionTime"))
        sessionCount = int(app.getEntry("sessionCount"))
       	dateStart = str(app.getDatePicker("dateStart"))
       	wakeTime += ":00"
       	sleepTime += ":00"

        

        print ("date start: ", dateStart)

        #2017-mm-dd

       	print(wakeTime, sleepTime, sessionCount, sessionTime, sessionPeriod,  sessionGoal, dateStart, neighborhood,)

       	# def main(wake, bed, des_days, timelim, timepref,exrgl, startd, neigh):
       	my_calendar.main(wakeTime,sleepTime,sessionCount,sessionTime,sessionPeriod,sessionGoal,dateStart, neighborhood)

       	webbrowser.open_new('https://calendar.google.com/')


# create the GUI
app = gui("What2Wear", "600x700")
app.addLabel("title", "Welcome to What2Wear!")
app.setFont(18)

app.setFont(12)
app.addMessage("mess", """Please enter the following preferences:""", colspan=2)


app.addLabel("wake", "Wake Time (eg. 07:00, 24hr time)",2,0)
app.addEntry("wakeTime",3,0)

app.addLabel("sleep", "Sleep Time (eg. 22:30, 24hr time)",2,1)
app.addEntry("sleepTime",3,1)

app.addLabelOptionBox("neighborhood", ["yard", "river", "quad"],colspan=2)

app.addLabelOptionBox("sessionPeriod", ["morning", "afternoon", "evening"],colspan=2)

app.addLabelOptionBox("sessionGoal", ["strength", "cardio"],colspan=2)

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