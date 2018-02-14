from math import factorial
import time
 
def main():
    """Main Program"""
    start_time = time.time()
 
    n = 40      # The total number of moves for any one path (right + down)
    r = 20      # The total number of right moves for any one path
 
    print factorial(n) / (factorial(r) * factorial(n - r))
    print "Elapsed Time:", (time.time() - start_time) * 1000, "millisecs"
 
if __name__ == '__main__':
    main()
