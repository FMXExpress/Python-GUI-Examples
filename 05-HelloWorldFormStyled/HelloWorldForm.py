import os
from delphifmx import *

class Form1(Form):

    def __init__(self, owner):
        self.Label1 = None
        self.MaterialOxfordBlueSB = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "HelloWorldForm.pyfmx"))
        
def main():
    Application.Initialize()
    Application.Title = "Hello World"
    Application.MainForm = Form1(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()