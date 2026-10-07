import math
class Triangle:
    """
    Проверка существования треугольника.
    Нахождение периметра и площади.
    Конструктор для проверки на треугольность, выбросить исключение, которое будет обрабатываться.
    Реализовать функцию внутри класса для расчёта углов можду сторонами( по теореме косинусов).
    Программа для демонстраци возможностей класса.
    """
    def __init__(self, a, b, c):
        if a <=0 or b<=0 or c<=0:
            raise ValueError("Стороны должны быить положительными числами")
        if not (a+b>c and b+c>a and c+a>b):
            raise ValueError("Нарушено неравенство треугольников")
        self.__a=a
        self.__b=b
        self.__c=c

    @property
    def a(self):
        return self.__a
    @property
    def b(self):
        return self.__b
    @property
    def c(self):
        return self.__c

    @property
    def  perimetr(self)->float:
        return self.__a+ self.__b+self.__c

    @property
    def area(self)->float:
        p=self.perimetr/2
        return (p*(p - self.__a)*(p - self.__b)*(p-self.__c))**0.5

    def ugls(self):
        cos_a=(self.__b**2 + self.__c**2 - self.__a**2)/(2* self.__b * self.__c)
        cos_b=(self.__a**2 + self.__c**2 - self.__b**2)/(2* self.__a * self.__c)
        cos_c=(self.__b**2 + self.__a**2 - self.__c**2)/(2* self.__b * self.__a)

        cos_a, cos_b, cos_c = max(-1, min(1, cos_a)), max(-1, min(1, cos_b)), max(-1, min(1, cos_c))

        ugl_a=math.degrees(math.acos(cos_a))
        ugl_b=math.degrees(math.acos(cos_b))
        ugl_c=math.degrees(math.acos(cos_c))
        return ugl_a, ugl_b, ugl_c

try:
    a=float(input("Введите сторону a:"))
    b=float(input("Введите сторону b:"))
    c=float(input("Введите сторону c:"))
    t=Triangle(a,b,c)
    print(f"Треугольник со стронами {t.a}, {t.b}, {t.c}")
    print(f"Периметр: {t.perimetr:.2f}")
    print(f"Площадь: {t.area:.2f}")
    A,B,C=t.ugls()
    print(f"Углы: {A:.2f}°,{B:.2f}°,{C:.2f}°")

except ValueError as e:
    print(f"Ошибка: {e}")