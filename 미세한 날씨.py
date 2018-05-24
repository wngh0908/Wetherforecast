import platform
import os


if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = ".\\SDL2\\x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = ".\\SDL2\\x64"


from pico2d import *
import Framework
import main_state
import Load

open_canvas(452, 650, 60, '미세한 날씨')
Load.PrePareResource()

Framework.run(main_state)

Load.ReleaseResource()
close_canvas()
