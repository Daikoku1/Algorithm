
def mb_1_5(small, big, goal):
    if goal % 5 == 0:
        if int(small/5) + big >= int(goal/5):
            return True
        else:
            return False
    else:
        a = goal % 5
        if small < a:
            return False
        elif int((small - a)/5) + big >= int((goal - a)/5):
            return True
        else:
            return False
    
def mb_3_5(small, big, goal):
    if goal % 5 == 0:
        if 15 * (int(small)/5) + 5 * big >= goal:
            return True
        else:
            return False
    
    if goal % 5 == 1:
        # 3 * 2 = 6
        if small < 2 or goal < 6:
            return False
        elif 15 *(int( (small-2) / 5 ) ) + 5* big >= goal -6:
            return True
        else:
            return False
                  
    if goal % 5 == 2:
          # 3 * 4 = 12
        if small < 4 or goal < 12:
              return False
        elif 15 * (int( (small-4) / 5)) + 5 * big >= goal -12:
            return True
        else:
            return False
    
    if goal % 5 == 3:
          # 3 * 1 = 3
        if small < 1 or goal < 3:
              return False
        elif 15 * (int( (small-1) / 5)) + 5 * big >= goal - 3:
            return True
        else:
            return False
    
    if goal % 5 == 4:
          # 3 * 3 = 9
        if small < 3 or goal < 9:
              return False
        elif 15 * (int( (small-3) / 5)) + 5 * big >= goal -9:
            return True
        else:
            return False
