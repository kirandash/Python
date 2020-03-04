# Loops

def main():
    x = 0
    y = 0

    # While loop
    while(x < 5):
        print(x)
        x = x+1 # 0,1,2,3,4

    # For Loop
    for y in range(5, 10): 
        print(y) # 5,6,7,8,9

    # For Loop on collection
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)

    # use Break and continue
    for x in range(5, 10):
        if (x==7): break
        print(x) # 5,6

    for x in range(5, 10):
        if (x%2 == 0): continue
        print(x) # 5,7,9

    # Use enumerate() fn to get index
    for i,d in enumerate(days):
        print(i, d)
            
if __name__ == "__main__":
    main()