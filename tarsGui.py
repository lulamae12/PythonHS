import wx

#main class for app frame
class Dashboard(wx.Frame):
    def __init__(self):
        #basic gui stuff
        wx.Frame.__init__(self, None,pos=wx.DefaultPosition, size=wx.Size(450, 300),style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |wx.CLOSE_BOX | wx.CLIP_CHILDREN,title="TARS")
        panel = wx.Panel(self)
        mySizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(panel,label="Hello I am TARS. How can I help you?")
        button = wx.Button(panel,wx.ID_ANY,"Submit",(180,200))
        button.Bind(wx.EVT_BUTTON,self.OnButtonPress)
        mySizer.Add(label, 0, wx.ALL, 5)

        self.textBox =wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.textBox.SetFocus()
        self.textBox.Bind(wx.EVT_TEXT_ENTER, self.OnButtonPress)
        mySizer.Add(self.textBox, 0, wx.ALL ,5)
        panel.SetSizer(mySizer)
        self.Show()
    def OnButtonPress(self, event):
        input =self.textBox.GetValue()
        input = input.lower()
        print(input)

app = wx.App(True)
frame = Dashboard()
app.MainLoop()
