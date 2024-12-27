def calculate_discriminant(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) \
            or not isinstance(c, (int, float)):
        raise ValueError("Параметры a, b и c должны быть числами.")
    return b ** 2 - 4 * a * c
