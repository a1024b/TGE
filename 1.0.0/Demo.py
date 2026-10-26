from TGE import *
game=TGE() #创建实例
player=game.Rect(150, 150, 10, 20, 'grey', '') #创建玩家：Rect(self, x, y, w, h, fill, outline)
move_dict = {
    'w':False,
    'a':False,
    's':False,
    'd':False
}
#移动逻辑
def Move():
    if move_dict['a'] == True:
        game.Move(-1.5, 0, player) #Move(self, x, y, id)
    if move_dict['d'] == True:
        game.Move(1.5, 0, player)
    if move_dict['w'] == True:
        game.Move(0, -1.5, player)
    if move_dict['s'] == True:
        game.Move(0, 1.5, player)
    game.AddTask(Move) #循环

Move() #启动移动函数
game.Bind('KeyPress-s', lambda _: move_dict.update({'w':False, 's':True})) #按键绑定：Bind(self, event: str, func)
game.Bind('KeyPress-w', lambda _: move_dict.update({'w':True, 's':False}))
game.Bind('KeyPress-a', lambda _: move_dict.update({'a':True, 'd':False}))
game.Bind('KeyPress-d', lambda _: move_dict.update({'d':True, 'a':False}))
game.Bind('KeyRelease-s', lambda _: move_dict.update({'s':False}))
game.Bind('KeyRelease-w', lambda _: move_dict.update({'w':False}))
game.Bind('KeyRelease-a', lambda _: move_dict.update({'a':False}))
game.Bind('KeyRelease-d', lambda _: move_dict.update({'d':False}))
game.Tick(130) #修改帧率，提高理论帧率以达到理想帧率（120FPS上下）
game.Title('Demo') #修改标题
game.Size(550, 400) #修改大小
game.Bg('light blue')#修改背景
game.MainLoop() #启动主循环
