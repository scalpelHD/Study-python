import random
secret=random.randint(1,6)
print("猜一猜我现在正在想什么数字。")
k=0
while 1:
    guess=int(input())
    if guess==secret:
        print("哎呀，心心相印，心有灵犀啊,恭喜你猜对了。就是"+str(secret)+'。\n游戏结束，不玩了。')
        break
    if k==2:
        print("三次都没猜中，看来我们没有缘分，我想的是"+str(secret)+"。\n游戏结束，不玩了。")
        break
    else:
        if guess<secret:
            print("哥，小了，小了。请重新输入：")
        else:
            print("哥，大了，大了。请重新输入：")
    k=k+1

