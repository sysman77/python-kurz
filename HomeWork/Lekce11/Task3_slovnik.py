class DictionaryApp:
    def __init__(self):
        self.dictionary = {}
        self.popularity = {}

    def initial_input(self):
        initial_words = {
            "apple": "jablko",
            "banana": "banán",
            "cat": "kočka",
            "dog": "pes",
            "elephant": "slon"
        }
        self.dictionary.update(initial_words)
        for word in initial_words:
            self.popularity[word] = 0

    def display_word(self, word):
        if word in self.dictionary:
            self.popularity[word] += 1
            return f"{word} - {self.dictionary[word]}"
        else:
            return f"Slovo '{word}' nebylo nalezeno."

    def add_or_replace_translation(self, word, translation):
        if word in self.dictionary:
            self.dictionary[word] = translation
            return f"Překlad pro '{word}' byl nahrazen."
        else:
            self.dictionary[word] = translation
            self.popularity[word] = 0
            return f"Překlad pro '{word}' byl přidán."

    def delete_translation(self, word):
        if word in self.dictionary:
            del self.dictionary[word]
            del self.popularity[word]
            return f"Překlad pro '{word}' byl smazán."
        else:
            return f"Slovo '{word}' nebylo nalezeno."

    def display_top_words(self, top_n=10, least=False):
        sorted_words = sorted(self.popularity.items(), key=lambda item: item[1], reverse=not least)
        result = []
        for word, count in sorted_words[:top_n]:
            result.append(f"{word}: {count} požadavků")
        return result

    def menu(self):
        while True:
            print("\nSlovník - Menu")
            print("1. Počáteční vstup dat do slovníku")
            print("2. Zobrazit slovo a jeho překlady")
            print("3. Přidat nebo nahradit překlad slov")
            print("4. Smazat překlad slov")
            print("5. Zobrazit 10 nejoblíbenějších slov")
            print("6. Zobrazit 10 nejméně populárních slov")
            print("7. Ukončit aplikaci")

            choice = input("Vyberte možnost: ")

            if choice == "1":
                self.initial_input()
                print("Počáteční data byla vložena.")
            elif choice == "2":
                word = input("Zadejte slovo k zobrazení: ")
                print(self.display_word(word))
            elif choice == "3":
                word = input("Zadejte slovo: ")
                translation = input("Zadejte překlad: ")
                print(self.add_or_replace_translation(word, translation))
            elif choice == "4":
                word = input("Zadejte slovo k odstranění: ")
                print(self.delete_translation(word))
            elif choice == "5":
                print("10 nejoblíbenějších slov:")
                for item in self.display_top_words():
                    print(item)
            elif choice == "6":
                print("10 nejméně populárních slov:")
                for item in self.display_top_words(least=True):
                    print(item)
            elif choice == "7":
                print("Ukončuji aplikaci.")
                break
            else:
                print("Neplatná volba, zkuste to znovu.")


if __name__ == "__main__":
    app = DictionaryApp()
    app.menu()
