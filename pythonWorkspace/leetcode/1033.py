class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
      x = min(a, b, c)
      z = max(a, b, c)
      y = (a + b + c) - (x + z)
      if z == (y + 1) == (x + 2):
        return [0, 0]
      
      total_distance = z - x
      maxim = total_distance - 2
      xy = y - x
      yz = z - y
      if xy <= 2 or yz <= 2:
        minim = 1
      else:
        minim = 2
      
      return [minim, maxim]
