# We are stacking blocks to form a pyramid. Each block has a color which is a one letter string, like `'Z'`.

# For every block of color `C` we place not in the bottom row, we are placing it on top of a left block of color `A` and right block of color `B`. We are allowed to place the block there only if `(A, B, C)` is an allowed triple.

# We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples allowed. Each allowed triple is represented as a string of length 3.

# Return true if we can build the pyramid all the way to the top, otherwise false.

# Example 1:
# Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
# Output: true
# Explanation:
# We can stack the pyramid like this:
    # A
   # / \
  # D   E
 # / \ / \
# X   Y   Z

# This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are allowed triples.
# Example 2:
# Input: bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
# Output: false
# Explanation:
# We can't stack the pyramid to the top.
# Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.
# Note:
# bottom will be a string with length in range [2, 8].
# allowed will have length in range [0, 200].
# Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}.
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        self.rules ={}
        for triple in allowed:
            self.rules.setdefault(triple[:2],set()).add(triple[-1])
        pyramid = [list(bottom)]
        return self.search(pyramid)

    def search(self,pyramid):
        if len(pyramid[-1])==1 and (len(pyramid[-1])+1==len(pyramid[-2])):
            return True
        if len(pyramid)==1 or (len(pyramid[-1])+1==len(pyramid[-2])):
            new_layer = []
            pyramid.append(new_layer)
            key = "".join(pyramid[-2][0:2])
            candidates = self.rules.get(key,set())
            for can in candidates:
                new_layer.append(can)
                if self.search(pyramid):
                    return True
                else:
                    new_layer.pop()
            pyramid.pop()
            return False

        candidates = self.rules.get("".join(pyramid[-2][len(pyramid[-1]):len(pyramid[-1])+2]),set())
        for can in candidates:
            pyramid[-1].append(can)
            if self.search(pyramid):
                return True
            else:
                pyramid[-1].pop()
        return False