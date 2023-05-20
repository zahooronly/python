# scopes in python
enemies = 'aliens'
def scope_test():
    enemies = 'pirates'
    print('enemies inside function: ', enemies)

scope_test()
print('enemies outside function: ', enemies)
