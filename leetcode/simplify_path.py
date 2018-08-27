class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        curr_path = []
        for chunk in path.split('/'):
            if not chunk or chunk == '.':
                continue
            elif chunk == '..':
                if curr_path:
                    curr_path.pop()
            else:
                curr_path.append(chunk)
        return '/' + '/'.join(curr_path)
