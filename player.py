import math
import pygame as pg
import pygame.gfxdraw

key_color = (255, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)


def rotate(origin, point, angle):
    """angle should be given in radians"""
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


class Player(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.facing = 0
        self.rotation = 0
        self.thrusting = False

        self.ship_pts = [(15, 0), (6, 30), (15, 22), (24, 30)]

        self.redraw_ship()

    def redraw_ship(self):
        image = pg.Surface([30, 30])
        image.fill(key_color)
        image.set_colorkey(key_color)
        image = image.convert_alpha()
        pygame.gfxdraw.aapolygon(image, self.ship_pts, (white))
        self.image = image

    def set_rotation(self, direction):
        self.rotation = direction

    def rotate_points(self):
        rotated_points = []
        for pt in self.ship_pts:
            rotated_pt = rotate([15, 15], pt, math.radians(self.rotation))
            rotated_points.append(rotated_pt)
        self.ship_pts = rotated_points

    def rotate_ship(self):
        self.facing += self.rotation
        self.rotate_points()
        self.redraw_ship()

    def set_thrust_vector(self):
        pass

    def thrust(self):
        self.thrust_vector = self.set_thrust_vector()
