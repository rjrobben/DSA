# given input = 3
# print the following:
# 1
# 1
# 2
# 1
# 2
# 3

def main(n):
    for i in range(n):
        print(i+1)


# given an array, rerturn the 1st n smallest consevutive intervals that add up to the target sum

def find_subarray_sum(arr, target):
    # initialize the sum to 0
    sum = 0
    # initialize the start and end indices to 0
    start = 0
    end = 0
    # initialize the smallest difference to the largest possible value
    smallest_diff = float('inf')
    # loop through the array
    for i in range(len(arr)):
        # add the current element to the sum
        sum += arr[i]
        # if the sum is greater than the target, subtract the current element from the sum
        if sum > target:
            sum -= arr[i]
            # if the sum is equal to the target, then the difference is 0
            if sum == target:
                return [i, i]
            # if the sum is less than the target, then the difference is the current element
            else:
                diff = target - sum
                # if the difference is less than the smallest difference, then update the smallest difference and the start and end indices
                if diff < smallest_diff:
                    smallest_diff = diff
                    start = i
                    end = i
        # if the sum is equal to the target, then the difference is 0
        elif sum == target:
            return [i, i]
        # if the sum is less than the target, then the difference is the current element
        else:
            diff = target - sum
            # if the difference is less than the smallest difference, then update the smallest difference and the start and end indices
            if diff < smallest_diff:
                smallest_diff = diff
                start = i
                end = i
    # return the start and end indices
    return [start, end]

