class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        # If p is even, their partner is p + 1.
        # If p is odd, their partner is p - 1.

        n = len(row) // 2  # Number of couples
        position = {person: i for i, person in enumerate(row)}  # Map person to their position
        swaps = 0

        def partner(person): # can also be done by person ^ 1 XOR
            # if person % 2 == 0:
            #     return person + 1
            # else:
            #     return person - 1
            return person ^ 1
        
        def swap(i, j):
            temp = row[i]
            row[i] = row[j]
            row[j] = temp

        
        for i in range(0, 2*n, 2):
            first_person = row[i]
            second_person = row[i + 1]
            correct_partner = partner(first_person)

            if second_person != correct_partner:
                swaps += 1
                # Find the correct partner's position
                pidx = position[correct_partner]
                
                # Swap the second person with the correct partner
                swap(i + 1, pidx)
                
                # Update positions in the map
                position[second_person] = pidx
                position[correct_partner] = i + 1
        return swaps
        