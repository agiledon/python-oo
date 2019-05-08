from abc import ABC, abstractmethod


class Parameter(ABC):
    @abstractmethod
    def get_name(self):
        pass


class SimpleParameter(Parameter):
    def __init__(self, name, values=[]):
        self.values = values
        self.name = name

    def get_name(self):
        return self.name

    def set_values(self, values):
        self.values = values


class ItemParameter(Parameter):
    def __init__(self, name, items=[]):
        self.name = name
        self.items = items

    def get_name(self):
        return self.name

    def get_items(self):
        return self.items


class Item:
    def __init__(self, name):
        self.name = name
        self.values = []

    def get_name(self):
        return self.name

    def set_values(self, values):
        self.values = values


class TableParameter(Parameter):
    def __init__(self, name, row_name, column_name, data_cell_name):
        self.name = name
        self.row_name = row_name
        self.column_name = column_name
        self.data_cell_name = data_cell_name
        self.elements = []

    def get_name(self):
        return self.name

    def get_row_name(self):
        return self.row_name

    def get_column_name(self):
        return self.column_name

    def get_data_cell_name(self):
        return self.data_cell_name

    def add_element(self, element):
        self.elements.append(element)


class TableParameterElement:
    def __init(self, row, column, data_cell):
        self.row = row
        self.column = column
        self.data_cell = data_cell
