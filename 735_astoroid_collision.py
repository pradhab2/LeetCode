class Solution:
    def asteroidCollision(self, asteroids: [int]) -> [int]:
        stack = []
        for a in asteroids:
            if len(stack) == 0:
                stack.append(a)
            else:
                while True:
                    peek = stack[-1]
                    if peek < 0:  # if existing top is -ve we can add -ve or +ve anything to the stack
                        stack.append(a)
                        break
                    elif peek == -a:  # if existing top in stack is -ve, and same +ve is coming the blow that element from                                             stack e.g [-8] srtack and 8 is current
                        stack.pop()
                        break
                    elif peek < -a:  # [3,2,1]  -4 is coming which is bigger -ve value
                        stack.pop()
                        if (len(stack) == 0):
                            stack.append(a)
                            break
                    elif peek > a and a < 0:  # [1,2,3,4] -3   here do nothing as the incoming is small  OR [2] and 1  - op                                                 [2,1]
                        break
                    elif peek > -a:  # [5] 10
                        stack.append(a)
                        break

        return stack

sl=Solution()

print(sl.asteroidCollision([5,10,-5]))