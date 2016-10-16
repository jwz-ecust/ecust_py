def decorato_maker_with_arguments(decorator_arg1,decoratro_arg2):
    print "I make decorators! And I accept arguments:", decorator_arg1, decoratro_arg2

    def my_decorator(func):
        print "I am the decorator. Somehow you passed me argumentss:",decorator_arg1,decoratro_arg2

        def wrapped(function_arg1,function_arg2):
            print "{0} {1} {2} {3}".format(decorator_arg1, decoratro_arg2,function_arg1, function_arg2)
            return func(function_arg1,function_arg2)
        return wrapped
    return my_decorator


@decorato_maker_with_arguments("zhangjiawei","chenbeibei")
def decorated_function_with_arguments(function_arg1,function_arg2):
    print "my arguments: {0} {1}".format(function_arg1, function_arg2)

decorated_function_with_arguments("Yichen","Fisher")