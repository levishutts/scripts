# DemoUI.py
import maya.cmds as cmds
import Mesh as mm
from config import *

class DemoUI(object):
    def __init__(self):
        self._mesh = mm.Mesh()

        self.window = cmds.window(title ="SliderWindow")
        
        self.column = cmds.columnLayout()
        
        cmds.button(
            'Create Nails',
            backgroundColor=LIGHT_GRAY,
            command=lambda *args: self._createNails()
        )

        cmds.button(
            'Simple bend',
            backgroundColor = DEFAULT_GRAY,
            command = lambda *args: self._simpleBend()
        )

        cmds.button(
            'Simple wave',
            backgroundColor = DARK_GRAY,
            command = lambda *args: self._simpleWave()
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

    def _simpleWave(self):
        self._mesh.simpleWave()
