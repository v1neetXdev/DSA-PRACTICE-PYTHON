# nums -> n : it means index is o
# ans -> n : also here index = 0
# ans[i] = nums[nums[i]]
# o <= i < nums.length
# ----------------------------------------------
# nums = [5 , 0 , 1 , 2 , 3 , 4]
# ans = []
# for i in range( 0 , len(nums)) :
#     ans.append(nums[nums[i]])
# print(ans)
# ----------------------------------------------
# 1920. Build Array from Permutation
def name(ans , nums , n) :
    if ( n == len(nums)) :
        return ans

    else :
        ans.append(nums[nums[n]])
        return name(ans , nums, n + 1)




print(name([] , [5 , 0 , 1 , 2 , 3 , 4] , 0))
