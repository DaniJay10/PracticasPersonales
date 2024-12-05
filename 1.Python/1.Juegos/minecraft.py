from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina(borderless=False)
window.size=(800,800)

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            origin_y=0.5,
            texture="grass",
            color = color.rgb(255,255,255),
            highlight_color= color.lime,
            )
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                voxel = Voxel(position= self.position + mouse.normal)
            if key == "right mouse down":
                destroy(self)

chunkSize = 28

for z in range(chunkSize):
    for x in range(chunkSize):
        voxel=Voxel(position=(x,0,z))

player = FirstPersonController()
player.position = Vec3(0,2,0)  
def update():
    if(player.position.y <= -10):
        player.position = Vec3(0,10,0)
def input(key):
    if key == "escape":
        quit()


app.run()
