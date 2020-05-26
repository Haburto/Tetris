import pygame

# CTRL + ALT + L    // format everything in pycharm


# Tetris - game logic
# I want to have a level system, each level the gamespeed increases a certain amount which affects the total score
# How many blocks can fit in the x axis? probably 6 to 8 ?

# TODO: read up on abstract classes and inheritance in python
# BLOCKS available: 7
# square, L, backward L, straight line, small T, stair, backward star

# SCORE (from wiki)
# one line rewards 100 pts, four lines rewards 800 pts (called tetris)
# each subsequent back-to-back tetris awards 1200 pts
# each level has a different score-multiplier

# UI
# HOTKEYS
# arrows keys: left / right to move that way, up to turn the block, and down for a hard-drop
# p: to pause
# r: to reset

# TODO: implement main window
# TODO: implement grid system
# TODO: implement UI
# TODO: pre implement all classes
# TODO: class Block
# TODO: class FOR EACH PIECE - see game logic comment
# TODO: implement gameplay loop - see game logic comment
# TODO: implement hotkey support
# TODO: implement logic
# TODO: add a title
# TODO: add a logo
# TODO: add background music
# TODO: add sound effects for ingame events
# TODO: (maybe) add a background image
window_size = (1200, 800)
game_area_size = (window_size[0] * 1 // 2, window_size[1] * 4 // 5)  # 2/3 of the width, 4/5 of the height

window_fill_colour = (10, 50, 10)
game_area_color = (150, 150, 150)

window = pygame.display.set_mode(window_size)

quit_game = False


def draw_game_area():
    """Draws the game area."""
    game_area_x_start = (window_size[0] - game_area_size[0]) // 2
    game_area_y_start = (window_size[1] - game_area_size[1]) // 2
    game_area_xy_start = (game_area_x_start, game_area_y_start)

    pygame.draw.rect(window,
                     game_area_color,
                     (game_area_xy_start[0], game_area_xy_start[1], game_area_size[0], game_area_size[1])
                     )


def test_method():
    """This method only exists to test new implementations - delete it later!"""
    pass


def surface_handler():
    """Calls all other surface affecting methods."""
    window.fill(window_fill_colour)
    draw_game_area()
    # TEST AREA START - # TODO: refactor and delete this part later! Do not forget!
    test_method()
    # TEST AREA END
    pygame.display.update()


def event_handler():
    """Handles game events like keyboard and mouse input."""
    global quit_game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True


def main():
    while not quit_game:
        event_handler()
        surface_handler()

    pygame.quit()
    exit()


pygame.init()
main()
