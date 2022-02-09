class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list3 = (set(list1) & set(list2))
        minn = 10000
        end = ["1"]
        for i in list3:
            res = list1.index(i) + list2.index(i)
            if res < minn:
                minn = res
                end.pop()
                end.append(i)
            elif res == minn:
                end.append(i)
        return end
