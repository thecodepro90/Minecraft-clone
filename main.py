from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

all_blocks_texture = load_texture('assets/allblocks.png')

grass_color = color.rgb(1, 235, 113)
stone_color = color.rgb(138,141,143)
dirt_color = color.rgb(200, 157, 124)
brick_color = color.rgb(212, 77, 77)
hand_color = color.rgb(255, 213, 200)
water_color = color.rgb(0, 138, 255)
wood_color = color.rgb(255, 149, 116)

block_pick = 1
def update():
    player_y = round(player.position.y)
    if player_y == -10:
        quit()
    
    if held_keys['escape']:
        quit()

    global block_pick

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if held_keys['5']: block_pick = 5
    if held_keys['6']: block_pick = 6

    if held_keys['e']:
        all.visible = True
    else:
        all.visible = False

class Voxel(Button):
    def __init__(self, position = (0,0,0), color = color.white, texture = 'white_cube'):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = texture,
            color = color,
            highlight_color = color,
                    )

    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                if block_pick == 1:voxel = Voxel(position = self.position + mouse.normal, color = grass_color)
                if block_pick == 2:voxel = Voxel(position = self.position + mouse.normal, color = stone_color)
                if block_pick == 3:voxel = Voxel(position = self.position + mouse.normal, color = dirt_color)
                if block_pick == 4:voxel = Voxel(position = self.position + mouse.normal, color = brick_color, texture = 'brick')
                if block_pick == 5:voxel = Voxel(position = self.position + mouse.normal, color = water_color)
                if block_pick == 6:voxel = Voxel(position = self.position + mouse.normal, color = wood_color)
            if key == 'left mouse down':
                destroy(self)
            
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = 'sky_default.jpg',
            scale = 175,
            double_sided = True
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/arm',
            scale = 0.2,
            color = hand_color,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.4, -0.6)
        )

    def active(self):
        self.position = Vec2(0.3,-0.5)
    def passive(self):
        self.position = Vec2(0.4,-0.6)

class All_blocks(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            texture = all_blocks_texture,
            position = Vec2(0,0),
            scale = 0.75
        )

def generate_world():
    for z in range(20):
        for x in range(20):
            voxel = Voxel(position=(x,0,z), color = grass_color)

    for y in range(3):
        for x in range(20):
            for z in range(20):
                voxel = Voxel(position=(x,y + -3,z), color = dirt_color)

generate_world()

player = FirstPersonController()
sky = Sky()
hand = Hand()
all = All_blocks()


app.run()