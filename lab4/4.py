def ticket(ticket_num):
    if len(ticket_num) % 2 != 0:
        return False

    pol = len(ticket_num) // 2
    first_pol = ticket_num[:pol]
    second_pol = ticket_num[pol:]

    sum_first_pol = sum(int(digit) for digit in first_pol)
    sum_second_pol = sum(int(digit) for digit in second_pol)
    return sum_first_pol == sum_second_pol


ticket_num = input("введите номер билета: ")
if ticket(ticket_num):
    print("билет счастливый!")
else:
    print("билет не счастливый")