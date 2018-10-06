from die import Die
import pygal

#创建一个D6
die_1=Die()
die_2=Die()

#掷几次骰子，并将结果储存在一个列表中
results=[]
for roll_num in range(1000):
    result=die_1.roll()+die_2.roll()
    results.append(result)

#分析结果
frequencies=[]
for value in range(2,die_1.num_sides+die_2.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)

#分析结果可视化
hist=pygal.Bar()

hist.title="Results of rolling one D6 1000 times"
hist.x_labels=[value for value in range(2,13)]
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add('D6+D6',frequencies)
hist.render_to_file("dice_visual.svg")
