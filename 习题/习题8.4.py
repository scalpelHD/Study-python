def make_shirt(scale='large',picture='I love you!'):
    """显示T桖的图案和大小"""
    print('We\'ll make a '+scale+' T-shirt'+' whith "'+picture.upper()+
          '" painted on it.')
#调用有默认值的函数
make_shirt()
make_shirt('small','I love China')
def describle_city(name='beijing',nation='China'):
    """描述一个国家的一个城市"""
    print(name.title()+' is in '+nation+'.')
describle_city('reykjavik','Iceland')
describle_city()
describle_city('chengdu')
