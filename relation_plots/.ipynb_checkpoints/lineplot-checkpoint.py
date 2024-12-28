import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np 

exercise = sns.load_dataset('exercise')
exercise = exercise.drop('Unnamed: 0', axis=1)

print(exercise.info())
print(exercise.head())
print('''
    'id' - уникальный идентификатор участника тестирования;
    'diet' - диета, которую придерживался участник (no fat - полное исключение жиров, low fat - низкожировая диета);
    'pulse' - средний пульс участника после выполнения упражнения;
    'time' - время, проведенное на упражнениях (в минутах);
    'kind' - тип упражнения (running (бег), walking (ходьба), rest (отдых)).
''')
    # 'id' - уникальный идентификатор участника тестирования;
    # 'diet' - диета, которую придерживался участник (no fat - полное исключение жиров, low fat - низкожировая диета);
    # 'pulse' - средний пульс участника после выполнения упражнения;
    # 'time' - время, проведенное на упражнениях (в минутах);
    # 'kind' - тип упражнения (running (бег), walking (ходьба), rest (отдых)).
print('# -----------------------------')

sns.lineplot(exercise, 
             x = 'time', 
             y = 'pulse',
             errorbar = None,                # Отключает доверительный интервал 
             marker = 's',                  # точки перегиба
             ms = 20,                       # размер точек
             markerfacecolor = 'red',        # цвет точек
             lw = 5,                        # толщина линии
             color = 'c',
             alpha = 0.8,
             hue='kind',                     # деление на группы по цвету
             hue_order=['rest',              # порядок цветов
                    'running', 'walking'] 
             )

plt.grid(linestyle = '--', alpha = 0.5)
plt.title('Деление на группы\n по цвету', fontsize = 20, pad=15, fontweight='bold')
plt.show()


# ---- Деление по размеру  линии ----------
sns.lineplot(exercise, 
             x = 'time', 
             y = 'pulse',
             errorbar = None,                # Отключает доверительный интервал 
             size = 'kind',                 # Группировка по размеру
             size_order = ['running',       # Порядок толщины
             'walking', 'rest'],
             sizes = [3, 3, 9]                 # кортеж для интервала размера линий и список для того, 
                                            # чтоб точно назначить размер каждой линии
             )

plt.grid(linestyle = '--', alpha = 0.5)
plt.title('Деление на группы\n по размеру линии', fontsize = 20, pad=15, fontweight='bold')
plt.show()


# estimator, выбор функции, учавствующей в группировке (по умолчанию mean)
sns.lineplot(exercise, 
             x = 'time', 
             y = 'pulse',
             errorbar = None,                # Отключает доверительный интервал 
             hue = 'kind',
             marker = 'o', 
             estimator = np.sum,            # mean, sum, median, np.sum etc.
             lw = 4,
             ms = 15

             )

plt.grid(linestyle = '--', alpha = 0.5)
plt.title('выбор функции, \nучавствующей в группировке', fontsize = 20, pad=15, fontweight='bold')
plt.show()

# параметр errorbar (по умолчанию 95)
sns.lineplot(x='time', 
            y='pulse', 
            data=exercise,
            hue='diet',
            errorbar=('ci', 60),             # доверительный интервал, 
                                            # кортеж из названия (confidence interval) и процента (по дефолту 95)
            n_boot=100,                     # количество выборок для бутстрапа
            seed = 43,                       # для воспроизводимости результатов бутстрапа
            palette='hot'
            )

plt.title('выбор функции, \nучавствующей в группировке', fontsize = 20, pad=15, fontweight='bold')
plt.grid(linestyle='--', alpha=0.5)
plt.show()