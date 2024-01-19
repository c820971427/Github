# coding: utf-8
"""
    API for setup/usage of CANoe COM Client interface
"""
import msvcrt
# ----------------------------------------------------------
# Standard library Class
import os
# import sys
import time

from win32com.client import *
from win32com.client.connect import *


# Vector Canoe Class
class CANoe:
    def __init__(self):
        self.application = None
        self.application = DispatchEx("CANoe.Application")
        self.ver = self.application.Version
        print('Loaded CANoe version ',
              self.ver.major, '.',
              self.ver.minor, '.',
              self.ver.Build, '...')  # , sep,''
        self.Measurement = self.application.Measurement.Running

    def open_cfg(self, cfg_name):
        # open CANoe simulation
        if self.application is not None:
            if os.path.isfile(cfg_name) and os.path.splitext(cfg_name)[1] == '.cfg':
                # print(os.path.isfile(cfg_name))
                # print(os.path.splitext(cfg_name))
                self.application.Open(cfg_name)
                print("opening ..." + cfg_name)
            else:
                raise RuntimeError("Can't find CANoe cfg file")
        else:
            raise RuntimeError("CANoe Application is missing,unable to open simulation")

    def close_cfg(self):
        if self.application is not None:
            # self.stop_Measurement()
            self.application.Quit()
            self.application = None

    def start_Measurement(self):
        retry = 0
        retry_counter = 5
        # try to establish measurement within 5s timeout
        if __name__ == '__main__':
            while not self.application.Measurement.Running and (retry < retry_counter):
                self.application.Measurement.Start()
                time.sleep(1)
                retry += 1
                print(retry)
            if retry == retry_counter:
                raise RuntimeWarning("CANoe start measurement failed, Please Check Connection!")

    def stop_Measurement(self):
        if self.application.Measurement.Running:
            self.application.Measurement.Stop()
        else:
            pass

    def LoadTestStep(self, tse):
        """load tse to app cfg"""
        self.TestSetup = self.application.TestSetup
        tse_path = tse

    def RunTestModules(self):
        """start test modules and wait for all of them to finish!"""
        # start test modules
        for tm in self.TestModules:
            print(tm)
            # tm.Start()

    def get_SigVal(self, channel_num, msg_name, sig_name, bus_type="CAN"):
        """
        @summary Get the value of a raw CAN signal on the CAN simulation bus
        @param channel_num - Integer value to indicate from which channel we will read the signal, usually start from 1,
                             Check with CANoe can channel setup.
        @param msg_name - String value that indicate the message name to which the signal belong. Check DBC setup.
        @param sig_name - String value of the signal to be read
        @param bus_type - String value of the bus type - e.g. "CAN", "LIN" and atc.
        @return The CAN signal value in floating point value.
                Even if the signal is of integer type, we will still return by
                floating point value.
        @exception None
        """
        if self.application is not None:
            result = self.application.GetBus(bus_type).GetSignal(channel_num, msg_name, sig_name)
            return result.Value
        else:
            raise RuntimeError("CANoe is not open,unable to GetVariable")

    def set_SigVal(self, channel_num, msg_name, sig_name, bus_type, setValue):
        if self.application is not None:
            result = self.application.GetBus(bus_type).GetSignal(channel_num, msg_name, sig_name)
            result.Value = setValue
        else:
            raise RuntimeError("CANoe is not open,unable to GetVariable")

    def DoEvents(self):
        pythoncom.PumpWaitingMessages()
        time.sleep(1)


app = CANoe()  # 实例化对象
# app.open_cfg(r"D:\my_temporary_files\CANoe工程\CANoe_test\Test_CANoev12.0.cfg")
app.open_cfg(r"D:\my_temporary_files\CANoe工程\UDSBasic\UDSBasic.cfg")

time.sleep(5)
# app.start_Measurement()
# app.RunTestModules()
# while not msvcrt.kbhit():
#     EngineSpeed = app.get_SigVal(channel_num=1, msg_name="MotorState", sig_name="CarSpeed", bus_type="CAN")
#     print(EngineSpeed)
#     app.DoEvents()
# time.sleep(10)
# app.close_cfg()
