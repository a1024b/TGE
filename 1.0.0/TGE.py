from tkinter import Tk, Canvas, font
from time import sleep, perf_counter

class TGE:
    def __init__(self):
        self.__Root=Tk()
        self.__Canva=Canvas(self.__Root)
        self.__TaskList=[]
        self.__Main=True
        self.__FPS=30
        self.__title='TGE_Window'
        self.__Font=font.Font(family='PingFang SC',
                              size=20,
                              weight='normal',
                              underline=False,
                              overstrike=False,
                              slant='italic')
        
        self.Ver='1.0.0'
        self.__Root.title('TGE_Window')
        self.__Root.geometry('300x400')
        self.__Root.protocol("WM_DELETE_WINDOW", self.Exit)
    def Bg(self, color):
        self.__Canva['bg']=color
    def Tick(self, FPS: int|float):
        self.__FPS=FPS
    def Exit(self):
        self.__Main=False
    def AddTask(self, func, *args):
        self.__TaskList.append([func, args])
    def MainLoop(self):
        self.__Canva.pack(fill='both', expand=True, anchor='center')
        while self.__Main:
            t0=perf_counter()
            self.__Root.update()
            if self.__TaskList:
                self.__TaskList[0][0](*self.__TaskList[0][1])
                self.__TaskList.remove(self.__TaskList[0])
            dt=perf_counter()-t0
            if dt<1/self.__FPS:
                sleep(1/self.__FPS-dt)
            frame_dt = perf_counter() - t0
            self.__Root.title(f'{self.__title} - FPS: {1/frame_dt:.1f}')
    def Font(self, family='PingFang SC', size=20, **kw):
        return font.Font(family=family, size=size, **kw)
    def Bind(self, event: str, func):
        self.__Root.bind(f'<{event}>', func)
    def Text(self, x, y, text, Font=None):
        if Font==None:
            Font=self.__Font
        return self.__Canva.create_text(x, y, text=text, font=Font)
    def Rect(self, x, y, w, h, fill, outline):
        return self.__Canva.create_rectangle(x, y, x+w, y+h, fill=fill, outline=outline)
    def BBox(self, id):
        return self.__Canva.bbox(id)
    def Move(self, x, y, id):
        self.__Canva.move(id, x, y)
    def Force(self):
        self.__Root.focus_force()
    def Title(self, string):
        self.__Root.title(string)
        self.__title=string
    def Size(self, w, h):
        self.__Root.geometry(f'{w}x{h}')
    def SetPos(self, id, x, y, dx, dy):
        self.__Canva.coords(id, x, y, x+dx, y+dy)
    def Delete(self, id):
        self.__Canva.delete(id)
