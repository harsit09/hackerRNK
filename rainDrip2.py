class Solution(object):
   def trap(self, height):
      stack = []
      water = 0
      i=0
      while i<len(height):
         if len(stack) == 0 or height[stack[-1]]>=height[i]:
            stack.append(i)
            i+=1
         else:
            x = stack[-1]
            stack.pop()
            if len(stack) != 0:
               temp = min(height[stack[-1]],height[i])
               dist = i - stack[-1]-1
               water += dist*(temp - height[x])
      return water
ob = Solution()
print(ob.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
