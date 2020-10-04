def removeAdjacent(s):
    new_string = [i for i in s]
    for char in range(len(new_string) - 1):
        if new_string[char] == new_string[char + 1]:
            new_string[char] = ""
    return "".join(new_string)

####################################

# def removeAdjacent(s):
#     new_string = str(s[0])
#     for char in range(1, len(new_string) - 1):
#         if new_string[char] != new_string[char - 1]:
#             new_string += new_string[char]
#     return new_string

####################################

# def removeAdjacent(s):
#     new_string = ""
#     for i, char in enumerate(s):
#         if s[i] != s[i - 1]:
#             new_string += s[i]
#     return (new_string)


# print(removeAdjacent("aaaaa"))
print(removeAdjacent("aaaccbcccccccabbbbaaaccccbbbb"))
