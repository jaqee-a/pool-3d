class Keyboard:

    held_keys = []

    @staticmethod
    def add_key(key):
        Keyboard.held_keys.append(key)


    def remove_key(key):
        try:
            Keyboard.held_keys.remove(key)
        except:
            pass
