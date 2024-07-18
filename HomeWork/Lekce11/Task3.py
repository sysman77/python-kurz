class Dictionary:
    def __init__(self):
        self.data = {}
        self.popularity = {}

    def add_word(self, word, translations):
        if word in self.data:
            print(f"Slovo '{word}' již existuje.")
            return

        self.data[word] = translations
        self.popularity[word] = 0
        print(f"Slovo '{word}' bylo přidáno do slovníku.")

    def remove_word(self, word):
        if word in self.data:
            del self.data[word]
            del self.popularity[word]
            print(f"Slovo '{word}' bylo odstraněno ze slovníku.")
        else:
            print(f"Slovo '{word}' neexistuje ve slovníku.")

    def update_word(self, word, translations):
        if word in self.data:
            self.data[word] = translations
            print(f"Překlady slova '{word}' byly aktualizovány.")
        else:
            print(f"Slovo '{word}' neexistuje ve slovníku. Můžete ho přidat pomocí metody add_word.")

    def add_translation(self, word, translation):
        if word in self.data:
            if translation not in self.data[word]:
                self.data[word].append(translation)
                print(f"Překlad '{translation}' byl přidán k slovu '{word}'.")
            else:
                print(f"Překlad '{translation}' již existuje pro slovo '{word}'.")
        else:
            print(f"Slovo '{word}' neexistuje ve slovníku. Můžete ho přidat pomocí metody add_word.")

    def remove_translation(self, word, translation):
        if word in self.data:
            if translation in self.data[word]:
                self.data[word].remove(translation)
                print(f"Překlad '{translation}' byl odstraněn ze slova '{word}'.")
            else:
                print(f"Překlad '{translation}' neexistuje pro slovo '{word}'.")
        else:
            print(f"Slovo '{word}' neexistuje ve slovníku.")

    def get_translations(self, word):
        if word in self.data:
            self.popularity[word] += 1
            return self.data[word]
        else:
            return None

    def get_most_popular_words(self, n=10):
        sorted_words = sorted(self.popularity.items(), key=lambda x: x[1], reverse=True)
        return [word[0] for word in sorted_words[:n]]

    def get_least_popular_words(self, n=10):
        sorted_words = sorted(self.popularity.items(), key=lambda x: x[1])
        return [word[0] for word in sorted_words[:n]]


# Ukázkové použití aplikace
if __name__ == "__main__":
    dictionary = Dictionary()

    # Přidání slov do slovníku
    dictionary.add_word("hello", ["hola", "bonjour"])
    dictionary.add_word("goodbye", ["adiós", "au revoir"])
    dictionary.add_word("yes", ["sí", "oui"])
    dictionary.add_word("no", ["no", "non"])

    # Získání překladů slova
    print(dictionary.get_translations("hello"))  # ['hola', 'bonjour']

    # Přidání a odstranění překladů
    dictionary.add_translation("hello", "hallo")
    print(dictionary.get_translations("hello"))  # ['hola', 'bonjour', 'hallo']
    dictionary.remove_translation("hello", "bonjour")
    print(dictionary.get_translations("hello"))  # ['hola', 'hallo']

    # Odstranění slova
    dictionary.remove_word("yes")

    # Zobrazení nejoblíbenějších a nejméně oblíbených slov
    print("Nejoblíbenější slova:", dictionary.get_most_popular_words())
    print("Nejméně oblíbená slova:", dictionary.get_least_popular_words())