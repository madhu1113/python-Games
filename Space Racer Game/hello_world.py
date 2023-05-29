import pyglet

new_window = pyglet.window.Window()     # create an object of pyglet Window class

label = pyglet.text.Label('Hello world !',          # Text to display
                           font_name = 'copper',    # font of text
                           font_size = 16,          # size of font
                           x = new_window.width//2, # x-coordinate
                           y = new_window.height//2,#y- coordinate
                           anchor_x = 'center',      #Position of x-coordinate 
                           anchor_y = 'center')        # position of y-coordinate

@new_window.event           # Decorator--> To run the API. as soon as this event is invoked it will run the on_draw() function.
def  on_draw():
    new_window.clear()      # Clear the window
    label.draw()               # text will be shown using draw() function

pyglet.app.run()            # run the pyglet app