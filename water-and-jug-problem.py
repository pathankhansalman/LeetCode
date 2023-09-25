from fractions import gcd
class Solution(object):
    def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        """
        :type jug1Capacity: int
        :type jug2Capacity: int
        :type targetCapacity: int
        :rtype: bool
        """
        if targetCapacity > jug1Capacity + jug2Capacity:
            return False
        if targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0:
            return True
        return False