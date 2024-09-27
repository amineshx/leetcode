from typing import List
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        def get_age_from_string(input_string):
            if len(input_string) >= 4:
                last_four = input_string[-4:]
                age_str = last_four[:2]  
                age = int(age_str)
                return age
        res=0
        for c in details:
            age=get_age_from_string(c)
            if age > 60:
                res+=1
        return res