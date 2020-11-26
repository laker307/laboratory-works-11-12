import numpy as np
import matplotlib.pyplot as plt

class DoSoChKa:

    def __init__(self, k, l, m, n):
        self.k = k
        self.l = l
        self.m = m
        self.n = n
        self.el = ''
        self.q = ''

    def okk(self):      # Проверка на ошибки ввода
        l = [1, 2, 3, 4, 5, 6, 7, 8]
        if (self.k not in l) or (self.m not in l) or (self.l not in l) or (self.n not in l):
            print('\n\nПроизошла ошибка ввода, введите k, l, m, n корректно!\n')
            return False
        else:
            return True

    def sozdanie(self):     # создаём доску
        fig = plt.figure()
        m = 1
        g = 0
        s = 0
        for j in range(1, 9):
            if j % 2 == 0:
                for i in range(1, 9):
                    sqr = fig.add_subplot(8, 8, m) # добавление полей
                    if i % 2 == 0:
                        sqr.set(xticks=[], yticks=[]) # цвет полей
                    else:
                        sqr.set(xticks=[], yticks=[], facecolor = 'black') # цвет полей
                    if g == 0:
                        if j == 9-self.l and i == self.k:
                            sqr.set(xticks=[], yticks=[], facecolor='red') # цвет полей
                            g = 1
                    if s == 0:
                        if j == 9-self.n and i == self.m:
                            sqr.set(xticks=[], yticks=[], facecolor='blue') # цвет полей
                            s = 1
                    m += 1
            else:
                for i in range(1, 9):
                    sqr = fig.add_subplot(8, 8, m)  # добавление полей
                    if i % 2 == 0:
                        sqr.set(xticks=[], yticks=[], facecolor='black')  # цвет полей
                    else:
                        sqr.set(xticks=[], yticks=[])
                    if g == 0:
                        if j == 9-self.l and i == self.k:
                            sqr.set(xticks=[], yticks=[], facecolor='red')   # цвет полей
                            g = 1
                    if s == 0:
                        if j == 9-self.n and i == self.m:
                            sqr.set(xticks=[], yticks=[], facecolor='blue')   # цвет полей
                            s = 1
                    m += 1

        print('\nДоска имеет вид (красное поле - k, l; синее поле - m, n): \nЗакройте окно с доской для продолжения работы!\n')
        plt.show()


    def one_colour(self):  # Определение соответствия цвета полей
        if (self.k + self.l) % 2 == (self.n + self.m) % 2:
            print('a) Эти поля одного цвета!')
        else:
            print('a) Эти поля разного цвета!')
            self.el = 'n'

    def queen(self):  # Угрожает ли ферзь
        es = [0, 1, 3, 5, 7, 9, 11, 13, 15]
        if (self.k == self.m) or (self.l == self.n) or (abs(self.k - self.m) == abs(self.l - self.n)):
            print('\nб) Ферзь (красное поле) угрожает выбранному полю (синее поле)')
        else:
            print('\nб) Ферзь (красное поле) не угрожает выбранному полю (синее поле)')
            self.q = 'n'

    def mustang(self):  # Угрожает ли конь
        if ((abs(self.k - self.m) == 2) and (abs(self.l - self.n) == 1)) or ((abs(self.k - self.m) == 1) and (abs(self.l - self.n) == 2)):
            print('\nв) Конь (красное поле) угрожает выбранному полю (синее поле)')
        else:
            print('\nв) Конь (красное поле) не угрожает выбранному полю (синее поле)')

    def rook(self):  # Определение ходов для ладьи
        if (self.k == self.m) or (self.l == self.n):
            print('\nг) Ладья (красное поле) может попасть в это поле (синее поле) за один ход ')
        else:
            print('\nг) Ладья (красное поле) не может за один ход добраться до выбранного поля (синее поле)\nНо можно добраться через поле ',(self.k,self.n),' или ',(self.m,self.l))


    def queen_move(self):  # Определение ходов для ферзя
        if self.q == '':
            print('\nд) Ферзь (красное поле) может попасть в это поле (синее поле) за один ход ')
        else:
            print('\nд) Ферзь (красное поле) не может за один ход добраться до выбранного поля (синее поле)\nНо можно добраться через поля: ',(self.k,self.n), (self.m,self.l))

    def elephant(self):  # Определение ходов для слона
        if self.el == '':
            if abs(self.k - self.m) == abs(self.l - self.n):
                print('\nе) Слон (красное поле) может попасть в это поле (синее поле) за один ход ')
            else:
                vert = (self.k + self.l + self.m - self.n ) // 2
                gor =(self.k + self.l - self.m + self.n ) // 2
                if vert < 1 or vert > 8 or gor < 1 or gor > 8 :
                    vert = (self.m + self.k + self.n - 1) // 2
                    gor = (self.m - self.k + self.n + 1) // 2
                print('\nе) Слон (красное поле) не может за один ход добраться до выбранного поля (синее поле)\nНо можно добраться через поле: ',
                          vert, gor)

        else:
            print('\nе) Слон (красное поле) не может попасть в это поле (синее поле). Они разного цвета! ')



if __name__ == '__main__':
    while True: # бесконечный цикл
        print('Введите k, l, m, n в пределах от 1 до 8')
        dosoc = DoSoChKa(int(input()),int(input()),int(input()),int(input()))# вводим и передаём данные в класс
        if dosoc.okk() == True: # обработка ошибок
            dosoc.one_colour() # проверка цветов
            dosoc.queen() # проверка для ферзя
            dosoc.mustang() # проверка для коня
            dosoc.rook() # проверка с ладьёй x2
            dosoc.queen_move() # проверка ферзя х2
            dosoc.elephant()  # проверка для слона
            dosoc.sozdanie()  # выводится доска