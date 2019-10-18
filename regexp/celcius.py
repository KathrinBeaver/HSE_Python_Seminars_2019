import re

def celsius(inputString):
    newText = re.compile(r"(([-]?\d+)(\.(\d*))?)F")
    farenheit = newText.findall(inputString)
    result = inputString
    for value in farenheit:
        #print(value)
        cel = round((float(value[0]) - 32) / 1.8, 2)
        result = newText.sub(str(cel) + "C", inputString, 1)
        inputString = result
    return result

text = input("Enter the new string you would like to change:  ")
print("Reformatted text: ", celsius(text))
