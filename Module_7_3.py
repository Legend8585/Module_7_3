import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    # Удаление пунктуации
                    for punct in punctuation_to_remove:
                        content = content.replace(punct, '')
                    words = content.split()  
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
                all_words[file_name] = []

        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        positions = {}

        for file_name, words in all_words.items():
            if word in words:
                positions[file_name] = words.index(word) + 1  
            else:
                positions[file_name] = None

        return positions

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        counts = {}

        for file_name, words in all_words.items():
            counts[file_name] = words.count(word)

        return counts


##Пример выполнения программы:
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
