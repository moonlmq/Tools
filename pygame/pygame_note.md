pygame.init() 该函数用于初始化，需要在调用其他Pygame函数前被调用
pygame.display.set_mode((400, 300)) 该函数创建所谓的Surface对象用于绘图。我们为该函数提
供一个元组来表示对象的大小
pygame.display.set_caption('Hello World!') 该函数可将窗口标题设置为指定的字符串
pygame.font.SysFont("None", 19) 该函数根据英文逗号隔开的系统字体列表字符串（在本例中
为None）和字体大小创建字体对象
sysFont.render('Hello World', 0, (255, 100,
100))
该函数在Surface对象上呈现文本。最后一个参数是一个元
组，即以RGB值表示的颜色
screen.blit(rendered, (100, 100)) 该函数在Surface对象上进行绘制
pygame.event.get() 该函数用于获取Event对象列表。Event对象表示系统中的
一些特殊事件，如用户退出游戏
pygame.quit() 该函数清理Pygame使用的资源。在退出游戏前调用此函数
pygame.display.update() 该函数刷新屏幕上显示的内容