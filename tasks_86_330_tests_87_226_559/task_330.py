# task 330
def perfect_numbers(number):
    numbers = []
    for num in range(1, number):
        dividers = [div for div in range(1, int(num/2)+1) if num % div == 0]
        if sum(dividers) == num:
            numbers.append(num)
    return numbers


if __name__ == "__main__":
    numb = 1000
    print(perfect_numbers(numb))


