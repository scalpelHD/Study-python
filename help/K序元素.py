nums = eval(input('请输入数组：'))
k = eval(input('请输入K的值'))
nums.sort(reverse=True)
print(nums[k-1])
