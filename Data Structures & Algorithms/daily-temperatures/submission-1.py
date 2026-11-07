class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_i = stack.pop()
                days = i - prev_i

                result[prev_i] = days


            stack.append(i)

        return result