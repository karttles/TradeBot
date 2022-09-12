from datetime import datetime

arr = []


def getGroup():


    def getTime(lastTime):
        time = datetime.now().strftime("%H:%M")
        if time != lastTime:
            print(f'new time is {time}')
            return time

    def addNum(msg):
        p = 0
