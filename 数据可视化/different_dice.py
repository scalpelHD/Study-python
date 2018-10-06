from die import Die

import pygal

#创建一个D6和D10
die_1=Die()
die_2=Die(10)

#掷骰子多次，并将结果储存在一个列表中
results=[]
for roll_num in range(50000):
    result=die_1.roll()+die_2.roll()
    results.append(result)

#分析结果
frequencies=[]
for value in range(3,die_1.num_sides+die_2.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)

#可视化结果
hist=pygal.Bar()
hist.title="Results of rolling three D6 50000 times"
hist.x_labels=[value for value in range(2,17)]
hist.y_title='Frequency of result'
hist.x_title='Result'

hist.add('D6+D10',frequencies)
hist.render_to_file('dice_visual2.svg')