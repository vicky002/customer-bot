# -*- coding: utf-8 -*-
from .response import Response


class Statement(object):
    """
    A statement represents a single spoken entity, sentence or phrase that someone can say
    """

    def __init__(self, text, **kwargs):
        self.text = text
        self.in_response_to = kwargs.get("in_response_to", [])

        self.extra_data = {}
        if "in_response_to" in kwargs:
            del(kwargs["in_response_to"])

        self.extra_data.update(kwargs)

    def __str__(self):
        return self.text

    def __repr__(self):
        return "<Statement text:%s>" % self.text

    def __eq__(self, other):
        if not other:
            return False

        if isinstance(other, Statement):
            return self.text == other.text

        return self.text == other

    def add_extra_data(self, key, value):
        """
        :param key:
        :param value:
        :return: This method allows additional data to be stored on the statement object
        """
        self.extra_data[key] = value

    def add_response(self, response):
        """
        :param response: response object
        :return: add the response to the list if it does not already exist
        """
        if not isinstance(response, Response):
            raise Statement.InvalidTypeException(
                'A {} was received when a {} instance was expected'.format(
                    type(response),
                    type(Response(''))
                )
            )
        updated = False
        for index in range(0, len(self.in_response_to)):
            if response.text == self.in_response_to[index].text:
                self.in_response_to[index].occurrence += 1
                updated = True

        if not updated:
            self.in_response_to.append(response)