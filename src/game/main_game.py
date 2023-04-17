from src.common.constants import VEC, Color, TILE_SIZE, TILE_MARGIN, OPTIONS_BUTTON_FONT
from src.game.elements.container import Container
from src.game.elements.rack_tile import RackTile
from src.game.elements.button import Button1
from src.management.element import Style
from src.management.scene import Scene
import src.common.images as images
from src.game.board import Board

class MainGame(Scene):
    def setup(self) -> None:
        super().setup()

        self.board = Board(self)

        self.rack_button_style = Style(
            idle_color = Color.RACK_BUTTON_IDLE.value,
            hover_color = Color.RACK_BUTTON_HOVER.value,
            click_color = Color.RACK_BUTTON_CLICK.value,
            fg_color = (0, 0, 0),
            font = OPTIONS_BUTTON_FONT,
        )

        self.__build_rack_container()
        self.rack.add_children(RackTile(self, (11, 10, ..., "100% - 20p"), "M"))
        for _ in range(6):
            self.rack.add_children(RackTile(self, ("$ + 9p", 10, ..., "100% - 20p"), "C"))

        self.__build_options_container()

    def __build_rack_container(self) -> None:
        self.rack_cont = Container(self, (40, 780, (TILE_SIZE + TILE_MARGIN) * 15 - TILE_MARGIN, 110))
        self.rack_cont.setup(
            bg_color = (255, 255, 255),
            border_radius = 12,
        )

        self.rack_cont.add_children(ele := Button1(self, (15, 15, ..., "100% - 30p"), lambda: print("shuffle")))
        ele.setup(
            **self.rack_button_style,
            image = images.shuffle,
            border_radius = 12,
        )

        self.rack = Container(self, ("$ + 15p", 15, "100% - $ - $ - 30p - 30p", "100% - 30p"))
        self.rack.setup(
            bg_color = Color.BG.value,
            border_radius = 12,
        )
        self.rack_cont.add_children(self.rack)

        self.rack_cont.add_children(ele := Button1(self, ("$ + 15p", 15, ..., "100% - 30p"), lambda: print("reset")))
        ele.setup(
            **self.rack_button_style,
            image = images.reset,
            border_radius = 12,
        )

    def __build_options_container(self) -> None:
        cont = Container(self, (VEC(self.rack_cont.rect.topleft) + (0, 125), VEC(self.rack_cont.rect.size) - (0, 40)))

        cont.add_children(ele := Button1(self, (0, 0, "(100% - 15p * 3) / 4", "100%"), lambda: print("resign")))
        ele.setup(
            **self.rack_button_style,
            text = "Resign",
            border_radius = 9,
        )

        cont.add_children(ele := Button1(self, ("$ + 15p", 0, "$", "100%"), lambda: print("skip")))
        ele.setup(
            **self.rack_button_style,
            text = "Skip",
            border_radius = 9,
        )

        cont.add_children(ele := Button1(self, ("$ + 15p", 0, "$", "100%"), lambda: print("swap")))
        ele.setup(
            **self.rack_button_style,
            text = "Swap",
            border_radius = 9,
        )

        cont.add_children(ele := Button1(self, ("$ + 15p", 0, "$", "100%"), lambda: print("submit")))
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