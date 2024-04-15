def check_password(password, confirm_password):
    if password == confirm_password:
        print("пароль принят")
    else:
        print("пароль не принят")

password = input("введите пароль:")
confirm_password = input("подтвердите пароль:")
check_password(password, confirm_password)
