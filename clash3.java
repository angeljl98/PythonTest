// You must output the percentage of points that are within the circle.
//
// A point on the edge of the circle is considered as inside of it.
//
// Input
// Line 1: cx - Two space separated integers cx and cy for the coordinates of the circle center point
// Line 2: r - Integer for the circle radius
// Line 3: n - Integer for the number of points
// Next n lines: Two space separated integers px and py for the coordinates of a point
// Output
// The percentage of points that are within the circle
// Constraints
// The testcases are designed in a way that the result will always be an integer in range 0 - 100
// Example
// Input
// 5 4
// 2
// 1
// 6 3
// Output
// 100

import java.util.*;
import java.io.*;
import java.math.*;
class Solution {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int cx = in.nextInt();
        int cy = in.nextInt();
        int r = in.nextInt();
        int n = in.nextInt();
        double percent = 0;
        for (int i = 0; i < n; i++) {
            int px = in.nextInt();
            int py = in.nextInt();
            double d = Math.sqrt(Math.pow(cx-px,2)+Math.pow(cy-py,2));
            if(Math.pow(d,2) <= Math.pow(r,2))percent++;
            }
        System.out.println((int) (percent*100)/n);
    }
}
