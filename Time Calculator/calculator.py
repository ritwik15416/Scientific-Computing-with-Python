def add_time(start,dur,day=""):
    temp = 0
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    new = start.split(" ")
    unit = new[1]
    new_time = new[0].split(":")
    new_dur = dur.split(":")
    d_hr = new_dur[0]
    d_min = new_dur[1]
    s_hr = new_time[0]
    s_min = new_time[1]
    fin_min = int(d_min) + int(s_min)
    fin_hr = int(d_hr) + int(s_hr)
    def change(unit):
        if unit=="PM":
            unit = "AM"
        else:
            unit = "PM"
        return unit
    if fin_min >= 60:
        fin_min %= 60
        fin_hr += 1
    if fin_hr > 24:
        temp = fin_hr
        fin_hr %= 24
        if fin_hr > 12:
            fin_hr %= 12
    elif fin_hr > 12:
        temp = fin_hr
        fin_hr %= 12
    else:
        temp = fin_hr
    
    if temp > 24:
        rem = temp % 24
        if rem >= 12:
            unit = change(unit)
        else:
            pass
    elif temp >= 12 and temp < 24:
        unit = change(unit)
    else:
        pass
    
    day = day.title()
    def check(init,days):
        if init <= 6:
            day = days[init]
        else:
            r = init % 7
            day = days[r]
        return day

    if day != "":
        d = 0
        init = days.index(day)
        rem = int(d_hr) // 24
        r = int(d_hr) % 24
        if new[1] == "PM":
            mn = int(s_min) + int(d_min)
            if mn > 60:
                s_hr = int(s_hr) + 1
            else:
                pass
            diff = 12 - int(s_hr)
            if r >= diff:
                init += (rem+1)
                d += (rem+1)
            else:
                init += rem
                d += rem
        else:
            diff = 24 - int(s_hr)
            if r < diff:
                init += rem
                d += rem
            else:
                init += (rem+1)
                d += (rem+1)
        desc = "(" +str(d) + " days later)."
        day = check(init,days)
    else:
        desc = ""
        pass
    if len(str(fin_min)) < 2:
        fin_min = "0" + str(fin_min)
    else:
        pass
    print(str(fin_hr)+" :",fin_min,unit,day,desc)
    
