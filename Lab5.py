import re
import locale

# Встановлення локалізації для української мови
locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')

file_path = 'file.txt'  # шлях до вашого текстового файлу

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)  # Розділяємо текст на речення

        if len(sentences) > 0:
            first_sentence = sentences[0]
            print("Перше речення з файлу:")
            print(first_sentence)

            words = re.findall(r'\b\w+\b', text)  # Знаходимо всі слова без знаків пунктуації
            words = [word for word in words if word.isalpha()]  # Відфільтровуємо слова, що складаються тільки з букв

            ukrainian_words = sorted(
                [word for word in words if re.match('[а-яА-ЯЇЄІіҐґєї]', word)], key=locale.strxfrm
            )  # Усі слова українською мовою
            english_words = sorted(
                [word for word in words if re.match('[a-zA-Z]', word)], key=lambda x: x.lower()
            )  # Усі слова англійською мовою

            if len(ukrainian_words) > 0:
                print("\nУкраїнські слова в алфавітному порядку:")
                print(ukrainian_words)

            if len(english_words) > 0:
                print("\nАнглійські слова в алфавітному порядку:")
                print(english_words)

            print(f"\nКількість слів у тексті: {len(words)}")
        else:
            print("Файл порожній. Немає речень для обробки.")
except FileNotFoundError:
    print(f"Помилка: Файл {file_path} не знайдено.")
except Exception as e:
    print(f"Помилка: {e}")