from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGroupBox, QButtonGroup, QVBoxLayout, QHBoxLayout, QRadioButton
import random
from random import shuffle


## Класс 

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question ## Заполняем переменные значениями по умолчанию
        self.right_answer = right_answer ## Заполняем переменные значениями по умолчанию
        self.wrong1 = wrong1 ## Заполняем переменные значениями по умолчанию
        self.wrong2 = wrong2 ## Заполняем переменные значениями по умолчанию
        self.wrong3 = wrong3 ## Заполняем переменные значениями по умолчанию

## Функции

def start():
    ask(questions_list[num])

def clicked():
    if answer_button.text() == 'Начать': ## Проверяем текст на кнопке, если "Начать", то
        buttons_box.show() ## Показываем группу с кнопками
        answer_button.setText('Ответить') ## Меняем текст на кнопке на "Ответить"
        ask(questions_list[num]) ## Задаём первый вопрос
    elif answer_button.text() == 'Ответить': ## Если текст на кнопке "Ответить"
        check_answer() ## Запускаем функцию для прверки ответа
    elif answer_button.text() == 'Следующий вопрос': ## Если текст на кнопке "Следующий вопрос"
        next_question() ## Запускаем функцию для показа следующего вопроса
    elif answer_button.text() == 'Пройти тестирование снова': ## Если текст на кнопке "Пройти тестирование снова"
        shuffle(questions_list) ## Перемешиваем список вопросов
        start() ## Запускаем тестирование сначала

def show_question():
    answers_box.hide() ## Скрываем группу с ответом на вопрос
    buttons_group.setExclusive(False) ## Разрешаем изменять состояние выбора ответа
    button1.setChecked(False) ## Убираем маркер выбора с первой кнопки
    button2.setChecked(False) ## Убираем маркер выбора со второй кнопки
    button3.setChecked(False) ## Убираем маркер выбора с третьей кнопки
    button4.setChecked(False) ## Убираем маркер выбора с четвёртой кнопки
    buttons_group.setExclusive(True) ## Запрещаем изменять состояние выбора кнопок
    buttons_box.show() ## Показываем очищенную группу с кнопками
    answer_button.setText('Ответить') ## Изменяем текст кнопки на "Ответить"

def show_result():
    buttons_box.hide() ## Скрываем группу с кнопками
    answers_box.show() ## Показываем группу с ответами
    answer_button.setText('Следующий вопрос') ## Меняем текст кнопки на "Следующий вопрос"
    

def ask(quest):
    global num ## В функцию добавляем глобальную переменную
    shuffle(answers) ## Перемешиваем кнопки
    main_question.setText(quest.question) ## Изменяем текст в заголовке на текст вопроса
    answers[0].setText(quest.right_answer) ## В первую кнопку из списка добавляем правильный ответ 
    answers[1].setText(quest.wrong1) ## Во вторую кнопку из списка добавляем один из неправильных ответов
    answers[2].setText(quest.wrong2) ## В третью кнопку из списка добавляем правильный ответ
    answers[3].setText(quest.wrong3) ## В четвёртую кнопку из списка добавляем посл
    right_answer_label.setText(quest.right_answer) ## В заголовок вставляем правильный ответ
    show_question() ##  Вызываем функцию для вывода вопроса

def check_answer():
    if answers[0].isChecked(): ## Если выбран верный вариант ответа, то
        result_label.setText('Верно') ## В заголовок выводим "Верно"
        stats(True) ## В функцию для подсчёта статистики передаём аргумент, определяющий правильность ответа. В данный момент верно
    else: ## Иначе
        result_label.setText('Неверно') ## В заголовок выводим "Неверно"
        stats(False) ## В функцию для подсчёта статистики передаём аргумент, определяющий правильность ответа. В данном случае неверно
    show_result() ## Вызываем функцию для отображения результата

def next_question():
    global num ## В функцию подключаем глобальную переменную-счётчик
    if (len(questions_list) - 1) == num: ## Проверяем все ли вопросы были показаны, если все, то
        test_end() ## Вызываем функцию для завершения тестирования
    else: ## Иначе
        num += 1 ## Увеличиваем переменную-счётчик на 1, для показа следующего вопроса
        ask(questions_list[num]) ## Вызываем функцию для показа следующего вопроса

def stats(arg):
    global successfully_answered ## В функцию подключаем глобальную переменную, в которой хранится число вопросов с верным ответом
    global rating ## В функцию подключаем глобальную переменную, в которой хранится рейтинг
    total_questions = len(questions_list) ## Создаём переменную, в которую вносим общее количество вопросов
    if arg: ## Если ответ на вопрос правильный, то
        successfully_answered += 1 ## Засчитываем верный вариант ответа
    rating = (successfully_answered / total_questions) * 100 ## Высчитываем актуальный рейтинг
    print('Всего вопросов:', total_questions) ## Выводим общее число вопросов
    print('Правильных ответов:', successfully_answered) ## Выводим количество правильных ответов
    print('Рейтинг:', rating) ## Выводим рейтинг
    print('--------------------') ## Выводим сепаратор для визуального разграничения между вопросами

def test_end():
    global successfully_answered ## Подключаем глобальную переменную с количеством верных ответов
    global rating ## Подключаем глобальную переменную с рейтингом
    global num ## Подключаем глобальную переменную с рейтингом
    main_question.setText('Тестирование закончено') ## Изменяем текст заголовка
    answer_button.setText('Пройти тестирование снова') ## Меняем текст кнопки
    print('Тестирование подошло к концу.') ## Объявляем о завершении тестирования
    print(f'Вы успешно ответили на {successfully_answered} вопросов из {len(questions_list)}.') ## Выводим количество верных ответов и общее количество вопросов
    print(f'Ваш рейтинг по оканчанию тестирования равен {rating}.') ## Выводим Конечный рейтинг
    num = 0 ## Обнуляем переменную-счётчик
    successfully_answered = 0 ## Обнуляем переменную с верными ответами
    rating = 0 ## Обнуляем переменную с рейтингом
    buttons_box.hide() ## Скрываем группу с вариантами ответов
    answers_box.hide() ## Скрываем группу с ответами
    

## Конфиг приложения

app = QApplication([]) ## Создаём приложение
window = QWidget() ## Создаём окно
window.setWindowTitle('Memory Card') ## Задаём название для окна
window.resize(400, 300) ## Задаём размер окна

## Вопросы

q = Question('2 + 2 = ?', '4', '5', '1', '2')
q1 = Question('2 + 3 = ?', '5', '3', '1', '2')
q2 = Question('3 + 4 = ?', '7', '3', '1', '4')
q3 = Question('2 + 5 = ?', '7', '5', '2', '1')
q4 = Question('6 + 2 = ?', '8', '1', '6', '2')

questions_list = [q, q1, q2, q3, q4] ## Объединяем вопросы в список
shuffle(questions_list) ## Перемешиваем список с вопросамии

num = 0 ## Создаём переменную-счётчик
successfully_answered = 0 ## Создаём переменную, в которой будет храниться количество правильных ответов
rating = 0 ## Создаём переменную, где будет храниться рейтинг

## Направляющие

v_main = QVBoxLayout()
buttons_box_v = QVBoxLayout()
answers_box_v = QVBoxLayout()
buttons_box_v_left = QVBoxLayout()
buttons_box_v_right = QVBoxLayout()
buttons_box_h_lower = QHBoxLayout()

## Конфиг виджетов

main_question = QLabel('Готовы ли вы начать тестирование?')
answer_button = QPushButton('Начать')
button1 = QRadioButton()
button2 = QRadioButton()
button3 = QRadioButton()
button4 = QRadioButton()

buttons_box = QGroupBox('Варианты ответов')
buttons_box_v_left.addWidget(button1)
buttons_box_v_left.addWidget(button2)
buttons_box_v_right.addWidget(button3)
buttons_box_v_right.addWidget(button4)
buttons_box_h_lower.addLayout(buttons_box_v_left)
buttons_box_h_lower.addLayout(buttons_box_v_right)
buttons_box.setLayout(buttons_box_h_lower)

buttons_group = QButtonGroup()
buttons_group.addButton(button1)
buttons_group.addButton(button2)
buttons_group.addButton(button3)
buttons_group.addButton(button4)

answers = [button1, button2, button3, button4]

answers_box = QGroupBox('Результат теста')

result_label = QLabel('Тут будет результат')
right_answer_label = QLabel('тут будет правильный ответ')

## Лэйауты

v_main.addWidget(main_question, alignment = Qt.AlignCenter)
v_main.addWidget(buttons_box)
v_main.addWidget(answers_box)
v_main.addWidget(answer_button)
answers_box_v.addWidget(result_label)
answers_box_v.addWidget(right_answer_label)

buttons_box.setLayout(buttons_box_h_lower)
answers_box.setLayout(answers_box_v)

buttons_box.hide()
answers_box.hide()
answer_button.clicked.connect(clicked)


window.setLayout(v_main) ## Привязываем основную направляющую к окну
window.show() ## Выводим окно
app.exec_() ## Запускаем приложение