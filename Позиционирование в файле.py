def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for line_num, line in enumerate(strings, start=1):
            # Получаем текущую позицию байта перед записью строки
            byte_position = file.tell()
            # Записываем строку с переходом на новую строку
            file.write(line + '\n')
            # Сохраняем позицию строки и её текст в словарь
            strings_positions[(line_num, byte_position)] = line
    return strings_positions

# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
