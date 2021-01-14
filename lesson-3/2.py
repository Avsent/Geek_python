def data(**kwargs):
    print(kwargs)


data(
    name = input('Enter name - '),
    surname = input('Enter surname - '),
    birthday = input('Enter birthday - '),
    town = input('Enter live town - '),
    e_mail = input('Enter e-mail - '),
    phone_number = input('Enter phone_number - ')
)
