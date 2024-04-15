def vsyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    year = int(input("введите год:"))
    if vsyear(year):
        print(f"год {year} - високосный")
    else:
        print("год не високосный")

if __name__ == "__main__":
    main()
