# code to find closest number to 0
def compute_closest_to_zero(ts):
    if ts==[]:
        m=0
    else:
        ct2=0
        ts_abs=[]
        for ct1 in ts:
            ts_abs.append(abs(ct1))
            val_min=min(ts_abs)
            if (val_min==abs(ct1)):
                pos_sel=ct2
            ct2=ct2+1
        m=ts[pos_sel]
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    return m

var1=compute_closest_to_zero([-3,3,-2,9])
print(var1)
