import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt 

# Графики отношений (relational plots) - sns.scatterplot() & sns.lineplot()
# - универсальная функция sns.relplot(), которая позволяет 
# создавать как диаграммы рассеяния, так и линейные графики.

    # data: DataFrame или массив с данными;
    # x: название столбца или вектор данных для оси X;
    # y: название столбца или вектор данных для оси Y;
    # hue: название столбца или вектор данных для группировки точек по цвету;
    # size: название столбца или вектор данных для изменения размера точек;
    # style: название столбца или вектор данных для изменения стиля точек (например, разные формы);
    # palette: цветовая палитра для переменной hue;
    # hue_order: задаёт порядок отображения категорий для переменной hue;
    # hue_norm: позволяет нормализовать данные переменной hue;
    # sizes: диапазон размеров для переменной size;
    # size_order: задаёт порядок отображения категорий для переменной size;
    # size_norm: позволяет нормализовать данные переменной size, задавая диапазон значений;
    # markers: список стилей маркеров для переменной style;
    # style_order: задаёт порядок отображения категорий для переменной style.

penguins = sns.load_dataset('penguins').dropna()

print(penguins.info())
print(penguins.head())
print('#----------------------------------------')
print(sns.color_palette('inferno').as_hex())


# -------- hue species with hue_order группировка по цвету точек (номинативная переменная)
sns.set_style('darkgrid')
sns.scatterplot(penguins, 
                x = 'bill_length_mm', 
                y = 'bill_depth_mm', 
                color = 'red',
                alpha = 0.7,
                s = 150,                            # за размер отвечает именно s, не size
                marker = 'D',
                # hue = 'body_mass_g',                # не только номинативная переменная, но и количественная
                # hue_norm=(2700, 4000),               # для цветового акцента на определенной группе 
                hue = 'species',                    
                hue_order=['Gentoo', 'Chinstrap',   # порядок отображения в легенде и соответсвенно порядок цвета 
                           'Adelie']
                )        

plt.show()
# Вот некоторые из доступных кодов маркеров:

#     'o': круг;
#     's': квадрат;
#     '^': треугольник вверх;
#     'v': треугольник вниз;
#     '>': треугольник вправо;
#     '<': треугольник влево;
#     'x': крестик;
#     '*': звёздочка;
#     'D': ромб;
#     'H': шестиугольник.

# hue body_mass_g with hue_norm группировка по цвету точек (количественная переменная)
sns.set_style('darkgrid')
sns.scatterplot(penguins, 
                x = 'bill_length_mm', 
                y = 'bill_depth_mm', 
                color = 'red',
                alpha = 0.7,
                s = 150,                            # за размер отвечает именно s, не size
                marker = 'D',
                hue = 'body_mass_g',                # не только номинативная переменная, но и количественная
                hue_norm=(2700, 4000)               # для цветового акцента на определенной группе           
                )    

plt.show()

# style species with markers группировка по форме точек (количественная переменная)
sns.set_style('darkgrid')
sns.scatterplot(penguins, 
                x = 'bill_length_mm', 
                y = 'bill_depth_mm', 
                color = 'red',
                alpha = 0.7,
                s = 200,                      # за размер отвечает именно s, не size
                style = 'species',            # разбиение точек по форме
                markers= ['<', '^', '>'],     # установка кастомных форм для style
                hue = 'body_mass_g',          # не только номинативная переменная, но и количественная
                hue_norm=(2700, 4000)         # для цветового акцента на определенной группе           
                )    

plt.show()

# ------ size with sizes группировка по размеру точек(количественная переменная)  -------------
sns.set_style('darkgrid')
sns.scatterplot(penguins, 
                x = 'bill_length_mm', 
                y = 'bill_depth_mm', 
                alpha = 0.7,
                size = 'body_mass_g',
                sizes = (30, 500),          # кортеж для количественной переменной (от -> до)
                hue = 'species',
                marker = 'D'
)    

plt.show()

# -------size with sizes группировка по размеру точек (номинативная переменная)
# из графика видно, что на острове Biscoe обитают два вида: основной - Gentoo, 
# и в меньшей  степени - Adelie. 
sns.set_style('darkgrid')
sns.scatterplot(penguins, 
                x = 'bill_length_mm', 
                y = 'bill_depth_mm', 
                alpha = 0.7,
                size = 'island',
                sizes = [20, 300, 20],      # список для номинативной переменной ( размер для каждой категории) 
                # hue = 'species',
                marker = 's',
                hue = 'species',
                palette='inferno'   # цветовые гаммы, print(sns.palettes.SEABORN_PALETTES.keys()),
                                    # print(plt.colormaps())
)    

plt.show()
