class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
      arr_a = A.copy()
      arr_a.reverse()
      arr_k = [int(e) for e in str(K)]
      arr_k.reverse()
      larger = None
      if len(arr_a) > len(arr_k):
        larger = arr_a
        smaller = arr_k
      else:
        larger = arr_k
        smaller = arr_a
        
      result = []
      carry = False
      for i in range(len(larger)):
        try:
          num = smaller[i] + larger[i]
        except:
          num = larger[i]
          
        if carry:
          num += 1
          carry = False
          
        if num >= 10:
          carry = True
          num -= 10
          
        result.append(num)
          
      if carry:
        result.append(1)
        
      result.reverse()
        
      return result
