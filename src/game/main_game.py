from src.common.constants import VEC, Color, TILE_SIZE, TILE_MARGIN, OPTIONS_BUTTON_FONT
from src.game.elements.container import Container
from src.game.elements.button import Button1
from src.management.element import Style
from src.management.scene import Scene
import src.common.images as images
from src.game.board import Board

class MainGame(Scene):
    def setup(self) -> None:
        super().setup()
        self.board = Board(self)

        rack_button_style = Style(
            idle_color = Color.RACK_BUTTON_IDLE.value,
            hover_color = Color.RACK_BUTTON_HOVER.value,
            click_color = Color.RACK_BUTTON_CLICK.value,
            fg_color = (0, 0, 0),
            font = OPTIONS_BUTTON_FONT,
        )

        self.rack_container = Container(self, (40, 780, (TILE_SIZE + TILE_MARGIN) * 15 - TILE_MARGIN, 105))
        self.rack_container.setup(
            bg_color = (255, 255, 255),
            border_radius = 12,
        )

        self.rack_container.add_children(ele := Button1(self, (15, 15, ..., "100% - 30p"), lambda: print("shuffle")))
        ele.setup(
            **rack_button_style,
            image = images.shuffle,
            border_radius = 12,
        )

        self.rack_container.add_children(ele := Container(self, ("$ + 15p", 15, "100% - $ - $ - 30p - 30p", "100% - 30p")))
        ele.setup(
            bg_color = Color.BG.value,
            border_radius = 12,
        )

        self.rack_container.add_children(ele := Button1(self, ("$ + 15p", 15, ..., "100% - 30p"), lambda: print("reset")))
        ele.setup(
            **rack_button_style,
            image = images.reset,
            border_radius = 12,
        )

        self.options_container = Container(self, (VEC(self.rack_container.rect.topleft) + (0, 120), VEC(self.rack_container.rect.size) - (0, 40)))

        self.options_container.add_children(ele := Button1(self, (0, 0, "(100% - 15p * 3) / 4", "100%"), lambda: print("resign")))
        ele.setup(
            **rack_button_style,
            text = "Resign",
            border_radius = 9,
        )

        self.options_container.add_children(ele := Button1(self, ("$ + 15p", 0, "$", "100%"), lambda: print("skip")))
        ele.setup(
            **rack_button_style,
            text = "Skip",
            border_radius = 9,
        )

        self.options_container.add_children(ele := Button1(self, ("$ + 15p", 0, "$", "100%"), lambda: print("swap")))
        ele.setup(
            **rack_button_style,
            text = "Swap",
            border_radius = 9,
        )

        self.options_container.add_children(ele := Button1(self, ("$ + 15p", 0, "$", "100%"), lambda: print("submit")))
        ele.setup(
            text = "Submit",
            font = OPTIONS_BUTTON_FONT,
            fg_color = (255, 255, 255),
            idle_color = Color.SUBMIT_BUTTON_IDLE.value,
            hover_color = Color.SUBMIT_BUTTON_HOVER.value,
            click_color = Color.SUBMIT_BUTTON_CLICK.value,
            border_radius = 9,
        )

    def update(self) -> None:
        super().update()

    def draw(self) -> None:
        self.manager.screen.fill(Color.BG.value)

        super().draw()