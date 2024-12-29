import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_invalid_length_0(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert '' not in collector.books_genre

    def test_set_book_genre_valid_book(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_book_genre('Сияние') == 'Ужасы'

    def test_get_book_genre_valid_book(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_book_genre('Ужасы') == ['Сияние']

    def test_get_books_with_specific_genre_2_valid_books(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Хребты безумия')
        collector.set_book_genre('Хребты безумия', 'Ужасы')
        assert collector.get_books_genre('Ужасы') == ['Сияние', 'Хребты безумия']

    def test_get_books_genre_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        assert collector.get_books_genre() == {'Сияние': ''}

    def test_get_books_for_children_valid_book(self):
        collector = BooksCollector()
        collector.add_new_book('Незнайка на Луне')
        collector.set_book_genre('Незнайка на Луне', 'Комедия')
        assert 'Незнайка на Луне' in collector.get_books_for_children()

    def test_get_books_for_children_invalid_book(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert 'Сияние' not in collector.get_books_for_children()

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.add_book_in_favorites('Сияние')
        assert 'Сияние' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.add_book_in_favorites('Сияние')
        collector.delete_book_from_favorites('Сияние')
        assert 'Сияние' not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('books, genre', [('Сияние', 'Ужасы'),
                                              ('Незнайка на Луне', 'Комедия'),
                                              ('11/22/63', 'Фантастика')
                                             ]
                             )
    def test_get_list_of_favorites_books_3_books(self, books, genre):
        collector = BooksCollector()
        collector.add_new_book(books)
        collector.set_book_genre(books, genre)
        collector.add_book_in_favorites(books)
        assert books in collector.get_list_of_favorites_books()
