from delphifmx import *

class MyApp(Form):

    def __init__(self, owner):
        self.stylemanager = StyleManager(self)
        self.stylemanager.SetStyleFromFile("Air.style")
        
        self.SetProps(Caption="Button Click App")

        self.edit = Edit(self)
        self.edit.SetProps(Parent=self, Position=Position(PointF(10,10)))

        self.btn = Button(self)
        self.btn.SetProps(Parent=self, Text="Click Me", Position=Position(PointF(10,40)), OnClick=self.__button_click)

    def __button_click(self, sender):
        self.edit.text = "Button clicked!"

def main():
    Application.Initialize()
    Application.Title = "My App"
    Application.MainForm = MyApp(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
