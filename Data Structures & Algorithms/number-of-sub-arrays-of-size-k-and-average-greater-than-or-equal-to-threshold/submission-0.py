class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        res = 0
        curr_sum = 0


        for right in range(len(arr)):
            curr_sum += arr[right]

            if (right-left +1) > k:
                curr_sum -= arr[left]
                left += 1

            if (right-left +1 ) == k:
                avg = curr_sum / k
            
                if avg >= threshold:
                    res += 1
        return res
            



