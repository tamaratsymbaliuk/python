def move_zeroes(nums):
    length = 0

    # Move non-zero elements to the front of the array
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[length] = nums[i]
            length += 1

    # Fill the remaining elements with zeroes
    while length < len(nums):
        nums[length] = 0
        length += 1

    return nums

def main():
    nums = [0, 0, 1, 0, 2, 5, 6, 0]
    result = move_zeroes(nums)
    print(result)

if __name__ == "__main__":
    main()
