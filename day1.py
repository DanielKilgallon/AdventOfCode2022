import array

elf_list = []

elf_calories = 0
while True:
    elf_number = input()

    if elf_number == 'q':
        break
    elif elf_number == '':
        print('new elf babbeeeee')
        elf_list.append(elf_calories)
        elf_calories = 0
    else:
        elf_calories = elf_calories + int(elf_number)

sorted_list = sorted(elf_list)

print(sorted_list[-1] + sorted_list[-2] + sorted_list[-3])