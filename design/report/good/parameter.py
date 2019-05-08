from abc import ABC, abstractmethod


class Parameter(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def fill(self, http_request):
        pass


class SimpleParameter(Parameter):
    def __init__(self, name, values=[]):
        self.values = values
        self.name = name

    def get_name(self):
        return self.name

    def set_values(self, values):
        self.values = values

    def fill(self, http_request):
        values = http_request.get_parameter_values(self.name)
        self.set_value(values)


class ItemParameter(Parameter):
    def __init__(self, name, items=[]):
        self.name = name
        self.items = items

    def get_name(self):
        return self.name

    def get_items(self):
        return self.items

    def fill(self, http_request):
        for item in self.items:
            values = http_request.get_parameter_values(item.name)
            item.set_values(values)


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

    def fill(self, http_request):
        rows = http_request.get_parameter_values(self.row_name)
        columns = http_request.get_parameter_values(self.column_name)
        data_cells = http_request.get_parameter_values(self.data_cell_name)

        column_size = len(columns)
        for i in len(rows):
            for j in len(columns):
                element = TableParameterElement(rows[i], columns[j], data_cells[column_size * i + j])
                self.add_element(element)


class TableParameterElement:
    def __init(self, row, column, data_cell):
        self.row = row
        self.column = column
        self.data_cell = data_cell
