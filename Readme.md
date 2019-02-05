# Readme for Illumio Coding Assignment
# Tianxin Zhou

Time complexity:
The reason that I use dictionary to solve the assignment is the lookup time for dict in python is O(1).
We need to check every incoming packet according to rules. Then if we have a large set of rules, the lookup time is important.
By the assignment requirement: direction and protocol are prefixed, so I decide to prefix them in the dictionary. And I assume that there might be multiple ips for one port number,
then I use list as the dict value for ports.

Extra idea:
I had a idea that might be faster than the current solution in the situation that has fewer range values:
to represent each rule/ packet as a string or number and compare values between them.


Teams:

1. platform
2. policy
3. data
