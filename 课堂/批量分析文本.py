from 分析文本 import count_words

filenames=['D:\python文件\little_women.txt',
           'D:\python文件\siddhartha.txt',
           'D:\python文件\moby_dick.txt']

for filename in filenames:
    count_words(filename)
