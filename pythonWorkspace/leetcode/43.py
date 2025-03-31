class Solution:
    def multiply(self, num1: str, num2: str) -> str:
      n1 = [int(x) for x in num1]
      n2 = [int(x) for x in num2]
      n1.reverse()
      n2.reverse()
        
      result = 0
      
      for i in range(len(n1)):
        primary = (n1[i] * 10**i)
        for j in range(len(n2)):
          secondary = (n2[j] * 10**j)
          result += secondary * primary
          
      return str(result)
