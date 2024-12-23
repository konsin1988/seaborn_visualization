import matplotlib.pyplot as plt 
import seaborn as sns 

    # data: DataFrame или массив, содержащий данные для визуализации;
    # x, y: имена столбцов для построения графиков по осям X и Y;
    # hue: столбец для группировки данных по цвету;
    # col, row: столбцы для создания подграфиков;
    # kind: тип графика ('hist' для гистограммы, 'kde' для KDE-плотности, 'ecdf' для ECDF);
    # rug: добавляет штрих-диаграмму (по умолчанию - False);
    # bins: количество или границы бинов для гистограммы;
    # binwidth: ширина каждого бина;
    # palette: палитра цветов для группировки по hue;
    # kde: логическое значение для добавления KDE-плотности к гистограмме;
    # stat: статистика для оси Y ('count', 'density', 'probability', 'frequency', 'percent').

tips = sns.load_dataset('tips')
print(tips.head())
print(tips.info())

    # total_bill: общая сумма счета;
    # tip: сумма чаевых;
    # sex: пол посетителя;
    # smoker: курящий или нет;
    # day: день недели;
    # time: время посещения ресторана (обед или ужин);
    # size: количество людей за столиком.

sns.set_style('white')

# ------------- displot hist ---------------------
sns.displot(tips, 
            x = 'total_bill',
            kde = True,
            kind = 'hist',
            stat = 'probability',
            rug=True,
            rug_kws={'height': 0.05},
            facet_kws={'despine': False}            # правая и верхняя границы 
            )

plt.grid(linestyle = '--', alpha = 0.5)
plt.show()

# ------------ displot kde ---------------------
sns.displot(tips, 
            x = 'total_bill',
            kind = 'kde',
            fill = True,
            linewidth = 4,
            color = 'green',
            rug=True
            )

plt.grid(linestyle = '--', alpha = 0.5)
plt.show()

# --------- displot ECDF ------------------------
sns.displot(x='total_bill', data=tips,
            color='lightgreen',
            kind='ecdf')

plt.grid(linestyle='--', alpha=0.5)
plt.show()

# ----------- hue hist ----------------------
sns.displot(x='total_bill', 
            data=tips,
            hue='time',
            multiple = 'dodge',
            # kind = 'kde'
            )

plt.grid(linestyle='--', alpha=0.5)
plt.show() 

# ---------- hue kde ------------------
sns.displot(x='total_bill', 
            data=tips,
            hue='time',
            col = 'time',
            row = 'sex',
            kind = 'kde',
            cut = 0
            )

plt.grid(linestyle='--', alpha=0.5)
plt.show() 

# x - count variable ------------------------
sns.displot(x = 'total_bill', 
            y = 'sex', 
            data = tips)

plt.grid(linestyle='--', alpha=0.5)
plt.show()


sns.displot(x = 'total_bill', 
            y = 'size', 
            data = tips,
            cbar = True,
            facet_kws={'despine': False}
            )

plt.grid(linestyle='--', alpha=0.5)
plt.show()

# ------------------------ kde, x - count var ------
sns.displot(x='total_bill', y='size', data=tips, 
            kind='kde',
            rug=True)

plt.grid(linestyle='--', alpha=0.5)
plt.show()