from delphifmx import *

MainForm = Form(Application)                    

MainForm.SetProps(Caption = "Hello World")

msg = Label(MainForm)
msg.SetProps(Parent = MainForm,                                     
    Text = "Hello Python GUI Example from Delphi FMX",
    Position = Position(PointF(50, 50)),
    Width = 300)


Application.Initialize()
Application.Title = "Hello World"
Application.MainForm = MainForm
Application.MainForm.Show()
Application.Run()
Application.MainForm.Destroy()

