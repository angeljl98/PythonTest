// # The program:
// # Your program must find the greatest common divisor for two integers.
// #
// # The greatest common divisor of two integers is the largest positive integer that divides the numbers without a remainder.
// #
// # INPUT:
// # Two integer numbers separated by a whitespace, a and b.
// #
// # OUTPUT:
// # The greatest common divisor of a and b.
// #
// # CONSTRAINTS:
// # 0 < a,b ≤ 1000000
// #
// # EXAMPLE:
// # Input
// # 169 104
// # Output
// # 13
// #
// # Auto-generated code below aims at helping you parse
// # the standard input according to the problem statement.
// #
// # a, b = [int(i) for i in input().split()]
// #
// # Write an answer using print
// # To debug: print("Debug messages...", file=sys.stderr, flush=True)


using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution
{
    static void Main(string[] args)
    {
        string[] inputs = Console.ReadLine().Split(' ');
        int a = int.Parse(inputs[0]);
        int b = int.Parse(inputs[1]);
        int r=0;
        for(int i=1;i<=((a>=b)?b:a);i++)
        {
            r=(a%i==0 && b%i==0)?i:r;
        }
        Console.WriteLine(r);
    }
}
