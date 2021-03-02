# code to find closest number to 0
def compute_closest_to_zero(ts):
    if ts==[]:
        m=0
    else:
        n=len(ts)
        if n==1:
            m=ts(1)
        else:
            vector1=ts
            ct1=0
            menor=0
            for flg1 in vector1:
                ct1=ct1+1
                flg2=(0.00)
                if type(flg1)==int:
                    flg2[ct1]=float(-abs(flg1-0))
                elif type(flg1)==int and flg1<0:
                    flg2[ct1]=float(-abs(flg1-0))-0.01
                else:
                    flg2[ct1]=1
            menor=min(flg2)
            pos_menor=flg2.index(menor)
            m=ts(pos_menor)
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    return m

var1=compute_closest_to_zero(0,5,8,9)
print(var1)
