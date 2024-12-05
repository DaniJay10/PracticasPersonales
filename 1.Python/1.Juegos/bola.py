from ursina import *
import time
import random

game = Ursina()
player = Entity(model='sphere', color=color.yellow, position=(0, 3, -2000), scale=(5, 5, 5), collider='box')
camera.z = -15
camera.add_script(SmoothFollow(target=player, offset=(0, 5, -30)))
road = Entity(model='plane', scale=(50, 10, 1000000), color=color.black)
bullet = Entity(model='sphere')
rows = [-15, -10, -5, 0, 5, 10, 15]
median_r = Entity(model='cube', collider='box', position=(25, 2, 0), scale=(5, 10, 1000000), color=color.white)
median_l = Entity(model='cube', collider='box', position=(-25, 2, 0), scale=(5, 10, 1000000), color=color.white)
score_board = Text(text=str(0), scale=5, x=-0.85, y=0.45)
speed = 200

def update():
   player.z = player.z + time.dt * speed
   player.rotation_x = player.rotation_x + time.dt * 50
   score_val = player.z + 600
   score = int(score_val)
   global rows
   if held_keys['d']:
       player.x = player.x + time.dt * 25
       player.rotation_z = player.rotation_z + time.dt * 100
   if held_keys['a']:
       player.x = player.x - time.dt * 25
       player.rotation_z = player.rotation_z - time.dt * 100
   if held_keys['w']:
       player.z = player.z + time.dt * 1000
       player.rotation_x = player.rotation_x + time.dt * 600

   if player.intersects().hit or median_r.intersects().hit or median_l.intersects().hit:
       destroy(game)

   score_board.text = str(score)

for i in range(0, 100000, 100):
   enemy = Entity(model='cube', collider='box', position=(random.choice(rows), 6, i), color=color.random_color())
   enemy.scale = (10, 10, 10)

window.fullscreen = True
sky = Sky()
game.run()
