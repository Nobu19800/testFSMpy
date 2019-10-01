#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @file testFSMpyFSM.py
 @brief ModuleDescription
 @date $Date$


"""
import sys

import RTC
import OpenRTM_aist.StaticFSM as StaticFSM


@StaticFSM.FSM_TOPSTATE
class Top(StaticFSM.Link):
    def onInit(self):
        self.set_state(StaticFSM.State(node1))
        return RTC.RTC_OK

    """
    """

    def event1(self):
        pass

    """
    """

    def event2(self):
        pass


@StaticFSM.FSM_SUBSTATE(Top)
class node1(StaticFSM.Link):
    def onEntry(self):
        return RTC.RTC_OK

    def onExit(self):
        return RTC.RTC_OK

    def event1(self):
        self.set_state(StaticFSM.State(node2))


@StaticFSM.FSM_SUBSTATE(Top)
class node2(StaticFSM.Link):
    def onEntry(self):
        return RTC.RTC_OK

    def onExit(self):
        return RTC.RTC_OK

    def event2(self):
        self.set_state(StaticFSM.State(node3))


@StaticFSM.FSM_SUBSTATE(Top)
class node3(StaticFSM.Link):
    def onEntry(self):
        return RTC.RTC_OK

    def onExit(self):
        return RTC.RTC_OK
