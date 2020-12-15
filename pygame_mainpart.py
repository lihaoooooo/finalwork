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
reginal_line_pos = (100, 100)
# 待添加：音乐初始化部分

with open("text.txt") as f:  # 读取模板文本文件，将其转化为一排为单元的列表
    read_data_in_line = []
    for line in f:
        read_data_in_line.append(line)

line_in = ""


def draw_button_line(a):
    texlmage = myfont.render(a, True, (0, 0, 0))
    ul.draw_up_line(read_data_in_line)
    screen.blit(texlmage, input_pos)


# print(line_in)


class Upper_line:
    counter = 0

    def draw_up_line(self, text):
        screen.blit(background, (0, 0))
        if self.counter <= len(text) - 3:
            text_1 = myfont.render(text[self.counter], True, (0, 0, 0))
            text_2 = myfont.render(text[self.counter + 1], True, (0, 0, 0))
            text_3 = myfont.render(text[self.counter + 2], True, (0, 0, 0))
            screen.blit(text_1, (100, 100))
            screen.blit(text_2, (100, 150))
            screen.blit(text_3, (100, 200))
        elif self.counter <= len(text) - 2:
            text_1 = myfont.render(text[self.counter], True, (0, 0, 0))
            text_2 = myfont.render(text[self.counter + 1], True, (0, 0, 0))
            screen.blit(text_1, (100, 100))
            screen.blit(text_2, (100, 150))
        elif self.counter <= len(text) - 1:
            text_1 = myfont.render(text[self.counter], True, (0, 0, 0))
            screen.blit(text_1, (100, 100))
        else:
            pass


class Typing_data:
    count_char = 0
    count_time = 0
    count_correct = 0
    count_error = 0
    count_order = 0
    row_order = 0

    def get_WPM(self):
        return (self.count_char / 5) / (self.count_time / 30) * 60

    def get_correct_rate(self):
        return self.count_correct / self.count_char

    def get_backspace(self):
        if self.count_order > 0:
            self.count_order -= 1
            self.count_char -= 1
            self.count_error -= 1
        elif self.row_order > 0:
            self.row_order -= 1
        else:
            pass

    def draw_result(self):
        screen.blit(background, (0, 0))
        text_1 = myfont.render("WPM : {:.2f}".format(self.get_WPM()), True, (0, 0, 0))
        text_2 = myfont.render("correct rate : {:.2f}".format(self.get_correct_rate()), True, (0, 0, 0))
        text_3 = myfont.render("time : {:.2f}".format(self.count_time / 30), True, (0, 0, 0))
        screen.blit(text_1, (100, 100))
        screen.blit(text_2, (100, 150))
        screen.blit(text_3, (100, 200))


ul = Upper_line()
td = Typing_data()

# 游戏主体
while True:

    key_in = ""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_in = event.unicode
            if event.unicode != "":  # 对字符输入进行处理
                line_in = line_in + key_in
                draw_button_line(line_in)
                if ('z' >= event.unicode >= 'a') or (
                        'Z' >= event.unicode >= 'A') or (
                        '9' >= event.unicode >= '0'):
                    td.count_char += 1
                if td.row_order < len(read_data_in_line) and td.count_order < len(read_data_in_line[td.row_order]):
                    if event.unicode == read_data_in_line[td.row_order][td.count_order]:
                        td.count_correct += 1
                    else:
                        td.count_error += 1
                td.count_order += 1
            elif event.key == 8:  # 对backspace进行处理
                line_in = line_in[0:-1]
                td.get_backspace()
                if td.count_order == 0:
                    ul.counter -= 1
                draw_button_line(line_in)
            elif event.key == 13:  # 对回车进行处理
                ul.counter += 1
                draw_button_line(line_in)
                line_in = ""
                draw_button_line(line_in)
                td.row_order += 1
                td.count_order = 0
            if td.row_order >= len(read_data_in_line):
                td.draw_result()

    print(td.count_correct, td.count_char, td.count_error, td.count_time / 30)

    pygame.display.update()
    fclock.tick(fps)
    td.count_time += 1
