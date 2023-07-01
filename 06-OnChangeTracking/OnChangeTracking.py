from delphifmx import *

class MyApp(Form):

    def __init__(self, owner):
        self.stylemanager = StyleManager(self)
        self.stylemanager.SetStyleFromFile("Air.style")    
    
        self.SetProps(Caption="Change Tracking App")

        self.edit = Edit(self)
        self.edit.SetProps(Parent=self, Position=Position(PointF(10,10)), Text = "Type here...", OnChangeTracking=self.__edit_change)

        self.label = Label(self)
        self.label.SetProps(Parent=self, Position=Position(PointF(10,40)))

    def __edit_change(self, sender):
        self.label.Text = self.edit.text

def main():
    Application.Initialize()
    Application.Title = "My App"
    Application.MainForm = MyApp(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()