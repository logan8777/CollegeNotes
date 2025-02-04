def isPerfectSquare(num):
    left, right = 1, num
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == num:
            return True
        elif mid * mid < num:
            left = mid + 1
        else:
            right = mid - 1
    return False

n = int(input("Enter a number: "))
print(isPerfectSquare(n))