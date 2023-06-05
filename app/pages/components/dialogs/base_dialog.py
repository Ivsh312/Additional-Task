from typing import Union

from app.pages.components.base_element import BaseElement


class BaseDialog:

    def __init__(self, browser):
        self.browser = browser

    def fill_fild_by_class_attribute_name(self, class_attribute_name, value):
        self.get_element_by_name(class_attribute_name).text = value
        return self

    def fill_fields(self, fields: dict[str:str]):
        for fild, value in fields.items():
            self.fill_fild_by_class_attribute_name(fild, value)
        return self

    def get_element_by_name(self, name: str) -> 'BaseElement':
        return self.__getattribute__(name)
