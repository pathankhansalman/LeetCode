class RecentCounter(object):

    def __init__(self):
        self.ping_ts = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.ping_ts = [t] + self.ping_ts
        count = 0
        for time in self.ping_ts:
            if t - time <= 3000:
                count += 1
                continue
            break
        return count
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)