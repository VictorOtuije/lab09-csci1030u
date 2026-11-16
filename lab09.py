# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    # 1. Check each number in the list
    # 2. Compare it with the numbers after it
    # 3. If 2 numbers add up to the target, return their indices

    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    pass
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def max_profit(prices):
    # Outline:
    # 1. Keep track of the lowest price so far
    # 2. Calculate the profit using the current price
    # 3. Keep track of the highest profit
    # 4. Return the higheest profit

    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    pass
    if len(prices) == 0:
        return 0

    lowest_price = prices[0]
    highest_profit = 0

    for price in prices:
        profit = price - lowest_price

        if profit > highest_profit:
            highest_profit = profit

        if price < lowest_price:
            lowest_price = price

    return highest_profit

def max_subarray(nums):
    # Outline:
    # 1. Start with the first number
    # 2. keep track of the current sum
    # 3. add each new number or start a new sum
    # 4. keep track of the largest sum
    # 5. return to the largest sum

    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    pass

    current_sum = nums[0]
    largest_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        largest_sum = max(largest_sum, current_sum)

    return (largest_sum)


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    # 1. Create an empty list to store opening brackets
    # 2. Check each character in the string
    # 3. Add opening brackets to the list
    # 4. Check if closing brackets match the last opening bracket
    # 5. Return True if everything matches, otherwise False

    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass

    stack = []

    for char in s:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack:
                return False

            last = stack.pop()

            if(char ==")" and last != "(") or \
              (char == "]" and last != "[") or \
              (char == "}" and last != "{"):
                return False

    return len(stack) == 0 




def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
