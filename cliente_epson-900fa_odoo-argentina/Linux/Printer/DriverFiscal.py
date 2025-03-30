
from ctypes import cdll, windll
import platform
import os

EpsonLibInterface = False

def get_driver():
    try:
        name_os = platform.system()
        path  = os.path.dirname(os.path.realpath(__file__))
        archbits = platform.architecture()[0]
        if name_os == 'Linux':
            if archbits[0:2] == "64":
                fullpath = path + '/Library/Linux/64/libEpsonFiscalInterface.so'
            else:
                fullpath = path + '/Library/Linux/32/libEpsonFiscalInterface.so'
            EpsonLibInterface = cdll.LoadLibrary(fullpath)
        else:
            #Ojo: Siempre se va a leer la dll de 32 bits, porque se esta utilizando el python de 32 bits
            '''if archbits[0:2] == "64":
                fullpath =  path + "\\Library\\Windows\\64\\EpsonFiscalInterface.dll"
            else:'''
            fullpath =  path + "\\Library\\Windows\\32\\EpsonFiscalInterface.dll"
            EpsonLibInterface = windll.LoadLibrary(fullpath)
    except Exception as e:
        raise Exception(e)

    return EpsonLibInterface
