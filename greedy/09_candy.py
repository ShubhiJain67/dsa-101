class Solution:
    def candy(self, ratings: List[int]) -> int:
        return self.withExtraSpace(ratings)
    
    def withExtraSpace(self, ratings):
        candies = [1]*len(ratings)
        # Acknowledging left neighbour
        for index in range(1, len(ratings)):
            if ratings[index] > ratings[index-1]:
                candies[index] = candies[index-1] + 1
        # Acknowledging right neighbour
        for index in range(len(ratings)-2, -1, -1):
            if ratings[index] > ratings[index+1]:
                # here at index we are considerign the left and index + 1 is right
                candies[index] = max(candies[index], candies[index+1] + 1)
        return sum(candies)
