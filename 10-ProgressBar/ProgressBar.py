from delphifmx import *

class ProgressBarForm(Form):

    def __init__(self, owner):
        self.stylemanager = StyleManager(self)
        self.stylemanager.SetStyleFromFile("Air.style")
        
        self.SetProps(Caption = "Progress Bar Example", OnShow = self.__form_show, OnClose = self.__form_close)

        self.progressbar = ProgressBar(self)
        self.progressbar.SetProps(Parent = self, Max = 100, Min = 0, Value = 0, Align = "Center", Width = 260)

        self.start_button = Button(self)
        self.start_button.SetProps(Parent = self, Text = "Toggle Timer", Align = "Center", Margins = Bounds(RectF(0, 0, 0, -100)), OnClick = self.__button_click)
        
        self.timer = Timer(self)
        self.timer.SetProps(Parent = self, Enabled = False, OnTimer = self.__timer_event)
        
    def __form_show(self, sender):
        self.SetProps(Width = 640, Height = 480)

    def __form_close(self, sender, action):
        action = "caFree"

    def __timer_event(self, sender):
        if hasattr(self.progressbar, 'Value'):
            if self.timer.Enabled == True:
                if self.progressbar.Value == self.progressbar.Max:
                    self.progressbar.Value = self.progressbar.Min
                else:
                    self.progressbar.Value += 5

    def __button_click(self, sender):
        if self.timer.Enabled == True:
            self.timer.Enabled = False
        else:
            self.timer.Enabled = True

def main():
    Application.Initialize()
    Application.Title = "Progress Bar Delphi FMX"
    Application.MainForm = ProgressBarForm(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
