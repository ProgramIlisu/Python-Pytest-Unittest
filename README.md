# Python-Pytest-Unittest
# 🏫 ClassTeacher Project

## 📌 Описание
Проект демонстрирует использование **ООП в Python** и написание **автотестов** с помощью Pytest и Unittest.
ВАЖНО: В PyCharm это 2 отдельных проекта, и запускать их тоже отдельно. Я сделал их вместе одной папкой для удобства и создания репозитория 

Реализованы два класса:  
- **`Teacher`** — базовый класс для описания учителя: имя, образование, опыт работы, методы для выставления и удаления оценок, проведение консультаций.  
- **`DisciplineTeacher`** — наследник, расширяющий функционал за счёт предмета (`discipline`) и должности (`job_title`). Методы переопределены так, чтобы в результатах учитывались предмет и должность.  

## 📂 Структура проекта
```
ClassTeacher/teacher.py       # Основной код с классами Teacher и DisciplineTeacher
test_ClassTeacher/conftest.py # Фикстуры для Pytest (создание тестовых объектов)
test_ClassTeacher/test_teacher.py # Автотесты Pytest
unitest_ClassTeacher/unitest_ClassTeacher.py # Тесты с использованием Unittest
```

## 🛠 Возможности
- Инкапсуляция: атрибуты скрыты (protected/private), доступ через геттеры/сеттеры.  
- Валидация данных: 
  - опыт работы не может быть отрицательным;  
  - должность должна быть строкой.  
- Автоматизированное тестирование: 
  - проверка геттеров и сеттеров;  
  - тестирование методов (`get_teacher_data`, `add_mark`, `remove_mark`, `give_a_consultation`);  
  - обработка ошибок через `pytest.raises`.  

## 🚀 Запуск тестов

### Pytest
```bash
pytest -v
```

### Unittest
```bash
python -m unittest discover unitest_ClassTeacher
```

## 📊 Проверка покрытия кода тестами
```bash
coverage run -m pytest
coverage html
```

После этого откройте `htmlcov/index.html` в браузере, чтобы посмотреть красивый отчёт о покрытии кода тестами.  

## 📸 Пример отчёта Coverage
В папке htmlcov

---

👨‍💻 Автор: *Denis(Programilisu) — начинающий AQA Engineer*
