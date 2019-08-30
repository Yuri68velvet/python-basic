#functions with some default and some with user defined values
def subjects(name='python',course1='Django',time=3):
    print(f'if you take {name} and {course1} u need {time} months to finish')

subjects()

subjects('php','laravel',2)

subjects('javascript','React',4)

subjects('law','England')

subjects(4)



