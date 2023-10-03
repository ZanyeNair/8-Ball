import pygame as p
p.init()



WIN = p.display.set_mode((800, 800))
p.display.set_caption("8-Ball Pool")

FPS = 60

CLOCK = p.time.Clock()

FONT_STYLE = p.font.SysFont("bahnschrift", 25)

BG = (0, 255, 0)
WIN.fill(BG)

# TODO: Literally Everything Else lolz



# ----------------------------- MAIN LOOP ----------------------------- #
def main():
        while True:
                for event in p.event.get():
                        if event.type == p.QUIT:
                                p.quit()
                
                
                p.display.flip()
                CLOCK.tick(FPS)

main()
