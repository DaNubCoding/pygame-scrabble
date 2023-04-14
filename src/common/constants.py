from enum import Enum
import pygame

VEC = pygame.math.Vector2

FPS = 60
WIDTH, HEIGHT = SIZE = 800, 800
HSIZE = (WIDTH // 2, HEIGHT // 2)
TILE_SIZE = 44
TILE_MARGIN = 4

class Color(Enum):
    BG = (230, 230, 241)
    TILE_BG = (196, 196, 209)
    DL = (104, 162, 195)
    TL = (12, 103, 156)
    DW = (228, 162, 163)
    TW = (191, 78, 78)

BONUS_LOCATIONS = {
    (4, 1): Color.DL,
    (12, 1): Color.DL,
    (7, 3): Color.DL,
    (9, 3): Color.DL,
    (1, 4): Color.DL,
    (8, 4): Color.DL,
    (15, 4): Color.DL,
    (3, 7): Color.DL,
    (7, 7): Color.DL,
    (9, 7): Color.DL,
    (13, 7): Color.DL,
    (4, 8): Color.DL,
    (12, 8): Color.DL,
    (3, 9): Color.DL,
    (7, 9): Color.DL,
    (9, 9): Color.DL,
    (13, 9): Color.DL,
    (1, 12): Color.DL,
    (8, 12): Color.DL,
    (15, 12): Color.DL,
    (7, 13): Color.DL,
    (9, 13): Color.DL,
    (4, 15): Color.DL,
    (12, 15): Color.DL,

    (6, 2): Color.TL,
    (10, 2): Color.TL,
    (2, 6): Color.TL,
    (6, 6): Color.TL,
    (10, 6): Color.TL,
    (14, 6): Color.TL,
    (2, 10): Color.TL,
    (6, 10): Color.TL,
    (10, 10): Color.TL,
    (14, 10): Color.TL,
    (6, 14): Color.TL,
    (10, 14): Color.TL,

    (2, 2): Color.DW,
    (3, 3): Color.DW,
    (4, 4): Color.DW,
    (5, 5): Color.DW,
    (14, 2): Color.DW,
    (13, 3): Color.DW,
    (12, 4): Color.DW,
    (11, 5): Color.DW,
    (14, 14): Color.DW,
    (13, 13): Color.DW,
    (12, 12): Color.DW,
    (11, 11): Color.DW,
    (2, 14): Color.DW,
    (3, 13): Color.DW,
    (4, 12): Color.DW,
    (5, 11): Color.DW,
    (8, 8): Color.DW,

    (1, 1): Color.TW,
    (15, 1): Color.TW,
    (15, 15): Color.TW,
    (1, 15): Color.TW,
    (8, 1): Color.TW,
    (15, 8): Color.TW,
    (8, 15): Color.TW,
    (1, 8): Color.TW,
}