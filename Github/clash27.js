// # The program:
// # Swap each character at an even position with the next character if there is one. Positions start at zero.
// # INPUT:
// # A single string s.
// #
// # OUTPUT:
// # The transformed string.
// #
// # CONSTRAINTS:
// # s contains less than 8192 characters.
// #
// # EXAMPLE:
// # Input
// # ABCDEF
// # Output
// # BADCFE

S = readline().split('')
for(i=1;i<S.length;i+=2)[S[i-1],S[i]]=[S[i],S[i-1]]
print(S.join(''))
