import base64
import sys

# Проверяем, был ли передан аргумент командной строки (имя входного файла)
if len(sys.argv) < 2:
    print("Использование: python script_name.py <имя_входного_файла>")
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = 'file.txt'

try:
    # Открываем входной файл для чтения в бинарном режиме ('rb')
    with open(input_filename, "rb") as f_in:
        file_content = f_in.read()
        b64 = base64.b64encode(file_content).decode()
        
    # Открываем выходной файл для записи ('w')
    with open(output_filename, 'w') as f_out:
        f_out.write(b64)
        print(f"Файл '{input_filename}' успешно закодирован в Base64 и сохранен в '{output_filename}'")

except FileNotFoundError:
    print(f"Ошибка: Файл '{input_filename}' не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")

