class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = []
        c[:] = str(int(a) + int(b))
        # Reverses a string
        c.reverse()
        
        for i in range(len(c)):
          if int(c[i]) >= 2:
            c[i] = str(int(c[i]) - 2)
            
            if i + 1 >= len(c):
              c.append(0)
            
            c[i + 1] = str(int(c[i + 1]) + 1)

        c.reverse()
        
        return ''.join(c)
