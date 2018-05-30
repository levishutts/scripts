# DemoUI.py
import maya.cmds as cmds
import Mesh as mm
from config import *


class DemoUI(object):
    def __init__(self):
        self._mesh = mm.Mesh()

        self.window = cmds.window(title="SliderWindow")

        self.column = cmds.columnLayout()

        cmds.button(
            'Create Nails',
            backgroundColor=LIGHT_GRAY,
            command=lambda *args: self._createNails()
        )

        cmds.button(
            'Simple bend',
            backgroundColor=DEFAULT_GRAY,
            command=lambda *args: self._simpleBend()
        )

        cmds.button(
            'Uniform wave',
            backgroundColor=DEFAULT_GRAY,
            command=lambda *args: self._uniformWave()
        )

        cmds.button(
            'Sine wave',
            backgroundColor=MID_GRAY,
            command=lambda *args: self._sineWave()
        )

        cmds.button(
            'Simple wave',
            backgroundColor=DARK_GRAY,
            command=lambda *args: self._simpleWave()
        )
        cmds.button(
            'Apply material',
            backgroundColor=DARK_GREEN,
            command=lambda *args: self._assignPewter()
        )

        cmds.showWindow(self.window)

    def startUI(self):
        currentWindows = cmds.lsUI(windows=True)
        for window in currentWindows:
            title = cmds.window(window, query=True, title=True)
            if title == 'Controls':
                cmds.deleteUI(window)

    def _createNails(self):
        self._mesh.createNails()

    def _simpleBend(self):
        self._mesh.simpleBend()

    def _uniformWave(self):
        self._mesh.uniformWave()

    def _sineWave(self):
        self._mesh.sineWave()

    def _simpleWave(self):
        self._mesh.simpleWave()

    def _assignPewter(self):
        self._mesh.assignPewter()
