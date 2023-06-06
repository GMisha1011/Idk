def safe_calculator_decorator(func):
    def wrapper(expression):
        try:
            result = func(expression)
        except ZeroDivisionError:
            result = "Ошибка: Деление на ноль"
        except SyntaxError:
            result = "Ошибка: Неправильный синтаксис"
        except Exception as e:
            result = f"Ошибка: {e}"
        return result
    return wrapper

@safe_calculator_decorator
def calculate(expression):
    return eval(expression)