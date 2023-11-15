class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not all(isinstance(side, (int, float)) and side > 0 for side in [self.a, self.b, self.c]):
            return "Потрібно вводити тільки числа"
        elif self.a + self.b > self.c and self.b + self.c > self.a and self.c + self.a > self.b:
            return "Ура, можна побудувати трикутник"
        else:
            return "Жаль, але з цього трикутник не зробити."

class Triangle(TriangleChecker):
    pass

class ExtTriangle(Triangle):
    def is_triangle(self):
        result = super().is_triangle()
        if result == "Ура, можна побудувати трикутник!":
            return "Ура, можна побудувати трикутник!"
        elif result == "Потрібно вводити тільки числа!":
            return "З негативними числами нічого не вийде!"
        else:
            return result

# Приклад використання:
triangle1 = ExtTriangle(3, 4, 5)
print(triangle1.is_triangle())

triangle2 = ExtTriangle(-1, 2, 3)
print(triangle2.is_triangle())

triangle3 = ExtTriangle("a", 2, 3)
print(triangle3.is_triangle())

triangle4 = ExtTriangle(1, 1, 3)
print(triangle4.is_triangle())  
