#collision box
#create a box that can change colour if it collides with the mouse
import pygame, os
from engine import game_engine_21222 as game_engine
pygame.font.init()
file_dir = os.getcwd()


#create window
w, h = 640, 480
window = game_engine.update.define("Box", w, h)

#variable stuff
run = True
clock = pygame.time.Clock()
x, y = 10, 150

#background
display = []
background = game_engine.properties_object("background", "{}/textures/black_bg.jpg".format(file_dir), 0, 0, w, h, False)
display += [background]

#sprites
display_sprite = []
box = game_engine.properties_object("box", "{}/textures/green.png".format(file_dir), 10, 10, 100, 100, True)
display_sprite += [box]
#foreground
foreground = []
#text foreground
text_foreground = []

#main game
def main_game(events):
    global text_foreground, x

    #input text
    if not keys[pygame.K_BACKSPACE]:
        for event in events:
            if event.type == pygame.KEYDOWN:
                pygame.time.delay(80)
                x += 20
                text = game_engine.properties_text(event.unicode.upper(), event.unicode.upper(), "WHITE", x, y, 30)
                text_foreground += [text]
    else:
        pygame.time.delay(80)
        del text_foreground[len(text_foreground) - 1]
        x -= 20

    #check with collision and then change the colour appropriatly
    if game_engine.mouse.collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], "box", display_sprite):
        #load in red and change its size
        red = pygame.image.load("{}/textures/red.png".format(file_dir))
        red = pygame.transform.scale(red, (100, 100))
        box.texture = red
    else:
        #load in green and change its size
        green = pygame.image.load("{}/textures/green.png".format(file_dir))
        green = pygame.transform.scale(green, (100, 100))
        box.texture = green
    
#main loop
while run:
    # keyboard and exit button, main code -----------------------------
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    

    if keys[pygame.K_ESCAPE]:       #exit if esc key has been pressed
        run = False
    main_game(events)
    
    game_engine.update.window(window, display, display_sprite, foreground, text_foreground, clock, 0)
    clock.tick(60)
    
pygame.quit()
print("Quiting...")
