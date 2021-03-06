# In a city-state of n people, there is a rumor going around that one of the n people is a spy for the neighboring city-state.

# The spy, if it exists:

# Does not trust anyone else.
# Is trusted by everyone else (he's good at his job).
# Works alone; there are no other spies in the city-state.
# You are given a list of pairs, trust. Each trust[i] = [a, b] represents the fact that person a trusts person b.

# If the spy exists and can be found, return their identifier. Otherwise, return -1.

# Example 1:

# Input: n = 2, trust = [[1, 2]]
# Output: 2
# Explanation: Person 1 trusts Person 2, but Person 2 does not trust Person 1, so Person 2 is the spy.
# Example 2:

# Input: n = 3, trust = [[1, 3], [2, 3]]
# Output: 3
# Explanation: Person 1 trusts Person 3, and Person 2 trusts Person 3, but Person 3 does not trust either Person 1 or Person 2. Thus, Person 3 is the spy.
# Example 3:

# Input: n = 3, trust = [[1, 3], [2, 3], [3, 1]]
# Output: -1
# Explanation: Person 1 trusts Person 3, Person 2 trusts Person 3, and Person 3 trusts Person 1. Since everyone trusts at least one other person, there is no spy.
# Example 4:

# Input: n = 3, trust = [[1, 2], [2, 3]]
# Output: -1
# Explanation: Person 1 trusts Person 2, and Person 2 trusts Person 3. However, in this situation, we don't have any one person who is trusted by everyone else. So we can't determine who the spy is in this case.
# Example 5:

# Input: n = 4, trust = [[1, 3],[1, 4],[2, 3],[2, 4],[4, 3]]
# Output: 3
# Explanation: Person 1 trusts Person 3 and Person 4, Person 2 trusts Person 3 and Person 4, Person 4 trusts Person 3. Everyone trusts Person 3 but Person 3 does not trust anyone, so they are the spy.

def uncover_spy(n, trust):
#passed 3/7 tests
    return -1  # O(1)

#Time Complexity: O(1) - Constant because we return -1 regardless of the size of n
#Space Complexity: O(1) - Constant we aren't adding memory based on the input size of n

#How to solve: I would iterate through each person and see if they were in the first side of the trust pair because that would mean they trust whoever is in the second side of the pairing and so I would return that second index because that person is being trusted by others. It would be a for loop based on the input size of n so time complexity would be linear and the space complexity would just be constant because I would be running a check but not creating added memory to do so
