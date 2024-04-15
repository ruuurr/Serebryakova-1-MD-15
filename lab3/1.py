def main():
    N = int(input("количество слов: "))

    words = []
    for i in range(N):
        word = input(f" слово {i+1}: ")
        words.append(word)

    result = ' '.join(words)
    print("результат:", result)

if __name__ == "__main__":
    main()