#zoom test
from engine import game_engine_240123 as engine
import pygame, os
Canvas = engine.Canvas

file_dir = os.getcwd()
debug_file = open("debug.txt", "a")

#create window
w, h = 1280, 720
window = engine.window("Mesh testing", w, h)

#variables
run = True
clock = pygame.time.Clock()

#camera and player speeds
canvasSpeed = 5
playerSpeed = 5

#lists
display = []
for x in range(5):
    ground = engine.properties_object("ground", f"{file_dir}/textures/rock_brown.png", x * 64 * 3, h/2, 64 * 3, 64 * 3, True)
    display += [ground]

#display_sprite
display_sprite = []
player = engine.properties_object("player", f"{file_dir}/textures/player.png", w/2, h/2, 64, 64, True)
display_sprite += [player]

def main():
    #player movement
    if keys[pygame.K_w]:
        if engine.object.up(player, playerSpeed, 0):
            Canvas.offsetY -= playerSpeed
            engine.object.up(player, playerSpeed, 0)

    elif keys[pygame.K_s]:
        if engine.object.down(player, playerSpeed, h - 64):
            Canvas.offsetY += playerSpeed
            engine.object.down(player, playerSpeed, h - 64)

    if keys[pygame.K_a]:
        if engine.object.left(player, playerSpeed, 0):
            Canvas.offsetX -= playerSpeed
            engine.object.left(player, playerSpeed, 0)
        
    elif keys[pygame.K_d]:
        if engine.object.right(player, playerSpeed, w - 64):
            Canvas.offsetX += playerSpeed
            engine.object.right(player, playerSpeed, w - 64)

    player.x = pygame.mouse.get_pos()[0] - (24 * 3) / 2
    player.y = pygame.mouse.get_pos()[1] - (24 * 3) / 2
    
    #camera movement
    if keys[pygame.K_i]:
        Canvas.offsetY -= canvasSpeed
    if keys[pygame.K_k]:
        Canvas.offsetY += canvasSpeed
    if keys[pygame.K_j]:
        Canvas.offsetX -= canvasSpeed
    if keys[pygame.K_l]:
        Canvas.offsetX += canvasSpeed

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    
    main()

    """
    #current new method before putting into game_engine
    for object in display:
        offsetX = object.x - player.x
        offsetY = object.y - player.y
        if player.mask.overlap(object.mask, (offsetX, offsetY)):
            print("Collision")
    """
    """
    #old method of how to find a collision
    collide = False
    for index in range(len(display)):
        if engine.object.collision_rect(player, display, index) != None:
            collide = True

    if collide:
        print("Collision")
    else:
        print("No Collision!")
    """
    
    #new method with game_engine implimentation
    if engine.object.collision_mask(player, display) != None:
        print("Collision!")
    else:
        print("No collision!")
    
    #engine.window.writeDebug_file(debug_file, display, display_sprite, [], [], clock)
    engine.window.update(window, display, display_sprite, None, None, clock)
    clock.tick()
    
pygame.quit()
debug_file.close()