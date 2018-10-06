players=['charles','martina','michaael','florance','eli']
print(players[0:3])#前三个
print(players[1:4])#第二到第四个
print(players[:4])#前四个
print(players[2:])#第三到最后
print(players[-3:])#倒数第三到最后
for player in players[:3]:#输出前三个人名
    print(player.title())
team=players[:]#复制列表
print(team,players)
team.append('tom')#通过添加元素确认已经创建两个列表
players.append('sam')
print(team,players)
team2=players#复制列表错误示范
team2.append('sony')#通过添加元素证明未成功创建两个列表
players.append('vivian')
print(team2,players)
