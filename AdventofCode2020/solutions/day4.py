def puzzle7(input):
    passports = [
        [info.split(":") for info in passport.replace(" ", "\n").split("\n") if info]
        for passport in input.split("\n\n")
        if passport
    ]
    pass_dicts = [{info[0]: info[1] for info in passport} for passport in passports]

    expected_info = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    valid_passport_count = 0
    for passport in pass_dicts:
        if set(passport.keys()).issuperset(set(expected_info)):
            valid_passport_count += 1
    return valid_passport_count


def puzzle8(input):
    pass


if __name__ == "__main__":
    sample_input4 = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
    input4 = open("AdventOfCode2020/inputs/input4.txt", "r").read()

    print(puzzle7(sample_input4))
    print(puzzle7(input4))
    # print(puzzle8(sample_input4))
    # print(puzzle8(input4))
