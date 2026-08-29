"""
This is a utility module 
"""

my_name = "Vinod KK"

def hello():
    """
    an example function to say hello 
    """
    print("hello, akash")

def hello(): 
    """
    an example function to say hello 
    """
    print("hello, yash")

    #function cannot have the same name in one scope
    #functions can have the same name in differernt scopes
    #the second hello replaces the first one -- it will give yash instead of akash