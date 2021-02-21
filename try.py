import datetime

class mytime:
    def __init__(self,hrs=0,mins=0,secs=0):
        self.hrs=hrs
        self.mins=mins
        self.secs=secs
    def printtime(self):
        timestring=""
        if self.hrs < 10:
            timestring += '0'
        timestring += str(self.hrs)+':' # timestring = "12:34:46" 
        if self.mins < 10:
            timestring += '0'
        timestring += str(self.mins)+':'
        if self.secs < 10:
            timestring += '0'
        timestring += str(self.secs)
        return (timestring)

def add_time(t1,t2):
    h = t1.hrs  + t2.hrs    # 12
    m = t1.mins + t2.mins   # 34
    s = t1.secs + t2.secs   # 46
    sumtime = mytime(h,m,s)
    return (sumtime)

d = datetime.datetime.now()
currenttime = mytime(d.hour,d.minute,d.second)
breadtime = mytime(1,0,0)
donetime = add_time(currenttime,breadtime)
print("Current Time : ",currenttime.printtime())
print("Bread Time : ",breadtime.printtime())
print("Done Time : ",donetime.printtime())
