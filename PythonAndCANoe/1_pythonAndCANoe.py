import msvcrt
import os
import sys
import time

import pythoncom
from win32com.client import *
from win32com.client.connect import *


class CANoe:
    def __init__(self):
        self.application = None
        self.application = DispatchEx("CANoe.Application")
        print(type(self.application.Version))
        self.version = self.application.Version
        print(self.version)
        print('Loaded CANoe version...',
              self.version.major, '.',
              self.version.minor, '.',
              self.version.Build, '...')
        self.Measurement = self.application.Measurement.Running
        if self.Measurement:
            self.application.Measurement.Stop()

    def open_cfg(self, cfgName):
        if self.application is not None:
            if os.path.isfile(cfgName) and (os.path.splitext(cfgName)[1] == ".cfg"):
                self.application.Open(cfgName)
                print("opening ... " + cfgName)
            else:
                raise RuntimeError("Can't find CANoe cfg file..")
        else:
            raise RuntimeError("CANoe Application is missing, unable to open simulation")

    def close_cfg(self):
        if self.application is not None:
            self.application.Quit()
            self.application = None

    def start_Measurement(self):
        retry = 0
        retry_counter = 5
        while not self.application.Measurement.Running and retry < retry_counter:
            self.application.Measurement.Start()
            time.sleep(1)
            retry += 1
        if retry == retry_counter:
            raise RuntimeWarning("CANoe start measurement failed, Please check Connection")

    def stop_Measurement(self):
        if self.application.Measurement.Running:
            self.application.Measurement.Stop()
        else:
            pass

    def get_SigVal(self, channel_num, msg_name, sig_name, bus_type='CAN'):
        """
        @summary Get the value of a raw CAN signal on the CAN simulation bus
        @param channel_num - Integer value to indicate from which channel we will read the signal, usually start from 1,
                             Check with CANoe can channel setup.
        @param msg_name - String value that indicate the message name to which the signal belong. Check DBC setup.
        @param sig_name - String value of the signal to be read
        @param bus_type - String value of the bus type - e.g. "CAN", "LIN" and etc.
        @return The CAN signal value in floating point value.
                Even if the signal is of integer type, we will still return by
                floating point value.
        @exception None
        """
        if self.application is not None:
            result = self.application.GetBus(bus_type).GetSignal(channel_num, msg_name, sig_name)
            return result.Value
        else:
            raise RuntimeError("CAN is not open, unable to GetVariable")

    def set_SigVal(self, channel_num, msg_name, sig_name, bus_type, setValue):
        if self.application is not None:
            result = self.application.GetBus(bus_type).GetSignal(channel_num, msg_name, sig_name)
            result.Value = setValue
        else:
            raise RuntimeError("CANoe is not open, unable to GetVariable")

    def get_EnvVar(self, var):
        if self.application is not None:
            result = self.application.Environment.GetVariable(var)
            return result.Value
        else:
            raise RuntimeError("CANoe is not open, unable to GetVariable")

    def set_EnvVar(self, var, value):
        result = None
        if self.application is not None:
            result = self.application.Environment.GetVariable(var)
            result.Value = value
            checker = self.get_EnvVar(var)
            while checker is not value:
                checker = self.get_EnvVar(var)
        else:
            raise RuntimeError("CANoe is not open, unable to GetVariable")

    def get_SysVar(self, ns_name, sysvar_name):
        if self.application is not None:
            systemCAN = self.application.System.Namespaces
            sys_namespace = systemCAN(ns_name)
            sys_value = sys_namespace.Variables(sysvar_name)
            return sys_value.Value
        else:
            raise RuntimeError("CANoe is not open,unable to GetVariable")

    def set_SysVar(self, ns_name, sysvar_name, var):
        if self.application is not None:
            systemCAN = self.application.System.Namespaces
            sys_namespace = systemCAN(ns_name)
            sys_value = sys_namespace.Variables(sysvar_name)
            sys_value.Value = var
        else:
            raise RuntimeError("CANoe is not open,unable to GetVariable")

    def DoEvents(self):
        pythoncom.PumpWaitingMessages()
        time.sleep(1)


app = CANoe()  # 实例化对象
try:
    # app.open_cfg(r"D:\my_temporary_files\CANoe工程\UDSBasic\UDSBasic.cfg")
    app.open_cfg(r"D:\my_temporary_files\CANoe工程\CANoe_test\Test_CANoev12.0.cfg")
except pywintypes.com_error:
    print("请检查CANoe工程修改后是否完成保存。。。。。。。。。。")
    raise pywintypes.com_error
time.sleep(2)
app.start_Measurement()

# while not msvcrt.kbhit():
#     EngineSpeed = app.get_SigVal(channel_num=1, msg_name="MotorState", sig_name="CarSpeed", bus_type="CAN")
#     print(EngineSpeed)
#     app.DoEvents()

# while not msvcrt.kbhit():
#     EngineSpeed = app.get_SigVal(channel_num=1, msg_name="MotorState", sig_name="CarSpeed", bus_type="CAN")
#     print(EngineSpeed)
#     app.set_SigVal(channel_num=1, msg_name="MotorState", sig_name="CarSpeed", bus_type="CAN", setValue=1)
#     app.DoEvents()

# while not msvcrt.kbhit():
#     bwm_test = app.get_EnvVar("en_bwm_test")
#     print(bwm_test)
#     if bwm_test == 2:
#         app.set_EnvVar("en_bwm_test", 10)

while not msvcrt.kbhit():
    EngineSpeedDspMeter = app.get_SysVar("Demo","VehSpd")
    print(EngineSpeedDspMeter)
    if EngineSpeedDspMeter == 0:
        # app.set_SysVar("Engine","EngineSpeedDspMeter",3)  #这里曾将出现问题许久没解决
        app.set_SysVar("Demo","VehSpd",3)
    app.DoEvents()

# app.close_cfg()
print(app.Measurement)
