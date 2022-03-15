def mid(string, beg, length=None):
    if length == None:
        return string[beg-1:]
    else:
        return string[beg-1:][:length]

def rox(arg1, arg2):
    password = "Qx7BM0v9GDD2YYgfAxtWm2CShiUx2ikHTazpgtf90bEGuUwk46nFlDwmJFfGuLcFxp30f7iQpYIogbVhjqV9Us03sJNQqFTrViarTSJzNBnXY5rFYy6QVxwqfqQrAKUHa3PBu81C4zT4YRE3jX8lFiNQ7JHQBVuXAEQXIajamj1EDqa9n34eHZ7y0XbfuxPt7pMjWo7Jm0btMvzatyCPbZjczioyr3RbIbZDklpZDvbZdKnjKZroMg6EzZA1y2"
    result = ""
    i = 1
    while i < len(arg1) + 1:
        u = i % len(password)
        if u == 0:
            u = len(password)
        result += chr(ord(mid(password, u+arg2, 1)) ^ arg1[i-1])
        i += 1
    return result

arr1 = [123, 11, 48, 89, 76, 63, 6, 59, 118, 65, 47, 104, 51, 39, 51, 27, 120, 41, 36, 50, 51, 44, 5, 75, 65, 36, 77, 92, 101, 55, 5, 4, 88, 2, 90, 90, 2, 104, 59, 91, 21, 16, 33, 13, 19, 7, 88, 54, 29, 91, 21, 62, 75]
arr2 = [35, 33, 60, 17, 9, 127, 109, 17, 78, 82, 109, 64, 28, 110, 13, 105, 98, 116]
arr3 = [47, 39, 58, 70, 14, 80, 16, 27, 20, 75, 73, 78, 101, 14, 85, 49, 30, 15, 90, 17, 26, 102, 30, 33, 22, 1, 38, 63, 70, 52, 1, 41, 2, 42, 88, 9, 92, 69, 20, 23, 15, 56, 28, 60, 58, 79, 93, 81, 118, 28, 2, 20, 118, 95, 57, 18, 87, 19, 26, 57, 110, 53, 7, 5, 0, 52, 45, 31, 3, 70, 11, 99, 40, 28, 59, 119, 13, 108, 110, 4, 66, 40, 6, 76, 94, 98, 56, 76, 25, 64, 80, 69, 63, 71, 60]
arr4 = [26, 89, 24, 113, 51, 48, 52, 28, 14, 48, 9, 46, 53, 12, 4, 5, 8, 67, 54, 54, 27, 29, 123, 77, 28, 88]
arr5 = [33, 23, 68, 54]

print rox(arr1, 143)
print rox(arr2, 125)
print rox(arr3, 30)
print rox(arr4, 4)
print rox(arr5, 0)