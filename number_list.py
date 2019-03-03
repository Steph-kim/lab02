
def find_reverse(numbers):
    return numbers[::-1]

def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)

def find_sum(numbers):
    return sum(numbers)

def find_average(numbers):
    return sum(numbers)/len(numbers)

def find_descending(numbers):
    return sorted(numbers, reverse = True)

def second_smallest(numbers):
    
    first=second=float('inf')
    for i in numbers:
        if i < first:
            second,first = first, i
        elif first < i < second:
            second = i
    return second

def kth_smallest(numbers, k):
    
    numbers = list(set(numbers))
    numbers =  sorted(numbers)

    return numbers[k-1]

if __name__ == '__main__':
    numbers = [1,1,2,1,2,3,4,5,6]
    numbers2 = [1,2,3,4,5]
    print("the 2th smallest number is:", second_smallest(numbers2))
    print("the kth smallest number is:", kth_smallest(numbers,3))
    pass