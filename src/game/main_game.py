from typing import Generator
import pygame

from src.common.constants import VEC, Color, TILE_SIZE, TILE_MARGIN, BONUS_LOCATIONS, BONUS_FONT, AXIS_FONT
from src.game.container import Container
from src.management.scene import Scene
from src.game.button import Button1
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

        self.rack_container.add_children(cont := Button1(self, (15, 15, ..., top), None))
        cont.setup(
            bg_color = Color.RACK_BUTTON.value,
            border_radius = 12,
        )

        self.rack_container.add_children(cont := Container(self, ("$ + 15p", 15, "100% - $ - $ - 30p - 30p", top)))
        cont.setup(
            bg_color = Color.BG.value,
            border_radius = 12,
        )

        self.rack_container.add_children(cont := Button1(self, ("$ + 15p", 15, ..., top), None))
        cont.setup(
            bg_color = Color.RACK_BUTTON.value,
            border_radius = 12,
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

    # right_rect = pygame.draw.rect(self.manager.screen, Color.RACK_BUTTON.value, (rect.right - 15 - (rect.height - 30), rect.top + 15, rect.height - 30, rect.height - 30), 0, 12)
    # pygame.draw.rect(self.manager.screen, Color.RACK_BUTTON.value, (*(VEC(right_rect.topleft) - (5, 5)), right_rect.height + 10, right_rect.height + 10), 2, 16)

    # rect = pygame.draw.rect(self.manager.screen, Color.RACK_BUTTON.value, (*(VEC(rect.topleft) + (15, 15)), rect.height - 30, rect.height - 30), 0, 12)
    # pygame.draw.rect(self.manager.screen, Color.RACK_BUTTON.value, (*(VEC(rect.topleft) - (5, 5)), rect.height + 10, rect.height + 10), 2, 16)

    # rect = pygame.draw.rect(self.manager.screen, Color.BG.value, (*(VEC(rect.topright) + (20, 0)), 497, rect.height), 0, 12)

    @property
    def board(self) -> Generator:
        for y, row in enumerate(self._board):
            for x, tile in enumerate(row):
                yield x, y, tile