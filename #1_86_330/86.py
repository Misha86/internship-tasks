# task 86a
def count_digits(number):
    return len(str(number))


# task 86b
def sum_digits(number):
    return sum([int(num) for num in str(number)])


if __name__ == "__main__":
    numb = 13456
    print(count_digits(numb))
    print(sum_digits(numb))
