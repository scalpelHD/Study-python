magicians=['penny','eric','edward']
def show_magician(magicians):
    """打印列表中每个魔术师的名字"""
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    """修改魔术师的名字"""
    for i in range(0,len(magicians)):
        magicians[i]='the Great '+magicians[i].title()
        i+=1
    return magicians

show_magician(magicians)
new_magicians=make_great(magicians[:])
show_magician(magicians)
show_magician(new_magicians)
