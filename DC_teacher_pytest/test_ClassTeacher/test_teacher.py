# 1.1 Тестирует свойства объекта Teacher через геттеры
import pytest


def test_teacher_properties(teacher):
    # Проверяем, что имя учителя задано корректно
    assert teacher.name == "Иван Петров"
    # Проверяем, что образование соответствует заданному
    assert teacher.education == "БГПУ"
    # Проверяем, что опыт работы соответствует значению
    assert teacher.experience == 4

# 1.2 Тест метода get_teacher_data — возвращает всю информацию об учителе в строке
def test_teacher_get_data(teacher):
    # Проверяем, что метод возвращает корректную строку с данными учителя
    assert teacher.get_teacher_data() == "Иван Петров, образование БГПУ, опыт работы 4 года"

# 1.3 Тест сеттера для поля experience — задаёт новый опыт работы
def test_teacher_set_experience(teacher):
    teacher.experience = 10  # Устанавливаем опыт работы 10 лет
    assert teacher.experience == 10  # Проверяем, что он действительно установлен

# 1.4 Тест проверки, что отрицательный опыт не устанавливается и выдаёт сообщение
def test_teacher_set_negative_experience(teacher):
    with pytest.raises(ValueError, match="Опыт не может быть отрицательным!"): #with pytest.raises(ValueError) проверяет, что в этом блоке будет выброшена ошибка ValueError.
        teacher.experience = -1  #match="..." - проверяет, что текст ошибки соответствует строке "Опыт не может быть отрицательным!"


# 2 Тест методов добавления и удаления оценки студенту
def test_teacher_marks(teacher):
    # Добавляем оценку студенту и проверяем результат
    assert teacher.add_mark("Алексей", 5) == "Иван Петров поставил оценку 5 студенту Алексей"
    # Удаляем оценку и проверяем сообщение
    assert teacher.remove_mark("Алексей") == "Иван Петров удалил оценку 5 студенту Алексей"

# 3 Тестирует геттеры класса-наследника DisciplineTeacher
def test_discipline_teacher_properties(discipline_teacher):
    # Проверка, что должность задана корректно
    assert discipline_teacher.job_title == "директор"
    # Проверка, что предмет задан корректно
    assert discipline_teacher.discipline == "Химия"

# 3.1 Тест установки новой должности (валидное значение)
def test_set_job_title_valid(discipline_teacher):
    discipline_teacher.job_title = "завуч"  # Меняем должность
    assert discipline_teacher.job_title == "завуч"  # Проверяем, что новое значение установилось

#3.1.1 Тест установки невалидной должности (не строка)
def test_set_job_title_invalid(discipline_teacher):
    # Проверяем, что при передаче не строки вызывается ошибка ValueError
    with pytest.raises(ValueError, match="Должность не определенна"):
        discipline_teacher.job_title = 123  # Некорректный тип

# 3.2 Тест метода get_teacher_data для класса-наследника DisciplineTeacher(Teacher)
def test_discipline_teacher_get_data(discipline_teacher):
    result = discipline_teacher.get_teacher_data()  # Получаем строку с данными
    assert "Предмет Химия" in result  # Проверяем, что есть упоминание предмета
    assert "должность директор" in result  # Проверяем, что указана должность


# 4 Тест метода консультации у класса-наследника
def test_consultation_text(discipline_teacher):
    result = discipline_teacher.give_a_consultation("9Б")  # Вызываем консультацию
    # Проверяем, что возвращаемая строка соответствует ожидаемой
    assert result == "Иван Петров провел консультацию в классе 9Б\nПо предмету Химия как директор"

# 5.1 Тест метода add_mark для DisciplineTeacher
def test_discipline_teacher_add_mark(discipline_teacher):
    result = discipline_teacher.add_mark("Алексей", 4)
    assert "Иван Петров поставил оценку 4 студенту Алексей" in result
    assert "Предмет Химия" in result

# 5.2 Тест метода remove_mark для DisciplineTeacher
def test_discipline_teacher_remove_mark(discipline_teacher):
    discipline_teacher.add_mark("Алексей", 4)
    result = discipline_teacher.remove_mark("Алексей")
    assert "Иван Петров удалил оценку 4 студенту Алексей" in result
    assert "Предмет Химия" in result
