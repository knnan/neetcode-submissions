class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        solution:
        1)reverse the s and check if revS == s , o(n) time , b(n) space
        2)use two poiter from each end and move inwards , if at any point low != high invalid , 
            time: o(n) we have to iterate thorugh the array once
            space: o(1) we dont need any extra space



        """

      
        lo = 0
        hi = len(s) -1 

        while lo < hi:
            while lo < len(s) and not s[lo].isalnum():
                lo +=1
            while hi >= 0 and not s[hi].isalnum():
                hi -= 1
            
            if not lo < hi:
                break
            if s[lo].lower() != s[hi].lower():
                return False
            lo += 1
            hi -= 1
        return True
      


        