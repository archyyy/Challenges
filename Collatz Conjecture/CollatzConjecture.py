"""
Start with a number n > 1.
Find the number of steps it takes to reach one using the following process:
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
"""


def main():
    # get_step(user_input())
    print(f"It took {get_step_recursive(user_input())} steps.")


# def get_step(n):
#     """Function to see how many steps it took"""
#     count = 0
#     while n != 1:
#         if n % 2 == 0:
#             n /= 2
#         else:
#             n = n * 3 + 1
#         count += 1
#         # print(int(n))
#     print(f"It took {count} steps.")


def get_step_recursive(n, count=0):
    """Recursive function to see how many steps it took"""
    if n == 1:
        return count
    elif n % 2 == 0:
        return get_step_recursive(n/2, count+1)
    else:
        return get_step_recursive(n*3+1, count+1)



def user_input():
    '''Get input from user'''
    number = int(input("Type a number to start: "))
    return number


if __name__ == "__main__":
    main()
