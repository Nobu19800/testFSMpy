﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file testFSMpy.py
 @brief ModuleDescription
 @date $Date$


"""

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist
import OpenRTM_aist.StaticFSM as StaticFSM
import OpenRTM_aist.EventPort as EventPort
import testFSMpyFSM

# Import RTM module


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
testfsmpy_spec = ["implementation_id", "testFSMpy",
                  "type_name",         "testFSMpy",
                  "description",       "ModuleDescription",
                  "version",           "1.0.0",
                  "vendor",            "VenderName",
                  "category",          "Category",
                  "activity_type",     "STATIC",
                  "max_instance",      "1",
                  "language",          "Python",
                  "lang_type",         "SCRIPT",
                  ""]
# </rtc-template>

##
# @class testFSMpy
# @brief ModuleDescription
#
#


class testFSMpy(OpenRTM_aist.DataFlowComponentBase):

    ##
    # @brief constructor
    # @param manager Maneger Object
    #
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">

        # </rtc-template>

    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    #
    # @return RTC::ReturnCode_t
    #
    #

    def onInitialize(self):
        # Bind variables and configuration variable

        # Set InPort buffers

        # Set OutPort buffers

        # Set service provider to Ports

        # Set service consumers to Ports

        # Set CORBA Service Ports
        self._fsm = StaticFSM.Machine(testFSMpyFSM.Top, self)
        self._eventIn = EventPort.EventInPort("event", self._fsm)
        self.addInPort("event", self._eventIn)
        self._eventIn.bindEvent0("event1", testFSMpyFSM.Top.event1)
        self._eventIn.bindEvent0("event2", testFSMpyFSM.Top.event2)

        return RTC.RTC_OK

    ###
    ##
    # The finalize action (on ALIVE->END transition)
    ##
    # @return RTC::ReturnCode_t
    #
    ##
    def onFinalize(self):
        self._fsm.shutdown()
        return RTC.RTC_OK

    ###
    ##
    # The startup action when ExecutionContext startup
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onStartup(self, ec_id):
    #
    #    return RTC.RTC_OK

    ###
    ##
    # The shutdown action when ExecutionContext stop
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onShutdown(self, ec_id):
    #
    #    return RTC.RTC_OK

    ###
    ##
    # The activated action (Active state entry action)
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onActivated(self, ec_id):
    #
    #    return RTC.RTC_OK

    ###
    ##
    # The deactivated action (Active state exit action)
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onDeactivated(self, ec_id):
    #
    #    return RTC.RTC_OK

    ###
    ##
    # The execution action that is invoked periodically
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    def onExecute(self, ec_id):
        self._fsm.run_event()
        return RTC.RTC_OK

    ###
    ##
    # The aborting action when main logic error occurred.
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onAborting(self, ec_id):
    #
    #    return RTC.RTC_OK

    ###
    ##
    # The error action in ERROR state
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onError(self, ec_id):
    #
    #    return RTC.RTC_OK

    ###
    ##
    # The reset action that is invoked resetting
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onReset(self, ec_id):
    #
    #    return RTC.RTC_OK

    ###
    ##
    # The state update action that is invoked after onExecute() action
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##

    ##
    # def onStateUpdate(self, ec_id):
    #
    #    return RTC.RTC_OK

    ###
    ##
    # The action that is invoked when execution context's rate is changed
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onRateChanged(self, ec_id):
    #
    #    return RTC.RTC_OK


def testFSMpyInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=testfsmpy_spec)
    manager.registerFactory(profile,
                            testFSMpy,
                            OpenRTM_aist.Delete)


def MyModuleInit(manager):
    testFSMpyInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""

    # Create a component
    comp = manager.createComponent("testFSMpy" + args)


def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()


if __name__ == "__main__":
    main()
