def main():
    words = []
    while True:
        word = input("введите слово ('stop' для завершения): ")
        if word.lower() == 'stop':
            break
        words.append(word)

    result = ' '.join(words)
    print("результат:", result)

if __name__ == "__main__":
    main()
