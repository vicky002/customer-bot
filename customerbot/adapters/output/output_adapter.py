from customerbot.adapters import Adapter


class OutputAdapter(Adapter):
    """
    This is an abstract class that represents the
    interface that all ouput adapters should implement
    """

    def process_response(self, input_value):
        """
        :param input_value: Take input
        :return: return output
        """

        return self.AdapterMethodNotImplementedError()