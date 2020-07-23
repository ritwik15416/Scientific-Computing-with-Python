def solve(problems,choice=False):           
    if len(problems) > 5:                
        print("Error, Too many problems.")
    else:
        first = []
        dash = []
        second = []
        result = []
        exit = False
        def printer():
            print(s_first)
            print(s_second)
            print(s_dash)
        for x in problems:
            new = x.split(" ")
            if new[0].isdigit() == False or new[2].isdigit() == False:   
                print("Error: Numbers must only contain digits.")
                exit = True
                break
            if len(new[0]) > 4 or len(new[2]) > 4:            
                print("Error: Numbers cannot be more than four digits.")
                exit = True
                break
            if (("+" not in new) and ("-" not in new)):           
                print("Error: Operator must be '+' or '-'.")
                exit = True
                break
                
            else:
                result.append(eval(x))   
                first.append(new[0])
                second.append(new[1] + new[2])
                dash.append("-----")
        if(exit == False):           
            result = map(str,result)
            s_first = ("\t").join(first)           
            s_second = ("\t").join(second)
            s_dash = ("\t").join(dash)
            s_result = ("\t").join(result)
        
            if choice == True:
                printer()
                print(s_result)
            else:
                printer()






