from typing import Generator
import pygame

from src.common.constants import VEC, Color, TILE_SIZE, TILE_MARGIN, BONUS_LOCATIONS, BONUS_FONT, AXIS_FONT
from src.game.button import Button1, Button2
from src.game.container import Container
from src.management.scene import Scene
import src.common.images as images

class MainGame(Scene):
    def setup(self) -> None:
        super().setup()
        self._board = [[None] * 15 for _ in range(15)]

        self.rack_container = Container(self, (40, 780, (TILE_SIZE + TILE_MARGIN) * 15 - TILE_MARGIN, 105))
        self.rack_container.setup(
            bg_color = (255, 255, 255),
            border_radius = 12,
        )

        top = "100% - 30p"

        self.rack_container.add_children(ele := Button1(self, (15, 15, ..., top), images.shuffle, lambda: print("shuffle")))
        ele.setup(
            bg_color = Color.RACK_BUTTON_IDLE.value,
            border_radius = 12,
        )

        self.rack_container.add_children(ele := Container(self, ("$ + 15p", 15, "100% - $ - $ - 30p - 30p", top)))
        ele.setup(
            bg_color = Color.BG.value,
            border_radius = 12,
        )

        self.rack_container.add_children(ele := Button1(self, ("$ + 15p", 15, ..., top), images.reset, lambda: print("reset")))
        ele.setup(
            bg_color = Color.RACK_BUTTON_IDLE.value,
            border_radius = 12,
        )

        self.options_container = Container(self, (VEC(self.rack_container.rect.topleft) + (0, 120), VEC(self.rack_container.rect.size) - (0, 40)))

        self.options_container.add_children(ele := Button2(self, (0, 0, "25% - 11p", "100%"), "Resign", lambda: print("resign")))
        ele.setup(
            bg_color = Color.RACK_BUTTON_IDLE.value,
            fg_color = (0, 0, 0),
            border_radius = 9,
        )

        self.options_container.add_children(ele := Button2(self, ("$ + 15p", 0, "25% - 11p", "100%"), "Skip", lambda: print("skip")))
        ele.setup(
            bg_color = Color.RACK_BUTTON_IDLE.value,
            fg_color = (0, 0, 0),
            border_radius = 9,
        )

        self.options_container.add_children(ele := Button2(self, ("$ + 15p", 0, "25% - 11p", "100%"), "Swap", lambda: print("swap")))
        ele.setup(
            bg_color = Color.RACK_BUTTON_IDLE.value,
            fg_color = (0, 0, 0),
            border_radius = 9,
        )

        self.options_container.add_children(ele := Button2(self, ("$ + 15p", 0, "25% - 11p", "100%"), "Submit", lambda: print("submit")))
        ele.setup(
            bg_color = Color.SUBMIT_BUTTON_IDLE.value,
            fg_color = (255, 255, 255),
            border_radius = 9,
        )

    def update(self) -> None:
        super().update()

    def draw(self) -> None:
        self.manager.screen.fill(Color.BG.value)

        self.draw_board()
        self.draw_axes()

        super().draw()

    def draw_board(self) -> None:
        for x, y, tile in self.board:
            pos = VEC(40 + x * (TILE_SIZE + TILE_MARGIN), 40 + y * (TILE_SIZE + TILE_MARGIN))
            color = BONUS_LOCATIONS[(x + 1, y + 1)] if (x + 1, y + 1) in BONUS_LOCATIONS else Color.TILE_BG
            pygame.draw.rect(self.manager.screen, color.value, (*pos, TILE_SIZE, TILE_SIZE), 0, 7)
            if color != Color.TILE_BG:
                if (x, y) == (7, 7):
                    self.manager.screen.blit(images.star, pos)
                    continue
                text_surf = BONUS_FONT.render(color.name, True, (255, 255, 255))
                self.manager.screen.blit(text_surf, pos + (VEC(TILE_SIZE) - text_surf.get_size()) // 2)

    def draw_axes(self) -> None:
        for i in range(15):
            text_surf = AXIS_FONT.render(chr(65 + i), True, Color.AXIS_TEXT.value)
            self.manager.screen.blit(text_surf, (58 + i * (TILE_SIZE + TILE_MARGIN), 22))

        for i in range(15):
            text_surf = AXIS_FONT.render(f"{i + 1: >2}", True, Color.AXIS_TEXT.value)
            self.manager.screen.blit(text_surf, (20, 56 + i * (TILE_SIZE + TILE_MARGIN)))

    @property
    def board(self) -> Generator:
        for y, row in enumerate(self._board):
            for x, tile in enumerate(row):
                yield x, y, tile