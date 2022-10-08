def fibonacci(n):
    """ Takes in a number n, returns the nth value in the fibonacci series """
    if type(n)!=int:
       """ for the string value """
       return "please enter only numbers"
    if n<0 :
        """ for the negative value """
        return "please enter a positive value"
    else:
        if n==0 or n==1:
            """ base value to stop the recursion """
            return n
        else:
            """ using recursion """
            return fibonacci(n-1)+fibonacci(n-2)

def lucas(n):
    """Takes in a number n, returns the nth value in the lucas series"""
    if type(n)!=int:
        """for the string value"""
        return "please enter only numbers"
    if n<0 :
        """ for the negative value """
        return "please enter a positive value"
    else:
        if n==0 :
            """base value to stop the recursion """
            return 2
        elif n==1:
            """base value to stop the recursion"""
            return 1
        else:
            """using recursion """
            return lucas(n-1)+lucas(n-2)


def sum_series(n, x=0 , y=1):
    """ Takes in a number n, returns the nth value in the series and the base is x,y"""
    if type(n)!=int :
        """for the string value"""
        return "please enter only numbers"
    if n<0 :
        """ for the negative value """
        return "please enter a positive value"
    else:
        if n==0 :
            """base value to stop the recursion """
            return x
        elif n==1:
            """base value to stop the recursion"""
            return y
        else:
            """using recursion """
            return sum_series(n-1,x,y)+sum_series(n-2,x,y)
