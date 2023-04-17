# Определяем функцию для извлечения данных из строки по символу разделителя
def get_data(line, sep):
    # Разделяем строку по символу разделителя
    result = line.split(sep)
    # Возвращаем второй элемент результата или пустую строку, если он отсутствует
    return result[1].strip() if len(result) > 1 else ""

# Открываем файл .txt для чтения
f = open("kaspas.txt", "r")
# Создаем пустой список для хранения данных
data = []
# Читаем файл построчно
for line in f:
    # Пропускаем пустые строки и разделители ---
    if line.strip() == "" or line.strip() == "---":
        continue
    # Извлекаем данные из строки по формату с помощью функции get_data
    website_name = get_data(line, ": ")
    website_url = get_data(f.readline(), ": ")
    login_name = get_data(f.readline(), ": ")
    login = get_data(f.readline(), ": ")
    password = get_data(f.readline(), ": ")
    comment = get_data(f.readline(), ": ")
    # Добавляем данные в список в виде кортежа
    data.append((website_name, website_url, login, password, comment))
# Закрываем файл .txt
f.close()
# Открываем файл .csv для записи
f = open("file.csv", "w")
# Записываем заглавную строку в файл с разделителем ";"
f.write("name; url; login; password; comment;\n")
# Записываем данные в файл построчно с разделителем запятая
for row in data:
    f.write(";".join(row) + "\n")
# Закрываем файл .csv
f.close()