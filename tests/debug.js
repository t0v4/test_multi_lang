function get_buff(w,symbol){
    var buffer_temp = "";
    var _ = 0;
    while(_ < w){
        buffer_temp = buffer_temp + symbol;
        _ = _ + 1;
    }
    return buffer_temp;
}
function sqr(w,h,sym){
    var cntr_y = 0;
    var buff = "";
    while(cntr_y < h){
        buff = get_buff(w,sym);
        console.log(buff);
        cntr_y = cntr_y + 1;
    }
}
sqr(10,5,"#");