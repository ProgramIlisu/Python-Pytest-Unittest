
import pytest
from ClassTeacher.teacher import Teacher, DisciplineTeacher

# Фикстура создаёт объект Teacher
@pytest.fixture   # @pytest.fixture это декоратор фикстуры. Обозначает, что функция teacher() — это фикстура, т.е. заготовленный объект, который может использоваться в тестах.
def teacher():
    return Teacher("Иван Петров", "БГПУ", 4)

# Фикстура создаёт объект DisciplineTeacher
@pytest.fixture  # это фикстура объекта класса DisciplineTeacher и возвращает его для тестов.
def discipline_teacher():
    return DisciplineTeacher("Иван Петров", "БГПУ", 4, "Химия", "директор")


