class Solution(object):
    def reconstructQueue(self, people):
        
        from operator import itemgetter
        
        if not people: return []
        
        retPpl = []
        heights = sorted(list(set([i[0] for i in people])))
        
        # initialize the subset with the tallest people in order of k
        maxHeight = heights.pop()
        for person in people:
            if person[0] == maxHeight:
                retPpl.append(person)
                
        # Sort the lists in place on k value
        retPpl.sort(key=itemgetter(1))
        people.sort(key=itemgetter(1))
        
        # For the second tallest people, third, etc. add them to the subset using k as location
        for height in heights[::-1]:
            for person in people:
                if person[0] == height:
                    # Remove the person and insert them before the first person who has k >= their k value
                    loc = person[1]
                    retPpl.insert(loc,person)
                        
        return retPpl