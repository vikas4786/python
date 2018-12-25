def rev(x,count):
     if count == len(x):
             return
     else:
	     print count
             v_ch=x[count]
             rev(x,count+1)
             print v_ch

rev("python",0)

