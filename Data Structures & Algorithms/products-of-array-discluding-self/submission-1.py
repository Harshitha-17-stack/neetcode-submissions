class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        no_of_zeros = 0
        for num in nums:
            if num == 0:
                no_of_zeros += 1
        
        if no_of_zeros > 1:
            return [0 for _ in range(len(nums))]

        total = 1
        for num in nums:
            if num != 0:
                total *= num
        
        products = []
        for num in nums:
            if no_of_zeros == 1:
                if num == 0:
                    products += [total]
                else:
                    products += [0]
            else:
                products += [total // num]
        return products
