import wx 
 
app = wx.App() 
window = wx.Frame(None, title = "ventana", size = (300,200)) 
panel = wx.Panel(window) 
label = wx.StaticText(panel, label = "Hola Mundo", pos = (100,50)) 
window.Show(True) 
app.MainLoop()
