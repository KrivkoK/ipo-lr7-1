# Словарь
books = [
    {'title': 'Война и мир', 'author': 'Лев Толстой', 'year': '1985'},
    {'title': 'Дом в котором', 'author': 'Мариам Петросян', 'year': '1583'},
    {'title': 'Портрет Дориана Грея', 'author': '	Оскар Уайльд', 'year': '1890'},
    {'title': 'Маленькие женщины', 'author': '	Луиза Мэй Олкотт', 'year': '1868'},
    {'title': 'Преступление и наказание', 'author': 'Фёдор Достоевский', 'year': '1865-1866'},
]

# Перебор всех книг и вывод информации
for index in range(len(books)):
    print(f"--Книга {index + 1}---")
    print(f"Название: {books[index]['title']}, Автор: {books[index]['author']}")
    print(f"--- {books[index]['year']}---")
    print()
