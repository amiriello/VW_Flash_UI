import wx

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        button = wx.BoxSizer(wx.HORIZONTAL)
        flex = wx.FlexGridSizer(2, 3, 3, 3)
        
        caltext = wx.StaticText(panel, label="CAL")
        
        inputcal = wx.TextCtrl(panel)
        buttoncal = wx.Button(panel, label='...')
        #lashbutton = wx.Button(panel, label='Flash')
        
        flex.AddMany([ (caltext), (inputcal, 1, wx.EXPAND), (buttoncal, 1, wx.EXPAND)])
        flex.AddGrowableRow (1, 1)
        flex.AddGrowableCol (1, 1)
        
        hbox.Add(flex, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        #button.Add(flashbutton)
        panel.SetSizer(hbox)

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()