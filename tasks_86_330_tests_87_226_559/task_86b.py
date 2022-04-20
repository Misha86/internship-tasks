# task 86b
def sum_digits(number):
    return sum([int(num) for num in str(number)])


if __name__ == "__main__":
    numb = 13456
    print(sum_digits(numb))
