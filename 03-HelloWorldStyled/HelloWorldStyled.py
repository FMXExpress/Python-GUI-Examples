from delphifmx import *

class HelloWorld(Form):

    def __init__(self, owner):
        self.stylemanager = StyleManager(self)
        self.stylemanager.SetStyleFromFile("Air.style")
        
        self.SetProps(Caption="Hello World App")
        
        self.label = Label(self)
        self.label.SetProps(Parent=self, Text="Hello, World!", Position=Position(PointF(10,10)))

def main():
    Application.Initialize()
    Application.Title = "Hello World"
    Application.MainForm = HelloWorld(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()