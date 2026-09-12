NEW
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)
def second_largest(nums):
    largest = nums[0]
    second = nums[1]

    if second > largest:
        largest, second = second, largest

    for num in nums[2:]:
        if num > largest:
            second = largest
            largest = num
        elif num > second:
            second = num

    return second


print(second_largest([10, 5, 8, 20, 15]))