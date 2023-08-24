"""Given an integer array nums and an integer val, remove all occurrences of val
in nums in-place. The order of the elements may be changed. Then return the
number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to
get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the
elements which are not equal to val. The remaining elements of nums are not
important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted."""
from typing import List

nums_for_test, val_for_test = [0, 1, 2, 2, 3, 0, 4, 2], 2


def remove_element(nums: List[int], val: int) -> int:
    counter = 0
    index_counter = 0
    indexes = []
    for index, number in enumerate(nums):
        if number != val:
            counter += 1
        else:
            indexes.append(index)

    for index_for_destroy in indexes:
        del nums[index_for_destroy - index_counter]
        index_counter += 1
    return counter


def remove_element_alternative(nums: List[int], val: int) -> int:
    nums[:] = [num for num in nums if
               num != val]  # Оператор среза `[:]` возвращает полный срез списка
    # То есть новый список, содержащий все элементы исходного списка.
    # При присвоении `[num for num in nums if num != val]` новому срезу все
    # элементы, удовлетворяющие условию `num != val`, добавляются в новый
    # список. Затем новый список присваивается срезу `nums[:]`, что приводит к
    # замене содержимого списка `nums`.

    return len(nums)


print(remove_element(nums_for_test, val_for_test))
