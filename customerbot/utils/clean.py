import re


def clean_whitespace(text):
    """
    :param text: text as a parameter
    :return: removes whitespaces and line breaks as needed.
    """
    #replace linebreaks with spaces
    text = text.replace("\n", " ").replace("\r", " ").replace("\t", " ")

    # remove any leading or trailing whitespaces
    text = text.strip()

    # remove consecutive spaces
    text = re.sub(" +", " ", text)
    return text


def clean(text):
    """
    :param text: taking text as a parameter
    :return: A function for cleaning a string of text. Returns valid ASCII characters.
    """
    import unicodedata
    import sys

    text = clean_whitespace(text)

    # Remove links from messages
    # text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)

    # Replace HTML escape characters
    if sys.version_info[0] < 3:
        from HTMLParser import HTMLParser
        parser = HTMLParser()
        text = parser.unescape(text)
    else:
        import html
        text = html.unescape(text)

    # Normalize unicode characters
    # raw_input is just 'input' in python 3
    if sys.version_info[0] < 3:
        text = unicode(text)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")

    return str(text)