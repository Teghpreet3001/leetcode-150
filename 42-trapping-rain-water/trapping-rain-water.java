class Solution {
    public int trap(int[] bars) {
        int left = 0;
        int right = bars.length - 1;
        int result = 0;
        int max = 0;
        int min = 0;
        while (left < right) {
            min = Math.min(bars[left], bars[right]);
            max = Math.max(max, min);
            result += max - min;
            if (bars[left] < bars[right]) {
                left++;
            }
            else {
                right--;
            }
        }
        return result; 
    }
}