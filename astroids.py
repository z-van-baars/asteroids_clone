import pygame as pg
import pygame.gfxdraw
from player import Player


pygame.init()
pygame.display.set_mode([0, 0])
pygame.display.set_caption("Astroids Clone v0.1")


key_color = (255, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)


class GameState(object):
    def __init__(self, screen_dimensions):
        self.screen_width = screen_dimensions[0]
        self.screen_height = screen_dimensions[1]
        self.screen = pygame.display.set_mode(screen_dimensions)
        self.clock = pg.time.Clock()
        self.player = Player()
        self.props = []
        self.particles = []
        self.projectiles = []


def keydown_handler(state, event):
    if event.key == pg.K_SPACE:
        state.player.fire()
    elif event.key == pg.K_w:
        state.player.thrusting = True
    elif event.key == pg.K_a:
        state.player.set_rotation(-1)
    elif event.key == pg.K_d:
        state.player.set_rotation(1)


def keyup_handler(state, event):
    if event.key == pg.K_w:
        state.player.thrusting = False

    elif event.key == pg.K_a or event.key == pg.K_d:
        state.player.set_rotation(0)


def event_handler(state):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.display.quit()
            pg.quit()
        if event.type == pg.KEYDOWN:
            return keydown_handler(state, event)

        if event.type == pg.KEYUP:
            keyup_handler(state, event)


def update(state):
    if state.player.rotation != 0:
        state.player.rotate_ship()
    if state.player.thrusting:
        state.player.thrust()


def physics_update(state):
    if state.player.thrusting:
        state.player.x += state.player.thrust_vector[0]
        state.player.y += state.player.thrust_vector[1]


def display_update(state):
    state.screen.fill(black)
    state.screen.blit(
        state.player.image,
        [state.player.x - 15, state.player.y - 15])
    for prop in state.props:
        state.screen.blit(prop.image, [prop.x, prop.y])
    for projectile in state.projectiles:
        state.screen.blit(projectile.image, [projectile.x, projectile.y])
    pg.display.flip()
    state.clock.tick(60)


state = GameState([800, 600])
state.player.x = int(
    state.screen_width / 2 - 15)
state.player.y = int(state.screen_height / 2 - 15)
while True:
    event_handler(state)
    update(state)
    physics_update(state)
    display_update(state)
