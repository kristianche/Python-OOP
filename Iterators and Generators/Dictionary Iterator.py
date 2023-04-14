class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = list(dictionary.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.dictionary) - 1:
            raise StopIteration

        self.index += 1

        return self.dictionary[self.index]