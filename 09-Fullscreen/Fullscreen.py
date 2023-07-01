from delphifmx import *

class FullscreenForm(Form):

    def __init__(self, owner):
        self.stylemanager = StyleManager(self)
        self.stylemanager.SetStyleFromFile("Air.style")
        
        self.SetProps(Caption = "Toggle Fullscreen", OnShow = self.__form_show, OnClose = self.__form_close)

        self.fullscreen_button = Button(self)
        self.fullscreen_button.SetProps(Parent = self, Text = "Toggle Fullscreen", Width = 200, Position = Position(PointF(40, 100)), OnClick = self.__button_click)

    def __form_show(self, sender):
        self.SetProps(Width = 300, Height = 200)

    def __form_close(self, sender, action):
        action = "caFree"

    def __button_click(self, sender):
        self.fullscreen = not self.fullscreen

def main():
    Application.Initialize()
    Application.Title = "Delphi FMX Fullscreen"
    Application.MainForm = FullscreenForm(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
