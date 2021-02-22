// # Given an integer N, determine if there exist two integers a, b such that
// # a^2 - b^2 = N
// # Input
// # A single integer N.
// # Output
// # A single word: true or false
// # Constraints
// # 2 ≤ N ≤ 3,000
// # Example
// # Input
// # 5
// # Output
// # true

N=+readline(),z=false;for(i=0;i<=N;i++){for(j=0;j<=N;j++){if(i*i-j*j==N)z=true;}}print(z);
