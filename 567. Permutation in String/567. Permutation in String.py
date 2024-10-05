from collections import Counter
class Solution:
    def checkInclusion(self,s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            return False
        
        print("s1: ",s1)
        print("s2: ",s2)

        s1_count = Counter(s1)
        print("s1_count: ",s1_count)
        window_count = Counter(s2[:len_s1])
        print("window_count: ", window_count)
        
        print("------------before-loop--------------------")
    
        for i in range(len_s1, len_s2):
            print(f"------------loop num {i+1} --------------------")

            if s1_count == window_count:
                return True
            
            
            left_char = s2[i - len_s1]
            print("left_char: ",left_char)
            print("s2[i - len_s1]: ", s2[i - len_s1])
            window_count[left_char] -= 1
            print("window_count[left_char]: ",window_count[left_char])

            if window_count[left_char] == 0:
                print("-------if window_count[left_char] == 0 ----------")
                print("window_count: ",window_count)
                del window_count[left_char]
                print("del window_count[left_char] : ",window_count[left_char])
                print("window_count: ", window_count)
            
            
            window_count[s2[i]] += 1
            print("window_count[s2[i]] += 1: ",window_count[s2[i]])

            print("s1_count: ",s1_count)
            print("window_count: ", window_count)
        
        
        return s1_count == window_count


s1 = "ba"
s2 = "eidbaooo"
sol=Solution()
print(sol.checkInclusion(s1, s2))  
