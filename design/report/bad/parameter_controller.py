from design.report.bad.parameter import SimpleParameter, ItemParameter, TableParameterElement


class ParameterController:
    @staticmethod
    def fill_parameters(http_request, parameter_graph):
        for parameter in parameter_graph.get_parameters():
            if isinstance(parameter, SimpleParameter):
                values = http_request.get_parameter_values(parameter.name)
                parameter.set_value(values)
            elif isinstance(parameter, ItemParameter):
                for item in parameter.get_items():
                    values = http_request.get_parameter_values(item.name)
                    item.set_values(values)
            else:
                rows = http_request.get_parameter_values(parameter.get_row_name())
                columns = http_request.get_parameter_values(parameter.get_column_name())
                data_cells = http_request.get_parameter_values(parameter.get_data_cell_name())

                column_size = len(columns)
                for i in len(rows):
                    for j in len(columns):
                        element = TableParameterElement(rows[i], columns[j], data_cells[column_size * i + j])
                        parameter.add_element(element)


