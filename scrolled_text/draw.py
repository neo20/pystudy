import pyglet
window = pyglet.window.Window()
label = pyglet.text.Label(u'你好 世界 你好 世界',
                          font_name = '宋体-简',
                          font_size = window.height*0.6,
                          x=window.width//2 , y=window.height//2+ 50,
                          anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.draw()

def update(dt):
	label.x -= dt * 200
	if (label.x) < -1000:
		label.x = 0
	print(dt)

pyglet.clock.schedule_interval(update, 0.02)	
pyglet.app.run()

