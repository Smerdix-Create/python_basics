"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def about_user(**kwargs):
    print(f"{kwargs['name']} {kwargs['surname']} {kwargs['year']} года рождения, проживает в городе {kwargs['city']},"
          f"\n"
          f"email: {kwargs['email']}, телефон: {kwargs['phone_number']}")


about_user(name="Иван",
           surname="Иванов",
           year=1846,
           city="Москва",
           email="jackie@gmail.com",
           phone_number="01005321456")

