class Sentence:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.formatting = []

    class WordFormatter:
        def __init__(self, word_number, capitalize=True):
            self.word_number = word_number
            self.capitalize = capitalize

    def __getitem__(self, position):
        word_formatter = self.WordFormatter(position)
        self.formatting.append(word_formatter)
        return word_formatter

    def __str__(self):
        result = []
        for index, word in enumerate(self.plain_text.split(' ')):
            for formatted in self.formatting:
                if formatted.word_number == index and formatted.capitalize:
                    word = word.upper()
            result.append(word)
        return ' '.join(result)


if __name__ == "__main__":
    sentence = Sentence('Hello world')
    sentence[1].capitalize = True
    print(sentence)
    print(sentence == "Hello WORLD")
