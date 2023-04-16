from src.management.scene import Scene
from src.management.element import Element

class Interactable(Element):
    def __init__(self, scene: Scene, rect: tuple[float, float, float, float]) -> None:
        super().__init__(scene, rect)
        self.hover_flag = True
        self.click_flag = True

    def update(self) -> None:
        if self.rect.collidepoint(self.manager.mouse_pos):
            if self.manager.mouse_state[0]:
                self.__handle_click()
            else:
                if not self.click_flag:
                    self.off_click()
                    self.click_flag = True
                self.__handle_hover()
        else:
            if not self.hover_flag:
                self.off_hover()
                self.hover_flag = True
            if not self.click_flag:
                self.off_click()
                self.click_flag = True

    def __handle_click(self) -> None:
        self.clicking()
        if self.click_flag:
            self.on_click()
            self.click_flag = False

    def __handle_hover(self) -> None:
        self.hovering()
        if self.hover_flag:
            self.on_hover()
            self.hover_flag = False

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