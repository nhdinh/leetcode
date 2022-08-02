# 1331. Rank Transform of an Array

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return None
        
        arrr = sorted([(idx, arr[idx]) for idx in range(len(arr))], key=lambda i: i[1])
        ret = [0]*len(arr)
        
        # print(arrr)
        
        rank = 1
        cur_val = arrr[0][1]
        cur_id = arrr[0][0]
        ret[cur_id] = rank
        
        for item in arrr[1:]:
            # print(item, rank)
            if (item[1] > cur_val):
                rank += 1
                cur_val = item[1]
            
            ret[item[0]] = rank
            
        return ret
        