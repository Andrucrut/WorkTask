def get_computer_declension(number):
    if number == 1:
        return f"{number} компьютер"
    elif 2 <= number <= 4:
        return f"{number} компьютера"
    else:
        return f"{number} компьютеров"
print(get_computer_declension(5))