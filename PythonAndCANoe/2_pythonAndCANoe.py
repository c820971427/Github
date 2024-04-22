import time, os, msvcrt
from win32com.client import *
from win32com.client.connect import *


def DoEvents():
    pythoncom.PumpWaitingMessages()
    time.sleep(.1)


def DoEventsUntil(cond):
    while not cond():
        DoEvents()


class CanoeSync(object):
    """Wrapper class for CANoe Application object"""
    Started = False
    Stopped = False
    ConfigPath = ""

    def __init__(self):
        app = DispatchEx('CANoe.Application')
        app.Configuration.Modified = True
        ver = app.Version
        print('Loaded CANoe version ',
              ver.major, '.',
              ver.minor, '.',
              ver.Build, '...', sep='')
        self.App = app
        self.Measurement = app.Measurement
        self.Running = lambda: self.Measurement.Running
        self.WaitForStart = lambda: DoEventsUntil(lambda: CanoeSync.Started)
        self.WaitForStop = lambda: DoEventsUntil(lambda: CanoeSync.Stopped)
        WithEvents(self.App.Measurement, CanoeMeasurementEvents)

    def Start(self):
        if not self.Running():  # 如果已经启动了，就不在执行Measurement.Start()了
            self.Measurement.Start()
            self.WaitForStart()

    def Stop(self):
        if self.Running():
            self.Measurement.Stop()
            self.WaitForStop()


class CanoeMeasurementEvents(object):
    """Handler for CANoe measurement events"""

    def OnStart(self):
        CanoeSync.Started = True
        CanoeSync.Stopped = False
        print("< measurement started >")

    def OnStop(self):
        CanoeSync.Started = False
        CanoeSync.Stopped = True
        print("< measurement stopped >")


def main():
    app = CanoeSync()
    app.Start()


if __name__ == "__main__":
    main()

