from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

grass_color = color.rgb(1, 235, 113)
stone_color = color.rgb(138,141,143)
dirt_color = color.rgb(200, 157, 124)

block_pick = 1

def update():
    if held_keys['escape']:
        quit()
    
    if player.position == Vec3(x, -80, z):
        quit()

    global block_pick

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3

class Voxel(Button):
    def __init__(self, position = (0,0,0), color = color.white):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color,
            highlight_color = color,
                    )

    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                if block_pick == 1:voxel = Voxel(position = self.position + mouse.normal, color = grass_color)
                if block_pick == 2:voxel = Voxel(position = self.position + mouse.normal, color = stone_color)
                if block_pick == 3:voxel = Voxel(position = self.position + mouse.normal, color = dirt_color)
            if key == 'left mouse down':
                destroy(self)
            
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = 'sky_default.jpg',
            scale = 150,
            double_sided = True
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/arm',
            scale = 0.2,
            color = color.rgb(255, 213, 200),
            rotation = Vec3(150,-10,0),
            position = Vec2(0.4, -0.6)
        )

    def active(self):
        self.position = Vec2(0.3,-0.5)
    def passive(self):
        self.position = Vec2(0.4,-0.6)

for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x,0,z), color = grass_color)

for y in range(3):
    for x in range(20):
        for z in range(20):
            voxel = Voxel(position=(x,y + -3,z), color = dirt_color)

player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()