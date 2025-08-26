"""
У вас есть абстракция учитель, где написал класс
согласно этой абстракции характеристики класса:
Поля (атрибуты) класса class Teacher:
имя (name) в примере Иван Петров;
образование (education) в примере БГПУ;
опыт работы (experience) в примере 4 года;
Все данные атрибуты сделал защищенными.
Для данных атрибутов написал геттеры (для всех),
а для атрибута опыт работы (experience) также еще и сеттер.
Методы класса Teacher.
get_teacher_data возвращает информацию об учителе результат вызова метода:
add_mark в качестве аргументов принимает имя студента и его оценку, результат вызова метода:
remove_mark в качестве аргументов принимает имя студента и его оценку, результат вызова метода:
give_a_consultation в качестве аргумента принимает, класс в котором учатся ученики, результат вызова метода:"""

class Teacher:
    def __init__(self, name, education, experience):  #Как я понял что метод init это конструктор. self это ссылка на текущий экземпляр (объект) класса Teacher. Позволяет обращаться к его внутренним переменным и методам.
        self.__name = name   # Приватный атрибут name
        self.__education = education
        self.__experience = experience
        self.__ratings = {} #Приватный словарь, хранит оценки студентов

    # Геттер имени
    @property    # Идет декоратор позволяет получить имя через teacher.name, а не через teacher.get_name()
    def name(self):
        return self.__name

    # Геттер образования
    @property
    def education(self):
        return self.__education

    # Геттер опыта
    @property
    def experience(self):
        return self.__experience

    # Сеттер для experience
    @experience.setter
    def experience(self, value):
        if isinstance(value, int) and value >= 0: # Я использовал isinstance() это встроенная функция в Python, которая проверяет, относится ли переменная к определённому типу данных.
            self.__experience = value
        else:
            raise ValueError("Опыт не может быть отрицательным!") # Здесь я использовал raise ValueError для явного выбрасывания ошибки исключения, если в experience передано неправильное значение


    def get_teacher_data(self):
        return f"{self.__name}, образование {self.__education}, опыт работы {self.__experience} года"

    def add_mark(self, student_name, rating):
        self.__ratings[student_name] = rating   #здесь идет обращение к защищенному словарю (self.__ratings), а [student_name] = rating - добавляет или обнавляет запись в словаре
        return f"{self.__name} поставил оценку {rating} студенту {student_name}"

    def remove_mark(self, student_name):
        if student_name in self.__ratings:   # Проверяет, есть ли такой студент
            removed_mark = self.__ratings[student_name]  # Сохраняет удаляемую оценку
            del self.__ratings[student_name]   # Удаляет оценку через метод del для удаления объектов, включая элементы из списков и переменные.
        return f"{self.__name} удалил оценку {removed_mark} студенту {student_name}"


    def give_a_consultation(self, class_name):
        return f"{self.__name} провел консультацию в классе {class_name}"


# if __name__ == '__main__':
#     teacher_name = Teacher("Иван Петров", "БГПУ", 4)
#     print(teacher_name.get_teacher_data())
#     print(teacher_name.add_mark("Петр Сидоров", 4))
#     teacher_name.add_mark("Дмитрий Степанов", 3)  #Здесь мы ставим оценку Дмитрий Степанов
#     print(teacher_name.remove_mark("Дмитрий Степанов"))  #А Здесь уже удаляем оценку
#     print(teacher_name.give_a_consultation("9Б"))
#     print()


"""
Второй класс наследник DisciplineTeacher, его классом родителем (базовым классом) будет класс
Teacher, к нему добавил 2 новых атрибута (поля).
discipline - предмет который он ведет; 
job_title - должность (например завуч, директор, учитель
старших классов).
Все атрибуты также сделал защищенными.
Для данных атрибутов написал геттеры (для всех), а для атрибута job_title еще добавил сеттер.
Далее адаптировал методы класса родителя а именно:
get_teacher_data
add_mark
remove_mark
give_a_consultation
"""

class DisciplineTeacher(Teacher):

    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)  # Вызов конструктора родительского класса
        self.__discipline = discipline
        self.__job_title = job_title

    @property
    def discipline(self):
        return self.__discipline

    @property
    def job_title(self):
        return self.__job_title

    @job_title.setter
    def job_title(self, new_title):
        if isinstance(new_title, str): # С помощью функции isinstance - используется для проверки принадлежности объекта к определенному классу. Проверка: значение должно быть строкой
            self.__job_title = new_title
        else:
            raise ValueError("Должность не определенна")  #в данном контексте используется для выбрасывания исключения, если в experience передано неправильное значение


    def get_teacher_data(self):
        base_info = super().get_teacher_data() # так мы здесь получаем данные из родителя
        return f"{base_info}\nПредмет {self.__discipline}, должность {self.__job_title}"

    def add_mark(self, student_name, rating):
        base = super().add_mark(student_name, rating)  # Используем поведение родителя
        return f"{base}\nПредмет {self.__discipline}"

    def remove_mark(self, student_name):
        base = super().remove_mark(student_name)
        return f"{base}\nПредмет {self.__discipline}"

    def give_a_consultation(self, class_name):
        base = super().give_a_consultation(class_name)
        return f"{base}\nПо предмету {self.__discipline} как {self.__job_title}"

# if __name__ == '__main__':
#     t = DisciplineTeacher("Иван Петров", "БГПУ", 4, "Химия", "директор")
#     print(t.get_teacher_data())
#     print(t.add_mark("Петр Сидоров", 4))
#     t.add_mark("Дмитрий Степанов", 3)  # Здесь мы ставим оценку Дмитрий Степанов. Она просто добавляется, без вывода
#     print(t.remove_mark("Дмитрий Степанов"))  # А Здесь уже удаляем оценку
#     print(t.give_a_consultation("10Б"))


