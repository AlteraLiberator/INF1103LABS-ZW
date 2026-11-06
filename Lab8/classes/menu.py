from typing import Any
from collections.abc import Callable


class Menu:
    def __init__(self) -> None:
        self._menu_options = [
            {
                "display_string": "Quit",
                "method": None,
            }
        ]
    @property
    def menu_options(self) -> list[dict]:
        return self._menu_options

    @menu_options.setter
    def menu_options(self, value) -> None:
        self._menu_options = value

    def add_menu_option(self, display_string: str, method: Callable[..., Any]) -> None:
        self._menu_options.append({"display_string": display_string, "method": method})

    @staticmethod
    def print_border() -> None:
        print("========================================")

    @staticmethod
    def get_user_input() -> str:
        return input("Enter option: ")

    @staticmethod
    def exit_message() -> str:
        return "Exiting program."

    def display_main_menu(self) -> str:
        self.print_border()
        for index, option in enumerate(self.menu_options):
            print(f"{index}. {option['display_string']}")
        return self.get_user_input()
