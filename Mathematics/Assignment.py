def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    nums = sorted(numbers)
    m = len(nums)
    mid = m // 2

    if m % 2 == 0:
        return (nums[mid -1] + nums[mid]) / 2
    else:
        return nums[mid]
    
def variance(numbers):
    n = mean(numbers)
    return sum((y -n) ** 2 for y in numbers) / len(numbers)


### EXAMPLE USAGE:###
data = [3, 6, 9, 12, 15]
print("Mean:", mean(data))
print("Median:", median(data))
print("Variance:", variance(data))
