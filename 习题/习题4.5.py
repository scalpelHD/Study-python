foods=('potato','tomato','french fries','beef','pork')#元组
for food in foods:#遍历元组
    print("delicious"+food+'!')
foods=('potato','tomato','fish','noodles','pork')#重新给元组赋值
for food in foods:
    print("delicious"+food+'!')
foods[0]="ricea"#不能给元组中的元素赋值
