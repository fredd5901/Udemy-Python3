# function that returns a list of even numbers from an arbitray number of arguments
def is_even(*args):
    even_list = []
    for num in args:
        if num%2 == 0:
            even_list.append(num)
    return even_list
            

mylist = is_even(1,2,3,4,5,6,7,8)
print(mylist)
