# config.py

import maya.cmds as cmds

workspace = cmds.workspace(query=True, dir=True)

# presuming the user name is the element split off based on '/'
user = workspace.split('/')[2]

# some standarized colors
BEIGE        = [0.5, 0.75, 0.5]
DARK_GRAY    = [0.2, 0.2, 0.2]
DARK_GREEN   = [0.2, 0.4, 0.2]
DARK_MOAVE   = [0.22, 0.39, 0.39]
DEFAULT_GRAY = [0.267, 0.267, 0.267]
GRAY_GREEN   = [0.1, 0.3, 0.1]
LIGHT_GRAY   = [0.8, 0.8, 0.8]
LIGHT_GREEN  = [0.5, 0.85, 0.57]
MID_GRAY     = [0.4, 0.4, 0.4]
MOAVE        = [0.5, 0.56, 0.57]
RED          = [1.0, 0.0, 0.0]
TAN          = [0.9, 0.7, 0.56]
YELLOW       = [1.0, 1.0, 0.53]
BLUE         = [0, 0, 0.53]