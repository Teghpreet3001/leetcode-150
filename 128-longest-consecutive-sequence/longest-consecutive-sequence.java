class Solution {
    public int longestConsecutive(int[] nums) {
        List<Integer> numList = Arrays.asList(
            Arrays.stream(nums).boxed().toArray(Integer[]::new)
        );
        HashSet<Integer> numSet = new HashSet<>(numList);
        int result = 0;
        for (int num: nums) {
            if (!numSet.contains(num - 1)) {
                int length = 1;
                while (numSet.contains(num + length)) {
                    length++;
                }
                result = Math.max(result, length);
            }
        }
        return result;
    }
}