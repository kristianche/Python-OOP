def start_playing(instance):
    return instance.play()


class Guitar:

    def play(self):
        return "Playing the guitar"


guitar = Guitar()
print(start_playing(guitar))