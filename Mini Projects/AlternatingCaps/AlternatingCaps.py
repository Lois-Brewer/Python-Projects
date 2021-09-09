def changing_caps(s):
    # Creates string with alternating caps, letters only
    count = 0
    output_str = ""
    for i in s:
        if i.isalpha() and (count % 2 == 0 or count == 0):
            count += 1
            output_str += i.upper()
        elif i.isalpha() and count % 2 != 0:
            count += 1
            output_str += i.lower()
        else:
            output_str += i
    return output_str


# Asks for input and returns output here
input_str = input("Input your string here:\n")
print(changing_caps(input_str))
