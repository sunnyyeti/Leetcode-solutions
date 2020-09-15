// Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

// Example 1:

// Input: nums = [1,2,3,1], k = 3, t = 0
// Output: true
// Example 2:

// Input: nums = [1,0,1,1], k = 1, t = 2
// Output: true
// Example 3:

// Input: nums = [1,5,9,1,5,9], k = 2, t = 3
// Output: false
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (k>=nums.length){
            k = nums.length-1;
        }
        TreeMap<Integer, Integer> tree_map = new TreeMap<Integer, Integer>();
        long mingap = Long.MAX_VALUE;
        for (int i=0; i<=k; i++) {
            if (tree_map.containsKey(nums[i])) {
                tree_map.put(nums[i],tree_map.get(nums[i])+1);
                mingap = 0;
            }else {
                tree_map.put(nums[i],1);
            }
        }
        if (mingap==0 && mingap<=(long)t) {
            return true;
        }else{
            int[] topk = Arrays.copyOfRange(nums,0,k+1);
            Arrays.sort(topk);
            for (int i=1;i<topk.length;i++){
                if (((long)topk[i]-(long)topk[i-1])<mingap){
                    mingap = (long)topk[i]-(long)topk[i-1];
                }
            }
            if (mingap <= (long)t) {
                return true;
            }
        }            
        for (int i=k+1; i<nums.length; i++){
            tree_map.put(nums[i-k-1],tree_map.get(nums[i-k-1])-1);
            if (tree_map.get(nums[i-k-1])==0){
                tree_map.remove(nums[i-k-1]);
            }
             mingap = Long.MAX_VALUE;
            if (tree_map.containsKey(nums[i])) {
                tree_map.put(nums[i],tree_map.get(nums[i])+1);
                mingap = 0;
            }else {
                Integer floorkey = tree_map.floorKey(nums[i]);
                if (floorkey != null) {
                    mingap = (long)nums[i]-(long)floorkey;
                }
                Integer ceilingkey = tree_map.ceilingKey(nums[i]);
                if (ceilingkey !=null) {
                    if (((long)ceilingkey-(long)nums[i])<mingap){
                        mingap = (long)ceilingkey-(long)nums[i];
                    }
                }
                if (mingap<=(long)t){
                    return true;
                }
                tree_map.put(nums[i],1);
            }
                
        }
        return false;
    }
}
