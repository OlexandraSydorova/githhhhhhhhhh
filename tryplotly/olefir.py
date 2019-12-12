import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.01, 0.01)
fig, ax = plt.subplots()
ax.axhline(y=0, color='black')
ax.axvline(x=0, color='black')
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.axis([-10, 10, -10, 10])

plt.title("Розв'язання системи двох рівнянь")

print("Інструкція щодо введення рівнянь\n * - множення\n \ - ділення\n ** - зведення в степінь\n")
print("Тригонометричні або логарифмічні рівняння вводіть у форматі:\n np.sin(x)\n np.cos(x)\n np.tan(x)\n np.log(base, x)\n")

choice = ''
while choice != '+':
    try:
        plt.plot(x, eval(input("Введіть перше рівняння: y1 = ")), color="blue", label="Графік першого рівняння")
        plt.plot(x, eval(input("Введіть друге рівняння: y2 = ")), color="green", label="Графік другого рівняння")
    except:
        print("Введено некоректні дані")
        continue

    plt.legend()
    plt.grid(True)
    plt.show()

    choice = input("Бажаєте завершити? Натисніть +. Для продовження натисніть будь-яку іншу клавішу: ")
    if choice != "+":
        print('\n', 'Наступна спроба: ', '\n')