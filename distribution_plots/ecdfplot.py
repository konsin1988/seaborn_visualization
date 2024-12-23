import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np

    # data: массив данных или датафрейм, содержащий данные для построения ECDF;
    # x: имя столбца или массив значений для оси X;
    # y: (нечасто используется) имя столбца или массив значений для оси Y. В ECDF чаще используется параметр x;
    # hue: имя столбца или массив, задающий подгруппы данных для отображения на графике разными цветами;
    # weights: массив весов для взвешенного ECDF;
    # stat: тип статистики для отображения на оси Y ('proportion' (по умолчанию), 'count', 'percent')';
    # complementary: логическое значение, указывающее, строить ли дополнительную ECDF (1 - ECDF). По умолчанию False;
    # palette: палитра цветов для подгрупп, заданных параметром hue;
    # hue_order: определяет порядок категорий в подгруппах;
    # log_scale: логическое значение или пара значений, указывающих, применять ли логарифмическое масштабирование к осям. Например, log_scale=True для логарифмической шкалы на обеих осях или log_scale=(False, True) для логарифмической шкалы только на оси Y.

tips = sns.load_dataset('tips')

print(tips.head())

# total_bill: общая сумма счета;
# tip: сумма чаевых;
# sex: пол посетителя;
# smoker: курящий или нет;
# day: день недели;
# time: время посещения ресторана (обед или ужин);
# size: количество людей за столиком.

sns.set_style('whitegrid')

sns.ecdfplot(tips, 
             x = 'tip',
             hue = 'day',
             stat='count'            
             
             )

plt.axhline(0.9, c = 'r', ls = '--')
# plt.yticks(list(plt.yticks()[0]) + [0.9])
plt.yticks([x/10 for x in range(0, 11, 2)] + [0.9])
plt.xticks([x/2 for x in range(0, 22, 1)])


plt.show()

