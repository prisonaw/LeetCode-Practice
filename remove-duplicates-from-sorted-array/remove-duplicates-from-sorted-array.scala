object Solution {
    def removeDuplicates(nums: Array[Int]): Int = {
        if(nums.length ==0){
            return 0
        }else{
            var start:Int =0;
            var end : Int =1
            while(end<nums.length){
                if(nums(end) != nums(start)){
                    start = start +1
                    nums(start) = nums(end)
                }
                end = end +1
            }
            start + 1
        }
    }
}    
​
