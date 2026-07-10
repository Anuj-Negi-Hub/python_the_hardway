#  Convert below inr to usd using for loop 
# inr = [123,445,63,21.5,3,78]

inr_lst = [123, 445, 63, 21.5, 3, 78]
usd_val = 92.5
for i in inr_lst:
    inr_to_usd = i / usd_val
    print(f"{i} INR in USD is {inr_to_usd} USD Dollar.")

print(50 * "*")


#-----------------------------------------------------------------------------------------------------------------------------------------------
#Solve the same problem using function
def inr_to_usd(inr_lst):
    inr_usd_val = 92.5
    for i in inr_lst:
        usd_val = i / inr_usd_val
        print(f"{i} INR in USD is {usd_val} USD Dollar.")

inr_lst = [321, 26, 68, 55, 105, 221]
inr_to_usd(inr_lst)

print(50 * "*")
#-----------------------------------------------------------------------------------------------------------------------------------------------
#Solve the same problem using class

class INR_USD():
    def __init__(self, inr_lst, usd_val):
        self.inr_lst = inr_lst
        self.usd_val = usd_val
    
    def inr_convrt(self):
        for i in self.inr_lst:
            inr_to_usd = i / self.usd_val
            print(f"{i} INR in USD is {inr_to_usd} USD Dollar.")

cur_lst = [48, 99.9, 47, 15.5, 19, 158]
usd_val = 94.6
cur_con = INR_USD(cur_lst, usd_val)

cur_con.inr_convrt()