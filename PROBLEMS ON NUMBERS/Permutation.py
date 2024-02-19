import math

def permutations(N, R):
    return math.factorial(N) // math.factorial(N - R)

if __name__ == "__main__":
    N = int(input("Enter the number of people (N): "))
    R = int(input("Enter the number of seats (R): "))
    
    result = permutations(N, R)
    print("Number of permutations:", result)


# #include<bits/stdc++.h>
# using namespace std;
# int fact(int n) {
# 	int ans = 1;
# 	for (int i = 1; i <= n; i++) {
# 		ans *= i;
# 	}
# 	return ans;
# }
# int main() {
# 	int n = 6, r = 4;
# 	int num = fact(n);
# 	int den = fact(n - r);
# 	cout << num / den;
# }
