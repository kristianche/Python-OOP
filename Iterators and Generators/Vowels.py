class vowels:
    def __init__(self, string):
        self.string = string
        self.index = -1
        self.vowels = ("a", "e", "o", "u", "i", "y")

    def __iter__(self):
        return self

    def __next__(self):
        result = []
        if self.index >= len(self.string) - 1:
            raise StopIteration
        self.index += 1
        char = self.string[self.index]
        if char.lower() in self.vowels:
            result.append(char)
        return "\n".join(result)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)