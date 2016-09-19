from nltk import word_tokenize


class POSTagger():
    """
    A custom-implementation of POS-taggers. Need to
    write for features here, only:
    1) tokenize: Returns the tokenized input text
    """

    def __init__(self):
        from nltk.data import find
        from nltk import download

        try:
            find('punkt.zip')
        except LookupError:
            download('punkt')

    def tokenize(self, text):
        """
        :param text: Taking an input string and tokenize that text
        :return: Returns an array of tuples which contain the tokenize text.
        """

        return word_tokenize(text)
