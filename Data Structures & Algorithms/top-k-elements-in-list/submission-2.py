class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        lis = []

        for num in nums:
            if num not in res:
                res[num] = 1
            else:
                res[num] += 1

        sorted_res = sorted(res, key=lambda num: res[num], reverse=True)
        for i in range(k):
            lis.append(sorted_res[i])
        
        return lis



            
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
        '''
        myMap = {}
        res = []

        for num in nums:
            if num in myMap :
                myMap[num] += 1
            else:
                myMap[num] = 1
        
        new = sorted(myMap, key=myMap.getCount, reverse = True)

        for i in range(k):
            res[i] = new[i].value()

        return res
'''
    