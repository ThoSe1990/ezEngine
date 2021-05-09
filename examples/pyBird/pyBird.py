#!/usr/bin/python3.8

import ezPyEngine
import time
import random

birdSize = ezPyEngine.Rectangle(0,0,130,105)
pipe_size = ezPyEngine.Rectangle(0,0,180,800)
pipe_gap = 200
pipe_spawn_x = 1920-130

future = 0

pipes = []

def createPipe(now , future):
    if now > future:
        
        pipe_top_spawn_y = pipe_size.h*random.uniform(0.1, 0.9) - pipe_size.h 
        pipe_bottom_spawn_y = pipe_top_spawn_y + pipe_size.h + pipe_gap

        pipe_top = ezPyEngine.CreateEntity()
        ezPyEngine.Sprite.Create(pipe_top, "pipe_top", ezPyEngine.Rectangle(0,0,261,1000), ezPyEngine.Rectangle(0,0,0,0), ezPyEngine.Sprite.Flip.none, ezPyEngine.Sprite.Layer.layer_1)
        ezPyEngine.Transform.Create(pipe_top, pipe_spawn_x, int(pipe_top_spawn_y), pipe_size.w, pipe_size.h, ezPyEngine.Vector2d(-250,0), 1)
        ezPyEngine.Collider.Create(pipe_top, 1.0, "pipe", 1)

        pipes.append(pipe_top)
        
        pipe_bottom = ezPyEngine.CreateEntity()
        ezPyEngine.Sprite.Create(pipe_bottom, "pipe_bottom", ezPyEngine.Rectangle(0,0,261,1000), ezPyEngine.Rectangle(0,0,0,0), ezPyEngine.Sprite.Flip.none, ezPyEngine.Sprite.Layer.layer_1)
        ezPyEngine.Transform.Create(pipe_bottom, pipe_spawn_x, int(pipe_bottom_spawn_y),pipe_size.w, pipe_size.h, ezPyEngine.Vector2d(-250,0), 1)
        ezPyEngine.Collider.Create(pipe_bottom, 1.0, "pipe", 1)

        pipes.append(pipe_bottom)

        if (len(pipes) > 8) :
            popped = pipes.pop(0)
            ezPyEngine.RemoveAllComponents(popped)
            popped = pipes.pop(0)
            ezPyEngine.RemoveAllComponents(popped)
        return 1
    else :
        return 0


def update():
    if ezPyEngine.Inputs.MouseButtonLeftDown():
        ezPyEngine.Sprite.UpdateTextureId(player, "bird_up")
    else:
        ezPyEngine.Sprite.UpdateTextureId(player, "bird_down")
    
    if ezPyEngine.Collider.CollidesWithType(player) == "pipe" :
        ezPyEngine.Sprite.UpdateTextureId(player, "bird_dead")
    else :
        ezPyEngine.Update()
    


ezPyEngine.Initialize()
ezPyEngine.Initialize_sdl()

ezPyEngine.AddTexture("background", "./examples/pyBird/assets/images/background.png")
ezPyEngine.AddTexture("bird_up", "./examples/pyBird/assets/images/bird_up.png")
ezPyEngine.AddTexture("bird_down", "./examples/pyBird/assets/images/bird_down.png")
ezPyEngine.AddTexture("bird_dead", "./examples/pyBird/assets/images/bird_dead.png")
ezPyEngine.AddTexture("pipe_bottom", "./examples/pyBird/assets/images/pipe_bottom.png")
ezPyEngine.AddTexture("pipe_top", "./examples/pyBird/assets/images/pipe_top.png")
ezPyEngine.AddFont("font", "./examples/pyBird/assets/fonts/TakeChances.ttf", 75)


background = ezPyEngine.CreateEntity()
ezPyEngine.Sprite.Create(background, "background", ezPyEngine.Rectangle(0,0,1912,855), ezPyEngine.Rectangle(0,0,1920,1080), ezPyEngine.Sprite.Flip.none, ezPyEngine.Sprite.Layer.layer_0)

player = ezPyEngine.CreateEntity()
ezPyEngine.Sprite.Create(player, "bird_up", ezPyEngine.Rectangle(0,0,300,230), ezPyEngine.Rectangle(0,0,0,0), ezPyEngine.Sprite.Flip.none, ezPyEngine.Sprite.Layer.layer_1)
ezPyEngine.Transform.Create(player, birdSize, ezPyEngine.Vector2d(0,0), 1)
ezPyEngine.UserInput.Create(player, "./examples/pyBird/assets/scripts/playerMovement.lua")
ezPyEngine.Collider.Create(player, 0.5, "player", 1)


textlabel = ezPyEngine.CreateEntity()
ezPyEngine.Textlabel.Create(textlabel, "pyBird: an easy flappy bird!!!", ezPyEngine.Rectangle(20,50,200,50), "font", ezPyEngine.Color(255,255,255,255))


future = time.time() + 3

while ezPyEngine.IsRunning():
    ezPyEngine.ProcessInput()

    player_bird = ezPyEngine.Transform.GetComponent(player)

    if createPipe(time.time(), future) == 1 :
        future = time.time() + 3
    
    update()
    ezPyEngine.Render()


ezPyEngine.Destroy()
