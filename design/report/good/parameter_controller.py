
class ParameterController:
    @staticmethod
    def fill_parameters(http_request, parameter_graph):
        for parameter in parameter_graph.get_parameters():
            parameter.fill(http_request)


