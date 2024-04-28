def remove_duplicates(nums):
    if not nums:
        return []
    
    length = 1  # Start length at 1 assuming there's at least one element in the array
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[length] = nums[i]
            length += 1
    
    return nums[:length]

def main():
    nums = [0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
    unique_numbers = remove_duplicates(nums)
    print("Array with duplicates removed:", unique_numbers)

if __name__ == "__main__":
    main()
