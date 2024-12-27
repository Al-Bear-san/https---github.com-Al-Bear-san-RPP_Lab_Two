from script import calculate_discriminant


def test_discriminant_positive():
    # D > 0
    if not calculate_discriminant(1, 5, 1) > 0:
        raise AssertionError("Discriminant should be positive")
    if not calculate_discriminant(2, 8, 3) > 0:
        raise AssertionError("Discriminant should be positive")


def test_discriminant_zero():
    # D = 0
    if not calculate_discriminant(1, 2, 1) == 0:
        raise AssertionError("Discriminant should be zero")
    if not calculate_discriminant(4, 4, 1) == 0:
        raise AssertionError("Discriminant should be zero")


def test_discriminant_negative():
    # D < 0
    if not calculate_discriminant(5, 10, 25) < 0:
        raise AssertionError("Discriminant should be negative")
