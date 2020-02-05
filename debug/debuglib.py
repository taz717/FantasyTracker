'''
debug lib for FantasyTracker
'''

def debug_function(func, args_list):
    print(f'\n\n[DEBUG] Function -> {func}\n')
    for i in range(len(args_list)):
        print(f'{type(args_list[i])} -> Value: {args_list[i]}')
def debug_object(obj):
    for i in range(len(obj.__dict__)):
        print(f'{type(obj.__dict__[i])} -> Value: {obj.__dict__[i]}')