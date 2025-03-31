class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
      result = []
      carry = False
      
      if len(num1) > len(num2):
        big = [int(x) for x in num1]
        small = [int(x) for x in num2]
      else:
        big = [int(x) for x in num2]
        small = [int(x) for x in num1]
      
      big.reverse()
      small.reverse()
      
      for i in range(max(len(num1), len(num2))):
        this_num = 0
        if carry:
          this_num += 1
          carry = False
          
        try:
          this_num += small[i] + big[i]
        except:
          this_num += big[i]
          
        if this_num >= 10:
          this_num -= 10
          carry = True
        else:
          carry = False
        
        result.append(str(this_num))
                
        
      if carry:
        result.append(str(1))
      
      result.reverse()
      return ''.join(result)
