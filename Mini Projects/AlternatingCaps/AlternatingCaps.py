def changing_caps(s):
    count = 0
    output_str = ""
    for i in s:
        if i.isalpha() and (count % 2 == 0 or count == 0):
            count += 1
            i = i.upper()
            output_str += i
        elif i.isalpha() and count % 2 != 0:
            count += 1
            i = i.lower()
            output_str += i
        else:
            output_str += i
    return output_str


print(changing_caps(input("Input your string here:\n")))
