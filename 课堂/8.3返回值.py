def get_formatted(first,last):
    """返回整洁的姓名"""
    full_name=first +' '+ last
    return full_name.title()

musician=get_formatted('jimi','hendrix')
print(musician)

def get_formatted_name(first,last,midlle=''):#指定默认值时应该放在参数末尾
    """返回整洁的姓名"""
    if midlle:
        full_name=first+' '+midlle+' '+last
    else:
        full_name=first+' '+last
    return full_name.title()

musician=get_formatted_name('john','hooker','lee')
print(musician)
musician=get_formatted_name('jimi','hendrix')
print(musician)
def build_person(first,last,age=''):#返回字典
    """返回一个字典，其中包含一个人的信息"""
    person={'first':first,'last':last}
    if age:
        person['age']=age
    return person
musician=build_person('jimi','hendrix')
print(musician)
musician=build_person('jimi','hendrix', 27)
print(musician)
