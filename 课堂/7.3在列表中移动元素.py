#创建一个待验证用户列表和一个用于储存已验证用户的空列表
unconfirmed_users=['alice','brain','brown']
confirmed_users=[]
#验证每个用户，直到没有未验证用户为止，将每个已验证的用户移到已验证用户列表中
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print('Verifying user:'+current_user.title())
    confirmed_users.append(current_user)
#显示所有已验证的用户
print('\nThe following users have been confirmed:')
for user in confirmed_users:
    print(user.title())
#检查未验证用户是否已经全部被移到已验证用户列表中
print(unconfirmed_users)
print(confirmed_users)
