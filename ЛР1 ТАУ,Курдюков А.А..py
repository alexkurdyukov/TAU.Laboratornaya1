#вводим дополнительные библиотеки
import matplotlib
import matplotlib.pyplot as pyplot
import control.matlab as matlab
import numpy as numpy
import math
import colorama as color
#выбор звена(апериодическое, безынерционное - пользователь сам решит какое звено ему нужно)
def choice():
    inertialessUnitName = 'Безынерционное звено'
    aperiodicUnitName = 'Апериодическое звено'
    integratingUnitName = 'Интегрирующее звено'
    ideallyDiffferentiatingUnitName = 'Идеально дифференцирующее звено'
    reallyDiffferentiatingUnitName = 'Реально дифференцирующее звено'

    needNewChoice = True
    while needNewChoice:
        print(color.Style.RESET_ALL)
        userInput = input('Введите номер команды:\n'
                      '1 - ' + inertialessUnitName + ';\n'
                      '2 - ' + aperiodicUnitName + ';\n'
                      '3 - ' + integratingUnitName + ';\n'
                      '4 - ' + ideallyDiffferentiatingUnitName + ';\n'
                      '5 - ' + reallyDiffferentiatingUnitName + ';\n')

        if userInput.isdigit():
            needNewChoice = False
            userInput = int(userInput)
            if userInput == 1:
                name = 'Безынерционное звено'
            elif userInput == 2:
                name = 'Апериодическое звено'
            elif userInput == 3:
                name = 'Интегрирующее звено'
            elif userInput == 4:
                name = 'Идеально дифференцирующее звено'
            elif userInput == 5:
                name = 'Реально дифференцирующее звено'
        else:
            print(color.Fore.RED +'Пожалуйста, введите целочисленное значение!\n')
            needNewChoice = True
    return name
def getUnit(name):
    needNewChoice = True
    while needNewChoice:
        k = input('Пожалуйста, введите коэффициент k \n')
        t = input('Пожалуйста, введите коэффициент t \n')
        if k.isdigit() and t.isdigit():
            k = int(k)
            t = int(t)
            if name == 'Безынерционное звено':
                unit = matlab.tf([k],[1])
            elif name == 'Апериодическое звено':
                unit = matlab.tf([k],[t,1])
            elif name == 'Интегрирующее звено':
                unit = matlab.tf([k],[1,0])
            elif name == 'Идеально дифференцирующее звено':
                unit = matlab.tf([k,0],[0.0000000000000000000000000000001,1])
            elif name == 'Реально дифференцирующее звено':
                unit = matlab.tf([k,0],[t,1])
            needNewChoice = False
        else:
            print(color.Fore.RED+ '\n Пожалуйста введите цифровое значение ')
            needNewChoice = True
    return unit

def graph(num,title,y,x):
    pyplot.subplot(2,1,num)
    pyplot.grid(True)
    if title =='Переходная характеристика':
        pyplot.plot(x,y,'purple')
    elif title == 'Импульсная характеристика':
        pyplot.plot(x,y,'green')
    pyplot.title(title)
    pyplot.ylabel('Амплитуда')
    pyplot.xlabel('Время, с ')

unitName = choice() # вводим переменную и кладем в нее значение функции выбора  - результат работы программы choice - название звена
unit = getUnit(unitName) # в юнит кладем

timeLine = []
for i in range(0, 10000):
    timeLine.append(i/1000)
[y,x] = matlab.step(unit, timeLine)
graph(1, 'Переходная характеристика', y, x)
[y,x] = matlab.impulse(unit, timeLine)
graph(2,'Импульсная характеристика',y, x)
pyplot.show()
#теперь построим частотные характеристики используя фрикресп


#задаем х, в диапазоне которого будет находиться амплитуда и фаза
secondtimeLine = []
for i in range(0, 1000):
    secondtimeLine.append(i/100)
mag, phase, omega = matlab.freqresp(unit, secondtimeLine)

#построим график АЧХ
pyplot.subplot()
pyplot.grid(True)
pyplot.ylabel('Амплитуда')
pyplot.xlabel('Частота, рад/сек')
pyplot.plot(mag)
pyplot.title('Амплитудно-частотная характеристика')
#построим график ФЧХ
pyplot.subplot()
pyplot.show()
pyplot.grid(True)
pyplot.ylabel('Фаза,градусы') # Название оси y - фаза
pyplot.xlabel('Частота, рад/сек') # название оси x - угловая частота
pyplot.plot(phase*180/math.pi)
pyplot.title('Фазо-частотная характеристика')
pyplot.show()




