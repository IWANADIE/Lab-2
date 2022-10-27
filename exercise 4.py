import statistics
def main():
    get_user_input()
    calc_average_temperature()
    #calc_min_max_temperature()

def get_user_input():
    x = input()
    print("You entered: " + x)
    y = x.split(",")
    print(y)
    mylist = y
    print(mylist)
    z = list(map(float, mylist))
    print(z)

    return z
def calc_average_temperature(num):
    x = sum(num)/len(num)
    print(x)
def calc_min_max_temperature():
    print("Please enter the temperature to find min and max: ")
    y = input()
    print(y)

main ()