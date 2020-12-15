import sys
import pygame

# 初始化

pygame.init()
width, height = 1000, 667
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("coding_practice")
background = pygame.image.load("background.jpg").convert()
bacrground_rect = background.get_rect()
fps = 30
fclock = pygame.time.Clock()
myfont = pygame.font.Font(None, 60)  # 创建字体
input_pos = (100, 500)
# 待添加：音乐初始化部分



with open("text.txt") as f:  # 读取模板文本文件，将其转化为一排为单元的列表
    read_data_in_line = []
    for line in f:
        read_data_in_line.append(line)

line_in = ""

# 游戏主体
while True:
    key_in = ""
    refresh_key = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_in = event.unicode
            refresh_key = 1
            if key_in != "":
                line_in = line_in + key_in
                texlmage = myfont.render(line_in, True, (0, 0, 0))
                screen.blit(texlmage, input_pos)
             #   print(line_in)

    screen.blit(background, (0, 0))
    pygame.display.update()
    fclock.tick(fps)
