import math

# Дополнительные тесты для filter (фильтрации)
def test_filter_odd_numbers():
    result = list(filter(lambda x: x % 2 != 0, [1, 2, 3, 4, 5, 6]))
    assert result == [1, 3, 5]

def test_filter_strings_with_a():
    result = list(filter(lambda x: 'a' in x, ["apple", "banana", "cherry", "date"]))
    assert result == ["apple", "banana", "date"]

def test_filter_large_numbers():
    result = list(filter(lambda x: x > 100, [50, 150, 200, 30, 400]))
    assert result == [150, 200, 400]

def test_filter_all_true():
    result = list(filter(lambda x: True, [1, 2, 3, 4, 5]))
    assert result == [1, 2, 3, 4, 5]

# Дополнительные тесты для map (отображения)
def test_map_double_numbers():
    result = list(map(lambda x: x * 2, [1, 2, 3, 4]))
    assert result == [2, 4, 6, 8]

def test_map_concat_strings():
    result = list(map(lambda x: x + "!", ["hi", "hello", "hey"]))
    assert result == ["hi!", "hello!", "hey!"]

def test_map_with_multiple_lists():
    result = list(map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]))
    assert result == [5, 7, 9]

def test_map_empty_string_list():
    result = list(map(lambda x: x.upper(), []))
    assert result == []

# Дополнительные тесты для sorted (сортировки)
def test_sorted_with_negative_numbers():
    result = sorted([-3, 1, -5, 2, 4])
    assert result == [-5, -3, 1, 2, 4]

def test_sorted_empty_list():
    result = sorted([])
    assert result == []

# Дополнительные тесты для math.pi
def test_math_pi_precision():
    assert round(math.pi, 2) == 3.14
    assert round(math.pi, 3) == 3.142

# Дополнительные тесты для math.sqrt
def test_math_sqrt_fractional():
    assert math.isclose(math.sqrt(2), 1.41421356237, rel_tol=1e-9)

def test_math_sqrt_large_number():
    assert math.sqrt(1000000) == 1000

def test_math_sqrt_zero():
    assert math.sqrt(0) == 0

# Дополнительные тесты для math.pow
def test_math_pow_zero_base():
    assert math.pow(0, 5) == 0
    assert math.pow(0, 0) == 1  # 0^0 трактуется как 1

def test_math_pow_negative_base():
    assert math.pow(-2, 3) == -8
    assert math.pow(-2, 4) == 16

# Дополнительные тесты для math.hypot
def test_math_hypot_multiple_args():
    assert math.hypot(1, 1, 1) == math.sqrt(3)
    assert math.hypot(2, 2, 2) == math.sqrt(12)

def test_math_hypot_large_numbers():
    assert math.hypot(300, 400) == 500

def test_math_hypot_zero_args():
    assert math.hypot(0, 0, 0) == 0
