##############################################################################
#
#    Copyright (C) 2007  pronexo.com  (https://www.pronexo.com)
#    All Rights Reserved.
#    Author: Juan Manuel De Castro - jm@pronexo.com - pronexo@gmail.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from ctypes import byref, c_int, c_char, c_long, c_short, create_string_buffer, cdll
import binascii
import sys



import platform
import os
EpsonLibInterface = False
def get_driver():
	try:
		
	
		name_os = platform.system()
		path  = os.path.dirname(os.path.realpath(__file__))
		#print ('path library: '), path
		archbits = platform.architecture()[0]
		if name_os == 'Linux':
			
			
			
			if archbits[0:2] == "64":
				fullpath = path + '/Library/Linux/64/libEpsonFiscalInterface.so'
			else:
				fullpath = path + '/Library/Linux/32/libEpsonFiscalInterface.so'

			#print('fullpath: ' , fullpath)
		
			import ctypes
			EpsonLibInterface = ctypes.cdll.LoadLibrary(fullpath)
		
		else:
			from ctypes import windll
			if archbits[0:2] == "64":
				fullpath =  path + "\\Library\\Windows\\64\\EpsonFiscalInterface.dll"
			else:
				fullpath =  path + "\\Library\\Windows\\32\\EpsonFiscalInterface.dll"
			#print('fullpath: ' , fullpath)
			
			EpsonLibInterface = windll.LoadLibrary(fullpath)
	except Exception as e:	
		raise Exception(e)

	return EpsonLibInterface

