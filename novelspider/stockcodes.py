# this python file is to produce STOCKCODES for spiders
Init_stockcode = '000669'
STOCKCODES = []
for x in range(3):
        i = '000'+str(int(Init_stockcode)+x)
        STOCKCODES.append(i)