date=input()
year=date[0:4]
month=date[4:6]
day=date[6:]
if int(year)%400==0 or int(year)%4==0 and int(year)%100!=0:
    runnian=1
else:
    runnian=0
daysdic={'01':31,'02':28+runnian,'03':'31','04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}
if int(day)>daysdic.get(month,0) or int(month)>13 or int(month)<1 or int(day)<1 or int(day)>31:
    print("输入的日期不存在")
else:
    print("{}年{}月一共有{}天".format(year,month,daysdic[month]))
