from customerbot.adapters.input import InputAdapter
from customerbot.conversation import Statement
from customerbot.utils.read_input import input_function


class TerminalAdapter(InputAdapter):
    """
    A simple adapter that allows customerbot to
    communicate through the terminal
    """

    def process_input(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return: Read the user's input from the terminal
        """
        user_input = input_function()
        return Statement(user_input)