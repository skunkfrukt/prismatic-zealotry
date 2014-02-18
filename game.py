import pyglet
from src import tilemap, pluckylass
from src.shapes import *
from pyglet.window import key
from pyglet.gl import *

pyglet.resource.path.append('data')
pyglet.resource.reindex()

testmap, testmapview = tilemap.load('testmap.json')
testmap.setup()
testmapview.setup()

player = pluckylass.PluckyLass()
playerview = pluckylass.PluckyLassView(player)
playerview.setup()

SCALE = 2

w = pyglet.window.Window(13*15*SCALE, 13*15*SCALE, 'Prismatic Zealotry')
glScalef(SCALE, SCALE, SCALE)

@w.event
def on_draw():
    w.clear()
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    testmapview.batch.draw()
    playerview.sprite.draw()

@w.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        player.direction = 'N'
    elif symbol == key.RIGHT:
        player.direction = 'E'
    elif symbol == key.DOWN:
        player.direction = 'S'
    elif symbol == key.LEFT:
        player.direction = 'W'

@w.event
def on_key_release(symbol, modifiers):
    player.direction = None

def mupdate(dt):
    testmap.update_passability_map()
    # Check if moving entities push others
    # Move all mobile entities
    # Update hue map
    # Match 3
    player.mupdate(dt)
    col, row = player.position + player.delta
    if not testmap.obstacle_at(col, row):
        player.position += player.delta
    elif testmap.tile_at(col, row).pushable and not testmap.obstacle_at(*(player.position + player.delta * 2)):
        testmap.shift_tile(col, row, player.delta)
        player.position += player.delta
        testmap.update_hue_map()
        testmap.match_3(col + player.delta.x, row + player.delta.y)

def vupdate(dt):
    chunk_x = (player.position.x // 13) * 15 * 13
    chunk_y = (player.position.y // 13) * 15 * 13
    screen_offset = Vect(-chunk_x, -chunk_y)
    testmapview.update_sprite_position(screen_offset)
    playerview.vupdate(screen_offset)

pyglet.clock.schedule_interval(mupdate, 0.1)
pyglet.clock.schedule(vupdate)

pyglet.app.run()