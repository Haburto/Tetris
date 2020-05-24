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
quit_game = False


def event_handler():
    global quit_game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True


def main():
    pygame.init()
    window_size = (800, 600)
    window = pygame.display.set_mode(window_size)
    window_fill_colour = (0, 0, 0)

    while not quit_game:
        window.fill(window_fill_colour)
        pygame.display.update()

        event_handler()

    pygame.quit()
    exit()


main()
