#!/usr/bin/python3
import re
def calc(A,B): 
 ai=str(A) 
 bi=str(B) 
 p = re.compile('¥d+(¥.¥d+)?') 
 if p.match(ai) or p.match(bi): 
 a=float(ai) 
 b=float(bi) 

def main (): 
matchstring = '' 
while matchstring != 'end': 
 A = input ('input A: ') 
 B = input ('input B: ') 
 print ('input A * input B = ', calc(A,B)) 
if __name__ == '__main__': 
main()
