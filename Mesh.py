 # Mesh.py
import maya.cmds as cmds
import math
from config import *

class Mesh():
    def createNails(self):
        x = -10
        z = -10
        for i in range(441):
            height = 2
            cmds.polyCylinder(n='nailt' + str(i), h=height, r=0.1, sz=1, sy=10)
            cmds.move(0, 1, 0)
            cmds.polyCylinder(n='nailb' + str(i), h=0.02, r=0.2)
            cmds.polyCone(n='nailp' + str(i), h=0.5, r=0.1, sy=5)
            cmds.move(0, 2.25, 0)
            nail = 'nail' + str(i)
            cmds.polyUnite('nailt' + str(i), 'nailb' + str(i), 'nailp' + str(i), n=nail)
            cmds.move(x, 0, z)
            cmds.nonLinear(type='bend', curvature=0.0, lowBound=0, highBound=2)
            cmds.move(x, 0, z)
            x += 1
            if x == 11:
                x = -10
                z += 1

    def deleteKeys(self):
        for i in range(441):
            cmds.cutKey('bend' + str(i + 1), time=(0,200), at='curvature', option="keys")

    def simpleBend(self):
        self.deleteKeys()
        for i in range(441):
            name = 'bend' + str(i + 1)
            cmds.setKeyframe(name, at='curvature', time=0, v=0)
            cmds.setKeyframe(name, at='curvature', time=100, v=60)
            cmds.setKeyframe(name, at='curvature', time=200, v=0)

    def sineWave(self):
        self.deleteKeys()
        for row in range(21):
            for col in range(21):
                name = 'bend' + str((21 * col) + (row + 1))
                v1t2 = (math.sin(row) + 1) * 30
                t2 = 100 * ((60 - v1t2) / 60)
                cmds.setKeyframe(name, at='curvature', time=0, v=v1t2)
                cmds.setKeyframe(name, at='curvature', time=t2, v=60)
                cmds.setKeyframe(name, at='curvature', time=(t2 + 100), v=0)
                cmds.setKeyframe(name, at='curvature', time=200, v=v1t2)
                cmds.keyTangent(name, itt='linear', ott='linear', t=(0, 200))

    def simpleWave(self):
        self.deleteKeys()
        for row in range(21):
            for col in range(21):
                name = 'bend' + str((21 * col) + (row + 1))
                cmds.setKeyframe(name, at='curvature', time=0, v=0)
                cmds.setKeyframe(name, at='curvature', time=(row * 5), v=60)
                cmds.setKeyframe(name, at='curvature', time=(row * 5) + 100, v=0)