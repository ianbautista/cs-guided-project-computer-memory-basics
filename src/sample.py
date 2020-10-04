input_str = "DivasDwivedi"

# Printing original string
print("Original string: " + input_str)

result_str = ""

for i in range(0, len(input_str)):
    print(i)
    if i != 3:
        result_str = result_str + input_str[i]

# Printing string after removal
print("String after removal of i'th character : " + result_str)
