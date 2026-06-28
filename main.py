import pygame as pg

print("Setup Start")
pg.init()
window = pg.display.set_mode(size=(800, 600))
print("Setup Start")

print("Loop Start")

while True:
    # check for all events
    for event in pg.event.get():
        if event.type == pg.QUIT:  # close window
            pg.quit()  # close cod
