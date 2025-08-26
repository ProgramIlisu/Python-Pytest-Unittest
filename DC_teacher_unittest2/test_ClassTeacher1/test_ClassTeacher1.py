
import unittest

from ClassTeacher.teacher import Teacher, DisciplineTeacher

# Класс TestTeacher - тестирует обычного учителя
# Это класс с тестами для базового класса Teacher
class TestTeacher(unittest.TestCase):  #Наследуемся от unittest.TestCase - это базовый класс для всех тестов.
    # Этот метод выполняется перед каждым тестом: создаём объект учителя
    def setUp(self):  #setUp() создаёт объект перед каждым тестом, чтобы не дублировать создание вручную.
        self.teacher = Teacher("Иван Петров", "БГПУ", 4)

    def test_get_name(self):
        # Тестирует, правильно ли возвращается имя через геттер
        self.assertEqual(self.teacher.name,"Иван Петров")  # Проверка, что имя корректное
        #assertEqual для проверки, совпадает ли результат с ожиданием.

    def test_get_education(self):
        # Тестирует, правильно ли возвращается образование
        self.assertEqual(self.teacher.education, "БГПУ") # Проверка, что образование корректное

    def test_experience_invalid(self):
        # Тест проверяет, что установка отрицательного опыта вызывает исключение ValueError
        with self.assertRaises(ValueError): # Ожидаем, что произойдёт ошибка. assertRaises для проверки, что в определённых ситуациях выбрасываются ошибки.
            self.teacher.experience = -5 # Пытаемся установить неправильное значение


    def test_teacher_get_data(self):
        # Тестирует метод get_teacher_data, должен возвращать корректную строку
        expected = "Иван Петров, образование БГПУ, опыт работы 4 года"
        self.assertEqual(self.teacher.get_teacher_data(), expected) # Сравниваем результат с ожидаемым

    def test_add_mark(self):
        # Тестирует добавление оценки студенту
        result = self.teacher.add_mark("Алексей", 5)
        self.assertEqual(result, "Иван Петров поставил оценку 5 студенту Алексей")

    def test_remove_mark(self):
        # Тестирует удаление оценки
        self.teacher.add_mark("Алексей", 5)  # Сначала ставим оценку
        result = self.teacher.remove_mark("Алексей")  # Затем удаляем
        self.assertEqual(result, "Иван Петров удалил оценку 5 студенту Алексей") # Проверка результата

    def test_experience_setter_valid(self):
        # Проверка работы сеттера: задаём новое допустимое значение
        self.teacher.experience = 10 # Меняем опыт
        self.assertEqual(self.teacher.experience, 10)  # Проверяем, что значение изменилось

#Класс TestDisciplineTeacher - тест наследника
#Тестируем DisciplineTeacher - он расширяет Teacher.
class TestDisciplineTeacher(unittest.TestCase):
    def setUp(self):
        # Создаём объект с нужными параметрами для всех тестов
        self.disc_teacher= DisciplineTeacher("Иван Петров", "БГПУ", 4, "Химия", "директор")

    def test_get_discipline(self):
        # Тестирует геттер discipline
        self.assertEqual(self.disc_teacher.discipline, "Химия")

    def test_get_teacher_data(self):
        # Проверяет, что метод get_teacher_data у наследника корректно добавляет предмет и должность
        result = self.disc_teacher.get_teacher_data()
        self.assertIn("Предмет Химия", result) # Проверяем наличие строки про предмет
        self.assertIn("должность директор", result) # Проверяем наличие строки про должность

    def test_add_mark(self):
        # Тест добавления оценки и расширенного вывода (с предметом)
        result = self.disc_teacher.add_mark("Алексей", 5)
        self.assertIn("Иван Петров поставил оценку 5 студенту Алексей", result) # Проверка оценки
        self.assertIn("Предмет Химия", result) # Проверка наличия предмета в выводе

    def test_remove_mark(self):
        # Тест удаления оценки и проверка вывода с предметом
        self.disc_teacher.add_mark("Алексей", 5)  # Ставим оценку
        result = self.disc_teacher.remove_mark("Алексей") # Удаляем
        self.assertIn("Иван Петров удалил оценку 5 студенту Алексей", result)  # Проверка текста
        self.assertIn("Предмет Химия", result) # Проверка предмета

    def test_give_consultation(self):
        # Тест метода консультации у наследника
        result = self.disc_teacher.give_a_consultation("9Б") # Проводим консультацию
        expected = "Иван Петров провел консультацию в классе 9Б\nПо предмету Химия как директор"
        self.assertEqual(result, expected)  # Проверка результата

    def test_job_title_getter(self):
        # Проверка геттера: сначала устанавливаем значение
        self.disc_teacher.job_title = "завуч" # Меняем должность
        self.assertEqual(self.disc_teacher.job_title, "завуч")  # Проверяем, что значение установилось

    def test_job_title_setter_invalid(self):
        # Проверка: при передаче нестрокового значения должно быть исключение
        with self.assertRaises(ValueError): # Ожидаем ValueError
            self.disc_teacher.job_title = 123 # Пытаемся установить недопустимое значение


