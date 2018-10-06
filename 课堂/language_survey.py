from survey import Survey

#定义一个问题，并创建一个表示调查的AnonymousSurvey的对象
question='What language did you first learn to speak?'
my_survey=Survey(question)

#显示问题并储存答案
my_survey.show()
print('Enter \'q\' at any time to quit.\n')
while True:
    response=input('language:')
    if response=='q':
        break
    my_survey.store_response(response)

#显示调查结果
print('\nThank you to everyone who participated in the survey!')
my_survey.show_result()
