def get_starting_number():
    num_bottles = int(input("How many bottles of beer on the wall?"))
    if num_bottles > 0:
        return num_bottles
    else:
            print("Please enter a positive number of bottles.")
            
def sing(num_bottles):
    have_more_bottles = True
    while have_more_bottles:
        print(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.")
        print(f"Take one down, pass it around, {num_bottles-1} bottles of beer on the wall.")
        num_bottles -= 1
        have_more_bottles = num_bottles > 0