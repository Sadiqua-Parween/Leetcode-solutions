class Solution(object):
    def combine(self, n, k):
        result = []

        def bt(index , path):
            if len(path) == k:
                result.append(path[:])
                return
            
            if index <= n:
                path.append(index)
                bt(index+1  , path)
                path.pop()
                bt(index +1 , path)
            
        bt(1 , [])
        return result
        