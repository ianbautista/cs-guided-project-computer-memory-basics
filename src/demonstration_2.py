"""
In order to solve this challenge you will need to [review the rules of Roman
Numerals](https://www.mathsisfun.com/roman-numerals.html).

Given a Roman Numeral (as a string), convert it to an integer. Your input is
guaranteed to be a Roman Numeral value from 1 to 3999.

Example 1:

Input: "IV"
Output: 4

Example 2:

Input: "XII"
Output: 12

Example 3:

Input: "MCMLXXXIV"
Output: 1984
"""


def roman_to_integer(roman):
    # Your code here

    # value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    # p = 0
    # ans = 0
    # n = len(roman)
    # print(n)
    # for i in reversed(range(n)):
    #     print(reversed(range(n)))
    #     if value[roman[i]] >= p:
    #         ans += value[roman[i]]
    #     else:
    #         ans -= value[roman[i]]
    #     p = value[roman[i]]
    # return ans


num = {
    "I": 1, "V": 5, "X": 10, "L": 50,
    "C": 100, "D": 500, "M": 1000
}
 converted = [num[i] for i in roman]
  integer = converted[-1]
   for i in range(len(converted)-1):
        if converted[i] < converted[i + 1]:
            integer -= converted[i]
        else:
            integer += converted[i]
    return integer
: heavy_check_mark:
1


print(roman_to_integer("XIV"))
