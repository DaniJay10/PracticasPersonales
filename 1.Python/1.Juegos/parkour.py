from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

app = Ursina(borderless=False)
random.seed(0)
window.size=(600,600)
Entity.default_shader=lit_with_shadows_shader

player = FirstPersonController()

class Cubo(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            position=position,
            model="cube",
            scale=(1,1),
            origin_y= -.5,
            color = color.light_gray,
            collider="box",
            )
        
player.position = Vec3(0,2,0)            
Cubo(position=(0,1,0))
     

        
for z in range(30):
    cubo = Cubo(position=(random.randint(1,4),1,z))
    if z==29:
       cubo.color = color.green

ground = Entity(model="plane", collider="box", color= color.red)
ground.position = Vec3(0,-20,0)

def update():
    if(player.position.y <= -10):
        player.position = Vec3(0,10,0)

def input(key):
    if key == "escape":
        quit()

Sky()

app.run()
