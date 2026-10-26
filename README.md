# TGE介绍
### 作者：a1024b（苏苏QwQ）
### 语言：Python

#### 本引擎为一款由Tkinter驱动的游戏引擎，抛弃Tk.mainloop，使用while+update实现高帧率主循环
#### 本引擎语法简洁，以下为API列表（1.0.0版本）：
```Python
Bg(self, color)
Tick(self, FPS: int|float)
Exit(self)
AddTask(self, func, *args)
MainLoop(self)
Font(self, family='PingFang SC', size=20, **kw)
Bind(self, event: str, func)
Text(self, x, y, text, Font=None)
Rect(self, x, y, w, h, fill, outline)
BBox(self, id)
Move(self, x, y, id)
Force(self)
Title(self, string)
Size(self, w, h)
SetPos(self, id, x, y, dx, dy)
Delete(self, id)
```
