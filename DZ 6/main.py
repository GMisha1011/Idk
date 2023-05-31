result = []

def divider(a, b):
    if a < b:
        raise ValueError("a должно быть больше или равно b")
    if b > 100:
        raise IndexError("b должно быть меньше или равно 100")
    return a/b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except IndexError as ie:
        print(f"IndexError: {ie}")
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: {zde}")
    except Exception as e:
        print(f"Unexpected error: {e}")

print(result)