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
reginal_line_pos = (100,100)
# 待添加：音乐初始化部分



with open("text.txt") as f:  # 读取模板文本文件，将其转化为一排为单元的列表
    read_data_in_line = []
    for line in f:
        read_data_in_line.append(line)

line_in = ""

def draw_button_line(line_in):
    texlmage = myfont.render(line_in, True, (0, 0, 0))
    ul.draw_up_line(read_data_in_line)
    screen.blit(texlmage, input_pos)
    print(line_in)



class Upper_line:
    counter = 0
    def draw_up_line(self,text):
        screen.blit(background, (0, 0))
        if self.counter <= len(text) - 3:
            text_1 = myfont.render(text[self.counter], True, (0, 0, 0))
            text_2 = myfont.render(text[self.counter+1], True, (0, 0, 0))
            text_3 = myfont.render(text[self.counter+2], True, (0, 0, 0))
            screen.blit(text_1, (100,100))
            screen.blit(text_2, (100, 150))
            screen.blit(text_3, (100, 200))
        elif self.counter <= len(text) - 2:
            text_1 = myfont.render(text[self.counter], True, (0, 0, 0))
            text_2 = myfont.render(text[self.counter + 1], True, (0, 0, 0))
            screen.blit(text_1, (100, 100))
            screen.blit(text_2, (100, 150))
        else:
            self.counter - 1

class Typing_data:
    count_words = 0
    count_time = 0
    count_correct = 0
    count_error = 0
    def get_WPM(self):
        return self.count_time / self.count_words
    def get_correct_rate(self):
        return self.count_correct / self.count_words



ul = Upper_line()





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
            if event.unicode != "":
                line_in = line_in + key_in
                draw_button_line(line_in)
            elif event.key == 8:
                line_in = line_in[0:-1]
                draw_button_line(line_in)
            elif event.key == 13:
                ul.counter += 1




    pygame.display.update()
    fclock.tick(fps)
