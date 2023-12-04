first_name = 'Pero'
last_name = 'Peric'

full_name = first_name + ' ' + last_name

print(full_name)

message = 'Puno ime i prezime je:' + ' ' + first_name + ' ' + last_name
print(message)

#'Puno ime i prezime je:' + ' ' + first_name + ' ' + last_name

puno_ime = 'Puno ime i prezime je: {} {}'.format(first_name, last_name)
print(puno_ime)

a = 8
v_a = 5
area = (a * v_a) / 2

print('Povrsina trokuta (a * v_a) / 2, za a = 8 i v_a = 5, iznosi: {}'.format(area))

print()
print()

puno_ime = f'Puno ime i prezime je: {first_name} {last_name}'

print(puno_ime)