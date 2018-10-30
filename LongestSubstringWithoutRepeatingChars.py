class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = list(s)
        if not chars:
            return 0
        maxLength = 0
        visited = []
        length = 0
        if " " == chars[0]:
            return 1
        for each in chars:
            if each not in visited:
                visited.append(each)
                length += 1
            else:
                length = len(visited) - visited.index(each)
                del visited[0:visited.index(each)+1]
                visited.append(each)
            maxLength = max(maxLength, length)
        return maxLength