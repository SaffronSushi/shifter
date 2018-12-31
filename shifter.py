import pygame
import sys
import game_functions as gf
from library import Settings, Player, Wall, EndBlock, Label, ColorShift
from pygame.sprite import Sprite, Group

def test(screen):
    pygame.display.set_caption("TEST")
    file_name = "levels/test.txt"
    ai_settings = Settings()
    
    player = Player(ai_settings, screen)
    end_block = EndBlock(ai_settings,screen)
    walls = gf.level_maker(ai_settings, file_name, screen, player, end_block)
    
    shift_types = [""]
    walls = Group(walls)
    labels = Group()
    bg_color = [0, 0, 0]
    running = True
    clock = pygame.time.Clock()
    while running:
        running = gf.update_game(ai_settings, screen, running, clock,
                  shift_types, bg_color, player, walls, end_block, labels)

def intro(screen):
    level_num = 0
    file_name = "levels/pt1_intro/intro_lvl.txt"
    ai_settings = Settings()
    ts = ai_settings.tile_size
    
    player = Player(ai_settings, screen)
    end_block = EndBlock(ai_settings,screen)
    walls = gf.level_maker(ai_settings, file_name, screen, player, end_block)
    label_1 = Label(screen, ts, text="PRESS ARROW KEYS TO MOVE",
                    color=[183,183,183])
    label_2 = Label(screen, ts, x=6, y=14, text="AND KEEP AN EYE OUT",
                    color=[24,24,24])

    shift_type = "x"
    walls = Group(walls)
    labels = Group(label_1, label_2)
    bg_color = [0, 0, 0]
    running = True
    clock = pygame.time.Clock()
    while running:
        running = gf.update_game(ai_settings, screen, running, clock,
                  shift_type, bg_color, player, walls, end_block, labels)

    level_num += 1
    return level_num

def end_level(screen):
    level_num = 0
    file_name = "levels/pt1_intro/intro_lvl.txt"
    ai_settings = Settings()
    ts = ai_settings.tile_size
    
    player = Player(ai_settings, screen)
    end_block = EndBlock(ai_settings,screen)
    walls = gf.level_maker(ai_settings, file_name, screen, player, end_block)
    label_1 = Label(screen, ts, text="END OF DEMO",
                    color=[183,183,183])
    label_2 = Label(screen, ts, x=4, y=14, text="Created by Andrew Durkee",
                    color=[24,24,24])

    shift_type = "x"
    walls = Group(walls)
    labels = Group(label_1, label_2)
    bg_color = [0, 0, 0]
    running = True
    clock = pygame.time.Clock()
    while running:
        running = gf.update_game(ai_settings, screen, running, clock,
                  shift_type, bg_color, player, walls, end_block, labels)
    sys.exit()
        
def level_1(screen):
    level_num = 1
    file_name = "levels/pt1_intro/level_1.txt"
    ai_settings = Settings()

    player = Player(ai_settings, screen)
    end_block = EndBlock(ai_settings,screen)
    walls = gf.level_maker(ai_settings, file_name, screen, player, end_block)

    shift_type = "x"
    walls = Group(walls)
    labels = Group()
    bg_color = [0, 0, 0]
    running = True
    clock = pygame.time.Clock()
    while running:
        running = gf.update_game(ai_settings, screen, running, clock,
                  shift_type, bg_color, player, walls, end_block, labels)

    level_num += 1
    return level_num

def level_2(screen):
    """ Introduce color changes for
        background and walls based
        on y position """
    level_num = 2
    file_name = "levels/pt1_intro/level_2.txt"
    ai_settings = Settings()

    player = Player(ai_settings, screen)
    end_block = EndBlock(ai_settings,screen)
    walls = gf.level_maker(ai_settings, file_name, screen, player, end_block)

    shift_type = "y"
    walls = Group(walls)
    labels = Group()
    bg_color = [0, 0, 0]
    running = True
    clock = pygame.time.Clock()
    while running:
        running = gf.update_game(ai_settings, screen, running, clock,
                  shift_type, bg_color, player, walls, end_block, labels)

    level_num += 1
    return level_num

def level_3(screen):
    level_num = 3
    file_name = "levels/pt1_intro/level_3.txt"
    ai_settings = Settings()

    player = Player(ai_settings, screen)
    end_block = EndBlock(ai_settings,screen)
    walls = gf.level_maker(ai_settings, file_name, screen, player, end_block)

    shift_type = "xy"
    walls = Group(walls)
    labels = Group()
    bg_color = [0, 0, 0]
    running = True
    clock = pygame.time.Clock()
    while running:
        running = gf.update_game(ai_settings, screen, running, clock,
                  shift_type, bg_color, player, walls, end_block, labels)

    level_num += 1
    return level_num

def level_4(screen):
    level_num = 4
    file_name = "levels/pt2_dyn_walls/level_4.txt"
    ai_settings = Settings()

    player = Player(ai_settings, screen)
    end_block = EndBlock(ai_settings,screen)
    walls = gf.level_maker(ai_settings, file_name, screen, player, end_block)

    shift_type = ""
    walls = Group(walls)
    labels = Group()
    bg_color = [224, 224, 224]
    running = True
    clock = pygame.time.Clock()
    while running:
        running = gf.update_game(ai_settings, screen, running, clock,
                  shift_type, bg_color, player, walls, end_block, labels)

    level_num += 1
    return level_num

def level_5(screen):
    level_num = 5
    file_name = "levels/pt2_dyn_walls/level_5.txt"
    ai_settings = Settings()

    player = Player(ai_settings, screen)
    end_block = EndBlock(ai_settings,screen)
    walls = gf.level_maker(ai_settings, file_name, screen, player, end_block)

    shift_type = "y"
    walls = Group(walls)
    labels = Group()
    bg_color = [224, 224, 224]
    running = True
    clock = pygame.time.Clock()
    while running:
        running = gf.update_game(ai_settings, screen, running, clock,
                  shift_type, bg_color, player, walls, end_block, labels)

    level_num += 1
    return level_num

def level_6(screen):
    level_num = 6
    file_name = "levels/pt3_clr_inv_walls/level_6.txt"
    ai_settings = Settings()

    player = Player(ai_settings, screen)
    end_block = EndBlock(ai_settings,screen)
    walls = gf.level_maker(ai_settings, file_name, screen, player, end_block)

    shift_type = ""
    walls = Group(walls)
    labels = Group()
    bg_color = [240, 240, 240]
    running = True
    clock = pygame.time.Clock()
    while running:
        running = gf.update_game(ai_settings, screen, running, clock,
                  shift_type, bg_color, player, walls, end_block, labels)

    level_num += 1
    return level_num

def level_7(screen):
    level_num = 7
    file_name = "levels/pt3_clr_inv_walls/level_7.txt"
    ai_settings = Settings()

    player = Player(ai_settings, screen)
    end_block = EndBlock(ai_settings,screen)
    walls = gf.level_maker(ai_settings, file_name, screen, player, end_block)

    shift_type = ""
    walls = Group(walls)
    labels = Group()
    bg_color = [240, 240, 240]
    running = True
    clock = pygame.time.Clock()
    while running:
        running = gf.update_game(ai_settings, screen, running, clock,
                  shift_type, bg_color, player, walls, end_block, labels)

    level_num += 1
    return level_num

def level_8(screen):
    level_num = 8
    file_name = "levels/pt3_clr_inv_walls/level_8.txt"
    ai_settings = Settings()

    player = Player(ai_settings, screen)
    end_block = EndBlock(ai_settings,screen)
    walls = gf.level_maker(ai_settings, file_name, screen, player, end_block)

    shift_type = ""
    walls = Group(walls)
    labels = Group()
    bg_color = [240, 240, 240]
    running = True
    clock = pygame.time.Clock()
    while running:
        running = gf.update_game(ai_settings, screen, running, clock,
                  shift_type, bg_color, player, walls, end_block, labels)

    level_num += 1
    return level_num

def level_9(screen):
    level_num = 9
    file_name = "levels/pt3_clr_inv_walls/level_9.txt"
    ai_settings = Settings()

    player = Player(ai_settings, screen)
    end_block = EndBlock(ai_settings,screen)
    walls = gf.level_maker(ai_settings, file_name, screen, player, end_block)

    shift_type = ""
    walls = Group(walls)
    labels = Group()
    bg_color = [240, 240, 240]
    running = True
    clock = pygame.time.Clock()
    while running:
        running = gf.update_game(ai_settings, screen, running, clock,
                  shift_type, bg_color, player, walls, end_block, labels)

    level_num += 1
    return level_num

def level_10(screen):
    level_num = 10
    file_name = "levels/pt3_clr_inv_walls/level_10.txt"
    ai_settings = Settings()

    player = Player(ai_settings, screen)
    end_block = EndBlock(ai_settings,screen)
    walls = gf.level_maker(ai_settings, file_name, screen, player, end_block)

    shift_type = ""
    walls = Group(walls)
    labels = Group()
    bg_color = [240, 240, 240]
    running = True
    clock = pygame.time.Clock()
    while running:
        running = gf.update_game(ai_settings, screen, running, clock,
                  shift_type, bg_color, player, walls, end_block, labels)

    level_num += 1
    return level_num

def level_11(screen):
    level_num = 11
    file_name = "levels/pt4_mono_inv_walls/level_11.txt"
    ai_settings = Settings()

    player = Player(ai_settings, screen)
    end_block = EndBlock(ai_settings,screen)
    walls = gf.level_maker(ai_settings, file_name, screen, player, end_block)

    shift_type = ""
    walls = Group(walls)
    labels = Group()
    bg_color = [240, 240, 240]
    running = True
    clock = pygame.time.Clock()
    while running:
        running = gf.update_game(ai_settings, screen, running, clock,
                  shift_type, bg_color, player, walls, end_block, labels)

    level_num += 1
    return level_num

def level_12(screen):
    level_num = 12
    file_name = "levels/pt4_mono_inv_walls/level_12.txt"
    ai_settings = Settings()

    player = Player(ai_settings, screen)
    end_block = EndBlock(ai_settings,screen)
    walls = gf.level_maker(ai_settings, file_name, screen, player, end_block)

    shift_type = ""
    walls = Group(walls)
    labels = Group()
    bg_color = [16, 16, 16]
    running = True
    clock = pygame.time.Clock()
    while running:
        running = gf.update_game(ai_settings, screen, running, clock,
                  shift_type, bg_color, player, walls, end_block, labels)

    level_num += 1
    return level_num
#NOTE:
#WALLS NEED TO DISAPPEAR WHEN MOVING RIGHT, NOT VICE-VERSA


def main():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("SHIFTER")
    pygame.display.set_icon(ai_settings.icon)
    level_names = [intro, level_1, level_2, level_3, level_4, level_5,
                   level_6, level_7, level_8, level_9, level_10, level_11,
                   level_12,
                   end_level]

    level_num = 0
    
    while True:
        level_num = level_names[level_num](screen)
        #test(screen)

main()
