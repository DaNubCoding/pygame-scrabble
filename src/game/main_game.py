from random import randint, shuffle

from src.common.constants import VEC, Color, TILE_SIZE, TILE_MARGIN, OPTIONS_BUTTON_FONT
from src.management.container import Container, Spacer
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
        self.rack.add_children(Spacer(self, (0, 0, 2, 0)))
        for _ in range(7):
            self.rack.add_children(RackTile(self, ("$ + 9p", 10, ..., "100% - 20p"), chr(randint(65, 90))))

        self.__build_options_container()

    def __build_rack_container(self) -> None:
        self.rack_cont = Container(self, (40, 780, (TILE_SIZE + TILE_MARGIN) * 15 - TILE_MARGIN, 110))
        self.rack_cont.setup(
            bg_color = (255, 255, 255),
            border_radius = 12,
        )

        self.rack_cont.add_children(ele := Button1(self, (15, 15, ..., "100% - 30p"), self.shuffle))
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

        self.rack_cont.add_children(ele := Button1(self, ("$ + 15p", 15, ..., "100% - 30p"), self.reset))
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

    def shuffle(self) -> None:
        children = self.rack.children[1:]
        shuffle(children)
        self.__reorder_rack(children)

    def reset(self) -> None:
        children = self.rack.children[1:]
        children.sort(key=lambda child: child.text)
        self.__reorder_rack(children)

    def __reorder_rack(self, children: list[RackTile]) -> None:
        self.rack.children = [self.rack.children[0]] + children
        for child in children:
            child.parse_rect()

    def update(self) -> None:
        super().update()

    def draw(self) -> None:
        self.manager.screen.fill(Color.BG.value)

        super().draw()