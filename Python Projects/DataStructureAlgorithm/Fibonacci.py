# Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number

# Fn = Fn-1 + Fn-2
# Seed Values F0=0 and F1=1

#!/usr/bin/env python3

# Fibonacci Sequence Generator
# Have the user enter a number and
# generate a fibonacci sequence
# which size is equivalent to that number.


def FibSequence(n):
    """
    Generate a Fibonacci sequence of size n

    """
    series=[]
    while len(series)<n:
        if len(series)==0:
            series.append(0)
        elif len(series)==1:
            series.append(1)
        else:
            series.append(series[-1]+series[-2])

    for i in range(len(series)): # Convert the numbers to strings
        series[i]=str(series[i])


    return (','.join(series)) #return the sequence separated by commas

def main():
    print(FibSequence(int(input('How many number you need: '))))

if __name__=='__main__':
    main()