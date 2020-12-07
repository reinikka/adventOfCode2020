
def readData(fileName):
    data = list({})
    print("Reading passports from: " + fileName)
    with open(fileName, 'r') as dataFile:
        person = None
        for inLine in dataFile:
            inLine = inLine.strip()
            if inLine:
                lineParts = inLine.split()
                for elem in lineParts:
                    keyVal = elem.split(":")
                    if not person:
                        person = dict()
                    person[keyVal[0]] = keyVal[1]
            else:
                if person:
                    data.append(person)
                    person = None
        if person:
            data.append(person)

    print(data)
    return data


def isYearValid(minYear, maxYear, value):
    if len(value) != 4:
        return False
    year = int(value)
    return (year >= minYear and year <= maxYear)


def isHeightValid(value):
    minHeight = 0
    maxHeight = 0
    height = 0
    if value.endswith("cm"):
        minHeight = 150
        maxHeight = 193
        height = int(value.replace("cm", ""))
    elif value.endswith("in"):
        minHeight = 59
        maxHeight = 76
        height = int(value.replace("in", ""))
    else:
        return False
    return (height >= minHeight and height <= maxHeight)


def isHairColorValid(value):
    if not value.startswith("#"):
        return False
    if len(value[1:]) != 6:
        return False
    for c in value[1:]:
        if not ((c >= "0" and c <= "9") or (c >= "a" and c <= "f")):
            return False
    return True


def IsFieldValueValid(key, value):
    if key == "byr":
        return isYearValid(1920, 2002, value)
    if key == "iyr":
        return isYearValid(2010, 2020, value)
    if key == "eyr":
        return isYearValid(2020, 2030, value)
    if key == "hgt":
        return isHeightValid(value)
    if key == "hcl":
        return isHairColorValid(value)
    if key == "ecl":  # Eye color
        return value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    if key == "pid":
        return (len(value) == 9 and int(value) > 0)
    return False


def countValidPassports(passports, doValueValidation):
    count = 0
    mandatoryFields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

    ppNum = 0
    for pp in passports:
        ppNum = ppNum + 1
        score = 1
        for field in mandatoryFields:
            if not field in pp:
                print(f"Passport {ppNum} missing field {field}")
                score = 0
                break
            if doValueValidation and not IsFieldValueValid(field, pp[field]):
                print(
                    f"Passport {ppNum} field {field} value {pp[field]} is not valid")
                score = 0
                break

        count = count+score
    return count


def main():
    passports = readData("input.txt")
    numberValidPassportsPart1 = countValidPassports(passports, False)
    numberValidPassportsPart2 = countValidPassports(passports, True)
    print(f"Number of all passports: {len(passports)}.")
    print(f"Number of valid part1 passports: {numberValidPassportsPart1}.")
    print(f"Number of valid part2 passports: {numberValidPassportsPart2}.")


if __name__ == "__main__":
    main()
