from src.management.element import Element
from src.management.scene import Scene

class Interactable(Element):
    def __init__(self, scene: Scene, rect: tuple[float, float, float, float]) -> None:
        super().__init__(scene, rect)
        self._hover_flag = True
        self._click_flag = True
        self._hover = False
        self._click = False
        self._clicked_outside = False

        self.locked = False

    def update(self) -> None:
        if self.locked:
            self.bg_color = getattr(self, "locked_bg_color", self.bg_color)
            self.fg_color = getattr(self, "locked_fg_color", self.fg_color)
            return

        self._hover = self.rect.collidepoint(self.manager.mouse_pos)
        self._click = self._hover and self.manager.mouse_state[0] and not self._clicked_outside

        # If click is released inside interactable, _clicked_outside should be reset to allow another click
        if self._hover and not self.manager.mouse_state[0]:
            self._clicked_outside = False

        if self._hover:
            self.__handle_hover()
        else:
            self.idle()
            self.__handle_unhover()
        if self._click:
            self.__handle_click()
        else:
            self.__handle_unclick()

    # When you manage to unnest everything (⌐▨_▨)
    def __handle_click(self) -> None:
        self.clicking()
        if not self._click_flag: return
        self.on_click()
        self._click_flag = False

    def __handle_hover(self) -> None:
        self.hovering()
        if not self._hover_flag: return
        self.on_hover()
        self._hover_flag = False

    def __handle_unhover(self) -> None:
        # This prevents the mouse being able to hold down click and drag over the interactable to activate it
        self._clicked_outside = self.manager.mouse_state[0]
        self.bg_color = getattr(self, "idle_color", self.bg_color)
        self.fg_color = getattr(self, "idle_fg_color", self.fg_color)

        if self._hover_flag: return
        self.off_hover()
        self._hover_flag = True

    def __handle_unclick(self) -> None:
        if self._click_flag: return
        self.off_click()
        self._click_flag = True

    def on_hover(self) -> None:
        # Override: Called on the first frame the cursor enters the area
        pass

    def on_click(self) -> None:
        # Override: Called on the first frame the mouse clicks the area
        pass

    def off_hover(self) -> None:
        # Override: Called on the first frame the cursor leaves the area
        pass

    def off_click(self) -> None:
        # Override: Called on the first frame the mouse ceases to click the area
        pass

    def hovering(self) -> None:
        # Override: Called continuously when the cursor is hovering over the area
        pass

    def clicking(self) -> None:
        # Override: Called continuously when the cursor is clicking the area
        pass

    def idle(self) -> None:
        # Override: Called continuously when the cursor is not in the area
        pass