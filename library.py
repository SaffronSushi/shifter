""" library.py
    contains classes for shifter.py """

import pygame, math
from pygame.sprite import Sprite, Group

# SETTINGS
class Settings():
    def __init__(self):
        # Screen settings
        self.screen_width = 512
        self.screen_height = 512

        # Icon
        self.icon = pygame.Surface((32, 32))
        self.icon.set_colorkey((0, 0, 0))
        pygame.draw.rect(self.icon, (255, 0, 0), (0, 0, 20, 20))
        pygame.draw.rect(self.icon, (0, 0, 255), (12, 12, 20, 20))

        self.tile_size = 32

        self.framerate = 60

        self.tile_num_width = int(self.screen_width / self.tile_size)

        # Get diagonal length of screen
        self.diagonal_length = int(math.hypot(self.screen_width,
                                              self.screen_height))

        # Convert screen size into units within color range
        self.unit = int(self.screen_width / 255)
        self.diagonal_unit = int(self.diagonal_length / 255)
        
        self.change_amount = ""


        self.bg_color = [0, 0, 0]
        
        self.icons = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                      'a', 'b', 'c', 'd', 'e', 'f', 'g']
        self.colors = [(100, 0, 0), (0, 100, 0), (0, 0, 100), (200, 150, 0),
                            (0, 100, 100), (200, 75, 0)]
        self.color_icons = ['R', 'G', 'B', 'V', 'Y', 'O']
# PLAYER
class Player(Sprite):
    def __init__(self, ai_settings, screen):
        super(Player, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.size = ai_settings.tile_size
        self.color = [255, 0, 0]
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False

        self.speed = 8
        self.dx = 0
        self.dy = 0

    def update(self, walls):
        
        # X movement        
        if self.move_right:
            self.dx = self.speed
        elif self.move_left:
            self.dx = -(self.speed)
        else:
            self.dx = 0
        self.rect.centerx += self.dx

        walls_hit = pygame.sprite.spritecollide(self, walls, False)
        for wall in walls_hit:
            if self.dx > 0:
                self.rect.right = wall.rect.left
            else:
                self.rect.left = wall.rect.right
        
        # Y movement
        if self.move_down:
            self.dy = self.speed
        elif self.move_up:
            self.dy = -(self.speed)
        else:
            self.dy = 0
        self.rect.centery += self.dy

        walls_hit = pygame.sprite.spritecollide(self, walls, False)
        for wall in walls_hit:
            if self.dy > 0:
                self.rect.bottom = wall.rect.top
            else:
                self.rect.top = wall.rect.bottom
        
        self.check_bounds()

    def check_bounds(self):
        # Screen collisions
        if self.rect.right > self.screen_rect.width:
            self.rect.right = self.screen_rect.width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > self.screen_rect.height:
            self.rect.bottom = self.screen_rect.height
        if self.rect.top < 0:
            self.rect.top = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)

# WALL
class Wall(Sprite):
    def __init__(self, ai_settings, screen, x=0, y=0, width=1, height=1,
                 color=[0,0,255]):
        super(Wall, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.size = ai_settings.tile_size
        self.width = width * self.size
        self.height = height * self.size
        self.color = color
        
        self.STANDARD = 0
        self.DYNAMIC_X = 1
        self.DYNAMIC_Y = 2
        self.type = self.STANDARD

        self.image = pygame.Surface((self.width, self.height))
        # If invalid color, print value
        try:
            self.image.fill(self.color)
        except TypeError:
            print(self.color)
            
        self.rect = self.image.get_rect()
        self.rect.x = x*self.size
        self.rect.y = y*self.size

    def update(self):
        self.image.fill(self.color)

    def blitme(self):
        self.screen.blit(self.image, self.screen)

# ENDBLOCK
class EndBlock(Wall):
    def __init__(self, ai_settings, screen, x=0, y=0, width=1,
                      height=1, color=[0,255,0]):
        Wall.__init__(self, ai_settings, screen, x=0, y=0, width=1,
                      height=1, color=[0,0,255])

    def blitme(self):
        self.screen.blit(self.image, self.rect)

# LABEL
class Label(Sprite):
    def __init__(self, screen, tile_size, x=0, y=0, font_size=30, text="",
                 color=[0,0,0]):
        """Initialize all aspects of label"""
        super(Label, self).__init__()
        self.screen = screen
        self.ts = tile_size
        self.fs = font_size
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont(None, self.fs)
        self.image = self.font.render(self.text, 1, self.color)
        self.rect = self.image.get_rect()

        self.rect.x = x*self.ts
        self.rect.y = y*self.ts

    def update(self):
        None
        #self.image = self.font.render(self.text, 1, self.color)        
        #self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class ColorShift():
    """ Contains all functions for changing
        color values """
    def change_mono_x(settings, color_obj, reference_obj,
                      show_value=False):
        """ Changes all values of specified object's color based on
            secondary object's x position """
        color_value_x = int(reference_obj.rect.x / settings.unit)
        color_obj[0] = color_value_x
        color_obj[1] = color_value_x
        color_obj[2] = color_value_x

        if show_value:
            print(color_obj[0])
        return color_obj

    def change_mono_y(settings, color_obj, reference_obj,
                      show_value=False):
        """ Changes all values of specified object's color based on
            secondary object's y position """
        color_value_y = int(reference_obj.rect.y / settings.unit)
        color_obj[0] = color_value_y
        color_obj[1] = color_value_y
        color_obj[2] = color_value_y

        if show_value:
            print(color_obj[0])
        return color_obj

    def change_mono_xy(settings, color_obj, reference_obj,
                      show_value=False):
        """ Changes all values of specified object's color based on
            secondary object's x and y position """
        color_value = (int((player.rect.x / ai_settings.unit) / 3) +
                       int((player.rect.y / ai_settings.unit) / 3))
        color_obj[0] = color_value_y
        color_obj[1] = color_value_y
        color_obj[2] = color_value_y

        if show_value:
            print(color_obj[0])
        return color_obj

    def change_group_mono(settings, color_objects, ref_obj,
                      show_value=False):
        """ Changes values of all objects in group, with different
                functions depending on obect type """
        for obj in color_objects:
            if obj.type == obj.DYNAMIC_X:
                ColorShift.change_mono_x(settings, obj.color, ref_obj)
            elif obj.type == obj.DYNAMIC_Y:
                ColorShift.change_mono_y(settings, obj.color, ref_obj)

    def reveal_group_clr(settings, color_objects, ref_obj,
                      show_value=False):
        """ Visibility of object is obscured by colored surface,
            with transparency set by reference object """
        pass
