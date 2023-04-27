h=int(input('Enter Height of wall '))
w=int(input('Enter Width of wall '))
coverage=5
def paintCalculator(h,w,coverage):
    print(f'This wall can consume {(h*w)/coverage} cans of Paint')
paintCalculator(h,w,coverage)