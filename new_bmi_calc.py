def calculate_bmi(weight, height):
    """Calculate BMI using standard formula."""
    return weight / (height ** 2)

def interpret_bmi(bmi):
    """Interpretation according to WHO classification."""
    if bmi < 18.5:
        return "Недостаточная масса тела"
    elif 18.5 <= bmi < 25:
        return "Норма"
    elif 25 <= bmi < 30:
        return "Избыточная масса тела"
    else:
        return "Ожирение"

def main():
    print("=== Калькулятор индекса массы тела (BMI) ===")

    try:
        weight = float(input("Введите ваш вес (кг): "))
        height = float(input("Введите ваш рост (в метрах): "))
    except ValueError:
        print("Ошибка: нужно вводить числа!")
        return

    bmi = calculate_bmi(weight, height)
    interpretation = interpret_bmi(bmi)

    print(f"\nВаш BMI: {bmi:.2f}")
    print(f"Интерпретация: {interpretation}")

if __name__ == "__main__":
    main()
