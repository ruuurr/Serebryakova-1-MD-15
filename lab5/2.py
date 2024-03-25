numbers = [1, 5, 9, 12, 14, 16, 19, 20, 21, 5, 19]
pov = []
nepov = {}
for n in numbers:
    if n in nepov:
        pov.append(n)
    else:
        nepov[n] = True
if pov:
    print("повторяющиеся элементы", pov)
else:
    print("нет повторяющихся элементов")
