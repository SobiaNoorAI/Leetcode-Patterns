class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        for i in range (len(tickets)):
            queue.append((i, tickets[i]))

        t=0

        while queue: 
            person, count= queue.popleft()
            count-=1
            t+=1

            if count>0:
                queue.append((person, count))
            
            if person ==k and count ==0:
                return t
        

