import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(Loggable, list):
    def append(self, element):
        super(LoggableList, self).log(element)
        super(LoggableList, self).append(element)


a = Loggable()
a.log('dd')

b = LoggableList()
b.append('123')
