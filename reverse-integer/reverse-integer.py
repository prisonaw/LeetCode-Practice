class Solution:
    def reverse(self, x: int) -> int:
        onverted_num = str(x)
        rev_li = list()
        li = list()
        for x in onverted_num:
            li.append(x)
        a = "0"
        for i in reversed(li):
            if i.isnumeric():
                a= a + i
            else:
                a = i + a
                
        if int(a) > 2**31 or int(a)<-2**31:
            print("hi")
            return 0
        else:
            return int(a)