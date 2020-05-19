class Translation:

    def __init__(self, original_text, translated_text):
        self.original_text = original_text
        self.translated_text = translated_text

    def get_tokens(self):
        result = {'original_tokens': tokeniser(self.original_text),
                  'translated_tokens': tokeniser(self.translated_text)}
        return result


def tokeniser(string):
    return string.split(" ")

