import pygame as p
p.init()
while True:
	for event in p.event.get():
    	if event.type == p.QUIT():
        	p.quit()
