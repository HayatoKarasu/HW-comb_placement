from matplotlib import pyplot as plt

plt.text(0.01, 0.9, '1) Дан пароль из 3 символов из 5 ', fontsize=15)
plt.text(0.01, 0.8, 'возможных цифр от 1 до 5 включительно.', fontsize=15)
plt.text(0.01, 0.7, 'Сколько времени надо хакеру если на', fontsize=15)
plt.text(0.01, 0.6, 'одну операцию уходит 5 сек.', fontsize=15)
form = r"$(1 2 3 4 5)$"
plt.text(0.01, 0.5, form, fontsize=15)
form = r"$A_3^5 = \frac{5!}{(5-3)!} = \frac{5*4*3*2!}{2!} = 60$"
plt.text(0.01, 0.4, form, fontsize=15)
plt.text(0.01, 0.3, '60 операций подбора нужно сделать', fontsize=15)
form = r"$60(опер)*5(сек)=300(сек)/60(сек/мин)= 5$"
plt.text(0.01, 0.2, form, fontsize=15)
plt.text(0.01, 0.1, '5 минут потребуется хакеру в худшем случае.', fontsize=14)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

plt.text(0.01, 0.9, '2) Если числа в пароле могут повторяться:', fontsize=15)
form = r"$Ā_3^5 = 5^3 = 125$"
plt.text(0.01, 0.8, form, fontsize=15)
plt.text(0.01, 0.7, '125 возможных операций подбора.', fontsize=15)
form = r"$125(оп)*5(сек)=625(сек)/60(сек/мин) \approx 10$"
plt.text(0.01, 0.6, form, fontsize=15)
plt.text(0.01, 0.5, 'примерно 10 минут потребуется хакеру.', fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

plt.text(0.01, 0.9, '3) Телефонный справочник с 6 значными номерами', fontsize=13)
plt.text(0.01, 0.8, 'Сколько может быть комбинаций?', fontsize=15)
form = r"$(0123456789)$"
plt.text(0.01, 0.7, form, fontsize=15)
plt.text(0.01, 0.6, 'Если цифры без повтора:', fontsize=15)
form = r"$A_6^{10} = \frac{10!}{(10-6)!} = \frac{10*9*8*7*6*5*4!}{4!} = 151200$"
plt.text(0.01, 0.5, form, fontsize=15)
plt.text(0.01, 0.4, 'Если цифры могут повторяться:', fontsize=15)
form = r"$Ā_6^{10} = 10^6 = 1000000$"
plt.text(0.01, 0.3, form, fontsize=15)
plt.text(0.01, 0.2, 'Сколько номеров с 4-я одинаковыми цифрами вконце:', fontsize=12)
form = r"$Ā_3^{10} = 10^3 = 1000$"
plt.text(0.01, 0.1, form, fontsize=15)
plt.text(0.01, 0.01, 'Для этого 4 цифры использовали как одну=6-4=2+1=3', fontsize=12)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()