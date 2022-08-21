import random
import ursina

def input(key):
    global snake, random_pos
    
    
    if key == 'd':
        snake.x += 1 * random_pos
    if key == 'q':
        snake.x -= 1 * random_pos
    if key == 's':
        snake.y -= 1 * random_pos
        
def update():
    global snake

    while input is False:
        snake.x += 0.25

app = ursina.Ursina()

snake = ursina.Entity(model="quad", scale=0.5, collider='box', color = ursina.color.white, position=(0,0))

random_pos = random.randint(0, 3)

fruit = ursina.Entity(model="quad", collider="box",color=ursina.color.green, position=(random_pos, random_pos), scale=0.25)

if __name__ == "__main__":
    app.run()
