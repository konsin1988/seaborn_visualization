import matplotlib.pyplot as plt 
import seaborn as sns 


    # data: DataFrame, массив с данными;
    # x: имя переменной, которая будет отображена на оси X;
    # y: имя переменной, которая будет отображена на оси Y. Если задан, строится 2D KDE;
    # hue: имя переменной для группировки данных по категориям, каждая из которых будет представлена отдельной линией KDE;
    # weights: массив значений для взвешивания точек данных. Должен быть такой же длины, как и данные;
    # palette: палитра цветов для различения категорий, заданных параметром hue;
    # hue_order: список для определения порядка категорий, отображаемых при использовании hue;
    # hue_norm: два значения, определяющие нормализацию данных по оси hue;
    # color: цвет линий и заливки, если hue не используется;
    # fill: логическое значение, определяющее, следует ли заполнять область под KDE;
    # multiple: определяет как отображать несколько KDE: 'layer', 'stack' или 'fill' (по умолчанию 'layer');
    # common_norm: логическое значение, определяющее, нормализовать ли плотности по всем категориям hue вместе (True) или отдельно (False). По умолчанию common_norm=True;
    # common_grid: логическое значение, определяющее, использовать ли общую сетку для всех категорий hue. По умолчанию common_grid=False;
    # cumulative: логическое значение, определяющее, строить ли накопительную функцию распределения (по умолчанию cumulative=False);
    # bw_method: метод для вычисления ширины окна (bandwidth): 'scott' (по умолчанию), 'silverman' или числовое значение;
    # bw_adjust: множитель для ширины окна. Умножает значение, вычисленное bw_method, на этот коэффициент (по умолчанию bw_adjust=1);
    # log_scale: Логическое значение или кортеж из двух логических значений для использования логарифмической шкалы по осям X и/или Y;
    # levels: количество уровней контуров для 2D KDE (по умолчанию levels=10);
    # thresh: минимальное значение плотности для отображения контуров в 2D KDE (по умолчанию thresh=0.05);
    # gridsize: количество точек в сетке для оценки плотности (по умолчанию gridsize=200);
    # cut: количество стандартных отклонений для увеличения границ осей при построении KDE (по умолчанию cut=3). Указывает, насколько далеко за пределы данных следует отображать кривую KDE;
    # clip: пределы значений для обрезки KDE;
    # legend: логическое значение, определяющее, отображать ли легенду (по умолчанию legend=True);
    # cbar: логическое значение, определяющее, отображать ли цветовую шкалу (по умолчанию cbar=False).

penguins = sns.load_dataset('penguins')
print(penguins.head())
print(penguins.info())

    # 'species' - вид пингвина (Adelie, Chinstrap, Gentoo);
    # 'island' - остров, где были собраны данные (Biscoe, Dream, Torgersen);
    # 'bill_length_mm' - длина клюва в миллиметрах;
    # 'bill_depth_mm' - глубина клюва в миллиметрах;
    # 'flipper_length_mm' - длина ласт в миллиметрах;
    # 'body_mass_g' - масса тела в граммах;
    # 'sex' - пол пингвина (Male, Female).

sns.kdeplot(penguins, 
            x = 'body_mass_g', 
            fill = True,
            linewidth = 3,
            color='#BC8F8F',
            # clip = (2800, 5300)         # ограничение по оси Х
            cut = 2,                     # насколько болььшая интерполяция за пределы графика
            # log_scale=True              # график в логарифмическом масштабе
            # cumulative=True,             # кумулятивная сумма вероятностей
            # bw_method=2
            bw_adjust=1, 
            hue = 'species',
            # multiple='fill'           # multiple:
                                        #  'layer' (по умолчанию): Это стандартное поведение, где каждая группа отображается своим собственным графиком поверх других.
                                        #   'stack': Оценки плотности отображаются друг над другом, но складываются, чтобы показать совокупную плотность. Это похоже на стопку областей, где нижняя часть следующей оценки плотности начинается там, где заканчивается верхняя часть предыдущей.
                                        #   'fill': Оценки плотности заполняются по вертикали, чтобы суммарная плотность на каждом уровне была равна 1, что может быть востребовано для визуализации относительных пропорций каждой группы в совокупном распределении.
            
            )
plt.show()


# Two-dimentional kde
sns.kdeplot(data=penguins, 
            x='bill_length_mm', 
            y='bill_depth_mm',
            levels = 100,                # levels может принимать:

                                        #   Целое число: указывает количество уровней, которые будут равномерно распределены между минимальной и максимальной плотностью (по умолчанию levels=10).
                                        #   Список или массив значений: конкретные значения уровней плотности, которые будут использованы для построения контуров.
            fill = True,
            cbar = True,
            hue='species',
            thresh=0.01
            )
plt.show()
