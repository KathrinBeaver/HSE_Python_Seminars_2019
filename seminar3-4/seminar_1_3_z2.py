text = "1 2 3 numbers 2 1 3 5"
text = text.replace("1","one")
text = text.replace("2","two")
text = text.replace("3","three")
text = text.replace("4","four")
text = text.replace("5","five")
text = text.replace("6","six")
text = text.replace("7","seven")
text = text.replace("8","eight")
text = text.replace("9","nine")
text = text.replace("0","zero")
print (text)

# так тоже можно "\" говорит интерпретатору, что команда будет продолжена
text = text.replace("1","one").replace("2","two") \
        .replace("3","three").replace("4","four").replace("5","five") \
        .replace("6","six").replace("7","seven").replace("8","eight").replace("9","nine").replace("0","zero")

print(text)
