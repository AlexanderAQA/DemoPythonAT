import pytest


def add(a, b):
    return a + b

@pytest.mark.edu
def test_add():
    result = add(2, 3)
    assert result == 4

# Что автоматизировать в первую очередь:
# регресс и смоук-тесты
# рутинные сценарии
# Приоритет: от наиболее критичного функционала

# "Плохие" кандидаты в автоматизацию:
# UI-дизайн проверки (нефункциональные)
# Везде где нужен человеческий взгляд
# Разовые, исследовательские тестирование

# На каждый тест кейс должен быть минимум 1 автотест

# Основа теста: Arrange-Act-Assert


#######################################
# ДЗ
def hello(text: str):
    return text

@pytest.mark.edu
def test_hello():
    assert hello('hello') == 'hello'



def some_text(text: str):
    return text * 52

@pytest.mark.edu
def test_some_text():
    result = some_text("a")
    assert result == "a" * 52

# Напиши 2 теста (пример с 7 строки) для функций say_hello и empty_text. Проверь, что ожидаемое и фактическое значение
# строки совпадают
