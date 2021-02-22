// # 	Goal
// # The goal is to remove all duplicate characters (case sensitive), but the last one.
// #
// # Examples: abcaba becomes cba, Aa stays Aa, hello world!!!! becomes he world!.
// # Input
// # Line 1: Input string S.
// # Output
// # Line 1: String with duplicate characters removed.
// # Constraints
// # S contains no Unicode characters.
// # Example
// # Input
// # abcaba
// # Output
// # cba

using static System.Console;using System.Collections.Generic;class S{static void Main(){
var s=ReadLine();var z=new List<char>();
for(int i=s.Length-1;i>=0;i--)if(!z.Contains(s[i]))z.Insert(0,s[i]);Write(string.Join("",z));}}
