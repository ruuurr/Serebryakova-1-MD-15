def slov():
    stran = {'россия': 'москва', 'германия': 'берлин', 'япония': 'токио', 'китай': 'пекин', 'финляндия': 'хельсинки'}
    print("пары: ")
    for st, stol in stran.items():
        print(st, "--", stol)

def stolitsa(st):
    if st in stran:
      return stran[st]
    else:
        return "страна не найдена"

strr = input("введите название страны: ")
print("столица", strr + ":", stolitsa(strr))

print("в алфавитном порядке: ")
sort_st = sorted(stran.keys())
for st in sort_st:
    print(st, "--", stran[st])
