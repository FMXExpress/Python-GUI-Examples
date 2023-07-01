from delphifmx import *
from os.path import exists

class TabApp(Form):

    def __init__(self, owner):
        self.stylemanager = StyleManager(self)
        self.stylemanager.SetStyleFromFile("Air.style")
        
        self.SetProps(Caption = "Tabbed App", OnShow = self.__form_show, OnClose = self.__form_close)

        self.tabControl = TabControl(self)
        self.tabControl.SetProps(Parent = self, Align = "Client", Margins = Bounds(RectF(3, 3, 3, 3)),)

        self.tab1 = TabItem(self.tabControl)
        self.tab1.SetProps(Parent = self.tabControl, Text = "Tab 1")

        self.tab2 = TabItem(self.tabControl)
        self.tab2.SetProps(Parent = self.tabControl, Text = "Tab 2")

        self.label1 = Label(self.tab1)
        self.label1.SetProps(Parent = self.tab1, Text = "You're on Tab 1!", Position = Position(PointF(20, 20)))

        self.label2 = Label(self.tab2)
        self.label2.SetProps(Parent = self.tab2, Text = "You're on Tab 2!", Position = Position(PointF(20, 20)))

    def __form_show(self, sender):
        self.SetProps(Width = 640, Height = 480)

    def __form_close(self, sender, action):
        action = "caFree"

def main():
    Application.Initialize()
    Application.Title = "Delphi FMX Tabbed App"
    Application.MainForm = TabApp(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
