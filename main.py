import pygame as p
p.init()
WIN = p.display.set_mode((800, 800))
p.display.set_caption("8-Ball Pool")

while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                    p.quit()
