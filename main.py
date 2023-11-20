# Ədədi massiv yaratmaq
massiv = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 5-ə bölünməyən ədədləri seçmək və yeni fayla yazmaq
with open("bolenme_fayli.txt", "w") as yeni_fayl:
    for eded in massiv:
        if eded % 5 != 0:
            yeni_fayl.write(str(eded) + "\n")

# 5-ə bölünməyən ədədlərin hasilini hesablamaq
hasil = 1
for eded in massiv:
    if eded % 5 != 0:
        hasil *= eded

# Hasili ekrana çap etmək
print("5-ə bölünməyən ədədlərin hasil:", hasil)
