# завдання 1

class Car:
    def __init__(self):
        self.__model_name = None
        self.__year_of_manufacture = None
        self.__producer = None
        self.__engine_volume = None
        self.__car_color = None
        self.__price = None
    def __str__(self):
        return f"model name: {self.__model_name}\nyear of manufacture: {self.__year_of_manufacture}\nproducer: {self.__producer}\nengine volume: {self.__engine_volume}\ncar color: {self.__car_color}\nprice: {self.__price}"
    def get_car(self):
        return f"model name: {self.__model_name}\nyear of manufacture: {self.__year_of_manufacture}\nproducer: {self.__producer}\nengine volume: {self.__engine_volume}\ncar color: {self.__car_color}\nprice: {self.__price}"
    def set_car(self, model_name, year_of_manufacture, producer, engine_volume, car_color, price):
        self.__model_name = model_name
        self.__year_of_manufacture = year_of_manufacture
        self.__producer = producer
        self.__engine_volume = engine_volume
        self.__car_color = car_color
        self.__price = price

car = Car()
car.set_car("Volvo", 2011, "Volvo Cars", 5, "Blue", 16400)
print(car.get_car())
print(car)

# завдання 2

class Book:
    def __init__(self):
        self.__book_name = None
        self.__year_of_publication = None
        self.__publisher = None
        self.__genre = None
        self.__author = None
        self.__price = None
    def __str__(self):
        return f"book name: {self.__book_name}\nyear of publication: {self.__year_of_publication}\npublisher: {self.__publisher}\ngenre: {self.__genre}\nauthor: {self.__author}\nprice: {self.__price}"
    def get_book(self):
        return f"book name: {self.__book_name}\nyear of publication: {self.__year_of_publication}\npublisher: {self.__publisher}\ngenre: {self.__genre}\nauthor: {self.__author}\nprice: {self.__price}"
    def set_book(self, book_name, year_of_publication, publisher, genre, author, price):
        self.__book_name = book_name
        self.__year_of_publication = year_of_publication
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

book = Book()
book.set_book(None, 2014, None, "fantasy", None, 120)
print(book.get_book())
print(book)

# завдання 3

class Stadium:
    def __init__(self):
        self.__stadium_name = None
        self.__opening_date = None
        self.__country = None
        self.__city = None
        self.__capacity = None
    def __str__(self):
        return f"stadium name: {self.__stadium_name}\nopening date: {self.__opening_date}\ncountry: {self.__country}\ncity: {self.__city}\ncapacity: {self.__capacity}"
    def get_stadium(self):
        return f"stadium name: {self.__stadium_name}\nopening date: {self.__opening_date}\ncountry: {self.__country}\ncity: {self.__city}\ncapacity: {self.__capacity}"
    def set_stadium(self, stadium_name, opening_date, country, city, capacity):
        self.__stadium_name = stadium_name
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__capacity = capacity

stadium = Stadium()
stadium.set_stadium(None, None, "Ukraine", "Kyiv", None)
print(stadium.get_stadium())
print(stadium)