def puzzle3(input):
    input_list = [x for x in input.split("\n") if x]
    valid_password_count = 0
    for row in input_list:
        nums, letter_colon, password = row.split()
        num1, num2 = nums.split("-")
        num1, num2 = int(num1), int(num2)
        letter = letter_colon[0]
        if num1 <= password.count(letter) <= num2:
            valid_password_count += 1
    return valid_password_count


def puzzle4(input):
    input_list = [x for x in input.split("\n") if x]
    valid_password_count = 0
    for row in input_list:
        nums, letter_colon, password = row.split()
        num1, num2 = nums.split("-")
        num1, num2 = int(num1), int(num2)
        letter = letter_colon[0]

        valid_position_1 = password[num1 - 1] == letter
        valid_position_2 = password[num2 - 1] == letter
        if valid_position_1 ^ valid_position_2:
            valid_password_count += 1
    return valid_password_count





if __name__ == "__main__":
    sample_input2 = "1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc"
    input2 = open("input2.txt", "r").read()
    
    print(puzzle3(sample_input2))
    print(puzzle3(input2))

    print(puzzle4(sample_input2))
    print(puzzle4(input2))
