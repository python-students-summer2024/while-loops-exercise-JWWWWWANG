def get_starting_number():
    num_bottles = int(input("How many bottles of beer on the wall?"))
    if num_bottles > 0:
        return num_bottles
    else:
            print("Please enter a positive number of bottles.")
            
def sing(num_bottles):
    for i in range(num_bottles,0,-1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down, pass it around, {i-1} bottles of beer on the wall.")
