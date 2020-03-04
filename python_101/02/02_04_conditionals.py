# Conditionals

def main():
    x , y = 100, 100

    # conditionals: if, elif, else
    if(x < y):
        st = "x is lt y"
    elif(x==y):
        st = "x is eq y"
    else:
        st = "x is gt y"
    
    print(st)

    st = "x is lt y" if(x<y) else "x is gt or eq y"

    print(st)

if __name__ == "__main__":
    main()