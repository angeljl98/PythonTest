# code to find closest number to 0
def compute_closest_to_zero(ts):
    if ts==[]:
        m=0
    else:
        ct2=0
        ts_abs=[]
        ts_abs0=[]
        pos_sel00=[]
        min_sel00=[]
        for ct00 in ts:
            ts_abs0.append(abs(ct00))
        print(ts_abs0)
        print(min(ts_abs0))
        cou00=0
        for ct01 in ts_abs0:
            val_min00=ct01
            if val_min00==min(ts_abs0):
                pos_sel00.append(cou00)
                cou00=cou00+1
            else:
                cou00=cou00+1
            #print(pos_sel00)
        for ct02 in pos_sel00:
            min_sel00.append(ts[ct02])
        m=max(min_sel00)
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    return m

var1=compute_closest_to_zero([-3,2,-2,9])
print ("resultado: ",var1)
