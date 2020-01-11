arabic_to_roman = {
    1000: "M",
    900: "CM",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV"
}


def roman_for(arabic_number):
    for case in arabic_to_roman:
        if arabic_number >= case:
            return arabic_to_roman[case] + roman_for(arabic_number - case)

    return "I" * arabic_number
