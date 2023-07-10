def check_scope():
    def do_local_test():
        #this test is local variable .available only inside this function
        test="local test"
    def do_non_local_test():
        test="non local test"
    def do_global_test():
        test="global test"


#this test is global variable
    test="Default"
    do_local_test()
    print("test value is   :" + test)

check_scope()

