""" game_functions.py
    for use in shifter.py """

import pygame
import sys
from pygame.sprite import Sprite, Group
from library import ColorShift as cs
from library import Settings, Player, Wall, EndBlock

def check_events(player, walls):
    """ Controls player movement """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            show_wall_clr(walls)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up = True
            elif event.key == pygame.K_DOWN:
                player.move_down = True
            elif event.key == pygame.K_RIGHT:
                player.move_right = True
            elif event.key == pygame.K_LEFT:
                player.move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.move_up = False
            elif event.key == pygame.K_DOWN:
                player.move_down = False
            elif event.key == pygame.K_RIGHT:
                player.move_right = False
            elif event.key == pygame.K_LEFT:
                player.move_left = False


def update_screen(ai_settings, bg_color, screen, end_block, player, walls,
                  labels):
    """ Draws and reveals all game elements """
    screen.fill(bg_color)
    #draw_grid(screen, ai_settings.tile_size)
    end_block.blitme()
    walls.draw(screen)
    labels.draw(screen)
    player.blitme()
        
    pygame.display.flip()

def update_game(ai_settings, screen, running, clock, shift_types, bg_color,
                player, walls, end_block, labels):
    """ Updates all elements of game"""
    clock.tick(ai_settings.framerate)
    check_events(player, walls)
    player.update(walls)
    walls.update()
    labels.update()
    running = end_collision(running, player, end_block)
    
    # Base off shift_type
    for shift_type in shift_types:
        if shift_type == "x":
            cs.change_mono_x(ai_settings, bg_color, player)
        elif shift_type == "y":
            cs.change_mono_y(ai_settings, bg_color, player)
        elif shift_type == "xy":
            cs.change_color_xy(ai_settings, bg_color, player)
        else:
            pass

    # Update dynamic walls
    cs.change_group_mono(ai_settings, walls, player)
    #change_wall_clr(ai_settings, player, walls)
    
    update_screen(ai_settings, bg_color, screen,
                     end_block, player, walls, labels)
    return running
'''
def change_color_x(ai_settings, color, player, show_value=False):
    """ Changes background color
        based on player's x position """
    color_value_x = int(player.rect.x / ai_settings.unit)

    color[0] = color_value_x
    color[1] = color_value_x
    color[2] = color_value_x
    
    if show_value:
        print(color[0])
    return color

def change_color_y(ai_settings, color, player, show_value=False):
    color_value_y = int(player.rect.y / ai_settings.unit)

    color[0] = color_value_y
    color[1] = color_value_y
    color[2] = color_value_y

    if show_value:
        print(color[0])
    return color

def change_color_xy(ai_settings, color, player, show_value=False):
    color_value = (int((player.rect.x / ai_settings.unit) / 3) +
                    int((player.rect.y / ai_settings.unit) / 3))
    
    color[0] = color_value
    color[1] = color_value
    color[2] = color_value

    print(color[0])
    return color

def change_wall_clr(ai_settings, player, walls, show_value=True):
    
    for wall in walls:
        if wall.type == wall.DYNAMIC_X:
            change_color_x(ai_settings, wall.color, player)
        elif wall.type == wall.DYNAMIC_Y:
            change_color_y(ai_settings, wall.color, player)
'''
def draw_grid(screen, size):
    """ Draws a grid based on tile_size """
    screen_rect = screen.get_rect()
    for x in range(0, screen_rect.width, size):
        pygame.draw.line(screen, (0, 0, 0), (x,0), (x, screen_rect.height))
    for y in range(0, screen_rect.height, size):
        pygame.draw.line(screen, (0, 0, 0), (0,y), (screen_rect.width, y))

def end_collision(running, player, end_block):
    """ Respond to player collisions with end block """
    if pygame.sprite.collide_rect(player, end_block):
        running = False
    return running

def show_wall_clr(walls):
    for wall in walls:
        if pygame.Rect.collidepoint(wall.rect, pygame.mouse.get_pos()):
            print(wall.color)

def wall_colorset(ai_settings):
    colorkeys = {}
    for i in range(ai_settings.tile_num_width):
        icon = ai_settings.icons[i]
        color = []
        for value in range(3):
            value = int(i*(ai_settings.tile_size/ai_settings.unit))
            color.append(value)
        colorkeys.update({icon:color})
        
    return colorkeys

def wall_hue_set(ai_settings):
    hue_keys = {}
    for i in range(6):
        icon = ai_settings.color_icons[i]
        color = ai_settings.colors[i]
        hue_keys.update({icon:color})

    return hue_keys

def level_maker(ai_settings, file_name, screen, player, end_block):
    walls = []
    map_data = []
    colorkeys = wall_colorset(ai_settings)
    hue_keys = wall_hue_set(ai_settings)
    
    with open(file_name, "r") as file:
        for line in file:
            map_data.append(line)
            
    for row, tiles in enumerate(map_data):
        for col, tile in enumerate(tiles):
            for icon, color in colorkeys.items():
                
                # Search for default tiles
                if tile == '0':
                    wall = Wall(ai_settings, screen, x=col, y=row)
                    walls.append(wall)
                    
                # Set player position
                elif tile == '@':
                    player.rect.x = col * ai_settings.tile_size
                    player.rect.y = row * ai_settings.tile_size

                # Set end position
                elif tile == '#':
                    end_block.rect.x = col * ai_settings.tile_size
                    end_block.rect.y = row * ai_settings.tile_size

                # Create colored walls
                elif tile == icon:
                    wall = Wall(ai_settings, screen, x=col,
                                y=row, color=color)
                    walls.append(wall)

                # Search for dynamic walls
                elif tile == "x":
                    wall = Wall(ai_settings, screen, x=col,
                                y=row)
                    wall.type = wall.DYNAMIC_X
                    walls.append(wall)

                elif tile == "y":
                    wall = Wall(ai_settings, screen, x=col,
                                y=row)
                    wall.type = wall.DYNAMIC_Y
                    walls.append(wall)

            for icon, color in hue_keys.items():
                if tile == icon:
                    wall = Wall(ai_settings, screen, x=col,
                                y=row, color=color)
                    walls.append(wall)

    return walls
