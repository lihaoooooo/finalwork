import sys
import pygame

# 初始化
pygame.init()
width, height = 1000, 667
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("coding_practice")
background = pygame.image.load("background.jpg").convert()
bacrground_rect = background.get_rect()

# 待添加：音乐初始化部分
screen.blit(background, (0, 0))

pygame.event.get()
with open("text.txt") as f:  # 读取模板文本文件，将其转化为一排为单元的列表
    read_data_in_line = []
    for line in f:
        read_data_in_line.append(line)
# 游戏主体
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
