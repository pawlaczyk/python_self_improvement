"""
You are given a class called `Sentence`, which takes a string such as `hello world`.
You need to provide an interface such that the indexer return a flyweight that can be used to capitalize a prticulat word in thsentence
"""


class Sentence:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.formatting = []

    class WordFormatter:
        def __init__(self, position, capitalize=True):
            self.position = position
            self.capitalize = capitalize

        def covers(self, position):
            return self.plain_text.split(' ')[self.position]

    def __getitem__(self, position):
        word_formatter = self.WordFormatter(position) #przy klasach wewnetrznych też trzeba używać self.
        self.formatting.append(word_formatter)
        return word_formatter

    def __str__(self):
        result = []
        for index in range(len(self.plain_text.split(' '))):
            word = self.plain_text.split(' ')[index] #mamy słowo
            for formatted in self.formatting:
                if formatted.position == index and formatted.capitalize:
                    word = word.upper()
            result.append(word)

        return ' '.join(result)




if __name__ == "__main__":
    sentence = Sentence('Hello world')
    sentence[1].capitalize = True
    print(sentence)
    print(sentence == "Hello WORLD")
