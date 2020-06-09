# 721. Accounts Merge

# Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.
# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

# Example 1:
# Input: 
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# Explanation: 
# The first and third John's are the same person as they have the common email "johnsmith@mail.com".
# The second John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

# Note:
# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].

import collections

class Solution(object):
    def accountsMerge(self, accounts):
        visited_accs = set()
        graph = collections.defaultdict(list)
        rs = []
        
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                graph[email].append(i)
                
        def dfs(i, emails):
            visited_accs.add(i)
            
            for email in accounts[i][1:]:
                emails.add(email)
                for nei in graph[email]:
                    if nei not in visited_accs:
                        dfs(nei, emails)
                    
        for i, acc in enumerate(accounts):
            if i not in visited_accs:
                name = acc[0]
                emails = set()
                dfs(i, emails)
                rs.append([name] + sorted(emails))
        
        return rs

class Solution2(object):
    def accountsMerge(self, accounts):
        parents = []
        
        def find(x):
            if parents[x] == -1:
                return x
            return find(parents[x])
        
        def union(x, y):
            xR = find(x)
            yR = find(y)
            if xR != yR:
                parents[xR] = yR
            
        email_to_id = {}
        id_to_name = {}
        for i, acc in enumerate(accounts):
            id_to_name[i] = acc[0]
            for email in acc[1:]:
                if email not in email_to_id:
                    email_to_id[email] = i
                    parents.append(-1)
                union(i, email_to_id[email])
                
        id_to_emails = collections.defaultdict(list)
        for email, id in email_to_id.items():
            master = find(id)
            id_to_emails[master].append(email)
            
        res = []
        for id, emails in id_to_emails.items():
            res.append([id_to_name[id]] + sorted(emails))
            
        return res
        
                
sol = Solution2()
sol.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])