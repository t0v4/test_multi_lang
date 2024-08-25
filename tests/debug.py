def get_buff(w,symbol):
    buffer_temp = ""
    _ = 0
    while _ < w:
        buffer_temp = buffer_temp + symbol
        _ = _ + 1
    
    return buffer_temp

def sqr(w,h,sym):
    cntr_y = 0
    buff = ""
    while cntr_y < h:
        buff = get_buff(w,sym)
        print(buff)
        cntr_y = cntr_y + 1
    

sqr(10,5,"#")