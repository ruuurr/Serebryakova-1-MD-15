def sl(word):
    if 'ф' in word.lower():
        return True
    else:
        return False

def main():
    word = input("введите слово:")
    if sl(word):
        print("это редкое слово!")
    else:
        print("это не очень редкое слово")

if __name__ == "__main__":
    main()