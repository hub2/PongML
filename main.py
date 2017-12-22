import sys, pygame
pygame.init()
screen = pygame.display.set_mode(size)

size = width, height = 640, 480
black = 0, 0, 0
white = 255,255,255

game_speed = 1
ball_radius = 6
paddle_width = 15
paddle_height = 90

class Ball:
    def __init__(self, screen, color=(0,0,0), pos=(0,0), radius=5):
        self.color = color
        self.pos = pos
        self.radius = radius
        self.screen = screen
        self.direction = (1,1)

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)

    def move(self):
        self.pos = (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])

    def flip_direction_x(self):
        self.direction = (self.direction[0]*(-1), self.direction[1])

    def flip_direction_y(self):
        self.direction = (self.direction[0], self.direction[1]*(-1))


class Paddle:
    def __init__(self, screen, color=(0,0,0), rect=(0,0,10,10)):
        self.color = color
        self.rect = rect
        self.screen = screen
        self.direction_up = 0
        self.direction_down = 0

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def move(self):
        tmp = list(self.rect)
        tmp[1] += (self.direction_up + self.direction_down)*game_speed
        self.rect = tuple(tmp)
    
    def set_direction_up(self):
        self.direction_up = -1

    def set_direction_down(self):
        self.direction_down = 1

    def stop_up(self):
        self.direction_up = 0

    def stop_down(self):
        self.direction_down = 0



b = Ball(screen, color=white, pos=(width//2, height//2), radius=ball_radius)
p1 = Paddle(screen, color=white, rect=(paddle_width+2*ball_radius, height//2 - paddle_height//2, paddle_width, paddle_height))
p2 = Paddle(screen, color=white, rect=(width - (2*paddle_width+2*ball_radius), height//2 - paddle_height//2, paddle_width, paddle_height))

move_map = {
    pygame.K_w: p1.set_direction_up, 
    pygame.K_a: p1.set_direction_down, 
    pygame.K_p: p2.set_direction_up, 
    pygame.K_l: p2.set_direction_down, 
}

stop_map = {
    pygame.K_w: p1.stop_up, 
    pygame.K_a: p1.stop_down,
    pygame.K_p: p2.stop_up,
    pygame.K_l: p2.stop_down,
}

            
def draw():
    screen.fill(black)
    b.draw()
    p1.draw()
    p2.draw()

def move():
    b.move()
    p1.move()
    p2.move()

k = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYUP:
            if event.key in stop_map:
                stop_map[event.key]()
        if event.type == pygame.KEYDOWN:
            if event.key in move_map:
                move_map[event.key]()

    draw()
    if k%5 == 0:
        move()

    k+=1

    pygame.display.flip()
