#launchDemoUI.py

import DemoUI as ui
import config as c
import Mesh as m

reload(ui)
reload(c)
reload(m)

interface = ui.DemoUI()

interface.startUI()
