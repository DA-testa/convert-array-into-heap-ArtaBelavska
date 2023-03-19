# python3


def build_heap(data):
    swaps = []
    garums=len(data)

    def uz_leju(i):
        left = 2*i+1
        right = 2*i+2
        mazais = i
        
        if left < garums and data[left] < data[mazais]:
            mazais=left
        if right < garums and data[right] < data[mazais]:
            mazais=right
            
        if i != mazais:
            data[i], data[mazais]= data[mazais], data[i]
            swaps.append((i, mazais))
            uz_leju(mazais)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range (garums//2, -1, -1):
        uz_leju(i)
    return swaps


def main():
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    try:
        text=input("Enter I or F: ")
    except EOFError:
        print("Nav ievadīts!")
        return

    if "I" in text:
        # input from keyboard
        garums = int(input())
        data = list(map(int, input().split()))

    elif "F" in text:
        filename=input()
        with open("test/"+filename, 'r') as fails:
            garums=int(fails.readline())
            data=list(map(int, fails.readline().split()))

    else:
        print("Error")
        return
    # checks if lenght of data is the same as the said lenght
    assert len(data) == garums

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
