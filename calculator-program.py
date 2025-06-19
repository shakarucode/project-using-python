# Calculator Program in Python

operation = input("Ketikkan Operasi Yang Ingin Dilakukan: (+, -, *, /) ")
a = float(input("Ketikkan Angka Pertama: "))
b = float(input("Ketikkan Angka Kedua: "))

if operation == "+":
    result = a + b
    print(result)
elif operation == "-":
    result = a - b
    print(result)
elif operation == "*":
    result = a * b
    print(result)
elif operation == "/":
    result = a / b
    print(result)
else:
    print("Operasi Tidak Dikenal")
