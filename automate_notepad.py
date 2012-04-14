import os
import sys

'''
	Add the White automation library assemblies to the sys.path so that a 
	simple AddReference will find them.
'''
project_root = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(project_root, "libs\\white"))

import clr
clr.AddReference("White.Core.dll")

from White.Core import *
from White.Core.UIItems import *

from System import Array

try:
	notepad = Application.Launch("C:\\Windows\\System32\\Notepad.exe")
	notepad_window = notepad.GetWindow("Untitled - Notepad")

	'''
		File open dialog is a little funny - Can't open it with GetWindow since
		it's modal, but, ModalWindow won't find it either.  GetWindows seems to
		find it alright.  :/
	'''
	notepad_window.MenuBar.MenuItem(Array[str](["File", "Open..."])).Click()
	file_open_dialog = notepad.GetWindows().Find(lambda window: window.Name == "Open")
	file_open_dialog.Get[TextBox]("File name:").Text = "I'm in ur TextBox entering textz!!11"
	file_open_dialog.Get[Button]("Cancel").Click()
	
	# Enter some random text...
	notepad_window.Get[MultilineTextBox]().Text = "Im in ur MultilineTextBox entering textz!!11"
	
	# Exit cleanly.
	notepad_window.MenuBar.MenuItem(Array[str](["File", "Exit"])).Click()
	notepad.GetWindows().Find(lambda window: window.Name == "Notepad").Get[Button]("Don't Save").Click()
	
finally:
	notepad.Kill()
