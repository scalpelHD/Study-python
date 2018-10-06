#创建三明治列表
sandwich_orders=['potato sandwich','tomato sandwich','chicken sandwich',
                 'pastrami sandwich','potato sandwich','pastrami sandwich',
                 'pastrami sandwich','potato sandwich']
#创建空列表
finished_sandwiches=[]
print('Sorry!All our pastrami have been saled out!')
#剔除pastrami sandwich
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
#检查是否已经剔除pastrami sandwich
print(sandwich_orders)
#制作三明治并将订单中的三明治移到已完成列表中
while sandwich_orders:
    mading=sandwich_orders.pop(0)
    print('I am mading your '+mading+'.')
    finished_sandwiches.append(mading)
#检查列表
print(sandwich_orders)
print(finished_sandwiches)


#度假问题
#创建字典
peo_place={}
while True:
    name=input('What is your name ?')
    if name=='no':
        break
    place=input('Where do you want to go ?')
    peo_place[name]=place
print(peo_place)
