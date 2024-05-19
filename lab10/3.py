
en_ru_content = """cat - кошка
dog - собака
home - домашняя папка, дом
mouse - мышь, манипулятор мышь
to do - делать, изготавливать
to make - изготавливать"""

with open('en-ru.txt', 'w', encoding='utf-8') as file:
    file.write(en_ru_content)

en_ru_dict = {}

with open('en-ru.txt', 'r', encoding='utf-8') as file:
    for line in file:
        en_word, ru_words = line.strip().split(' - ')
        ru_words_list = [word.strip() for word in ru_words.split(', ')]
        for ru_word in ru_words_list:
            if ru_word not in en_ru_dict:
                en_ru_dict[ru_word] = []
            en_ru_dict[ru_word].append(en_word)


with open('ru-en.txt', 'w', encoding='utf-8') as file:
    for ru_word in sorted(en_ru_dict.keys()):
        en_words = ', '.join(sorted(en_ru_dict[ru_word]))
        file.write(f'{ru_word} – {en_words}\n')