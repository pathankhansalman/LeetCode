class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trust_dict = {i:[] for i in range(1, n + 1)}
        for trust_pair in trust:
            trust_dict[trust_pair[1]].append(trust_pair[0])
        judge_prob = [k for k in trust_dict.keys() if len(trust_dict[k]) == n - 1]
        if len(judge_prob) != 1:
            return -1
        for trust_pair in trust:
            if trust_pair[0] == judge_prob[0]:
                return -1
        return judge_prob[0]
