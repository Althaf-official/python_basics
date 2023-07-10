def check_scope():
    def do_local_test():
        #this test is local variable .available only inside this function
        test="local test"

    def do_non_local_test():

        nonlocal test

        """
        The nonlocal keyword is used to work with variables inside nested functions, 
        where the variable should not belong to the inner function. 
        Use the keyword nonlocal to declare that the variable is not local.
        """
        test="non local test"




    def do_global_test():
        global test
        """
            #Difference between global and nonlocal variable
            Global is used to access and modify global variables from within a function, 
            while nonlocal is used to access and modify variables from the nearest enclosing scope that is not global.
            """
        test="global test"


#this test is global variable
    test="Default"


    do_local_test()
    print("test value calling after do local test   :" + test)

    #calling nonlocal
    do_non_local_test()
    print("test value calling after do non local test   :" + test)

    do_global_test()
    print("test value calling after do global test   :" + test)


check_scope()
print("test value after main "+test)

