def func(nums, aim):
    for x in range(len(nums)):
        for y in range(x+1, len(nums)):
            if nums[x] + nums[y] == aim:
                return [x, y]
    return False


num = eval(input('请输入列表：'))
target = eval(input('请输入目标数：'))
print(func(num, target))

