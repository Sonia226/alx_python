def common_elements(a, b):
    set_1 = set (a) 
    set_2 = set (b)
    c_set = set_1 & set_2
    empty_list = []
    
    if (c_set):
        return(list(c_set))
    else:
        return(empty_list)