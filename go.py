from PIL import ImageGrab
from PIL import Image
import time
import os
import glob
import win32gui
import ctypes
ctypes.windll.user32.SetProcessDPIAware() # for DPI scaling

def capture(numShots=1,delaySec=0):
    """capture and save screenshot(s)"""
    imCursor = Image.open('cursor.png')
    
    for n in range(numShots):
        im=ImageGrab.grab()
        curX,curY=win32gui.GetCursorPos()
        im.paste(imCursor,box=(curX,curY),mask=imCursor)
        fname="output/%.02f.bmp"%time.time()
        print("saving [%s] (%d of %d)"%(fname,n+1,numShots))
        im.save(fname)
        if delaySec:
            time.sleep(delaySec)

if __name__=="__main__":
    if not os.path.exists("output/"):
        os.mkdir("output")
    for fname in glob.glob("output/*.bmp"):
        os.remove(fname)
    capture(numShots=20,delaySec=1/5)