// An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

// 'A': Absent.
// 'L': Late.
// 'P': Present.
// Any student is eligible for an attendance award if they meet both of the following criteria:

// The student was absent ('A') for strictly fewer than 2 days total.
// The student was never late ('L') for 3 or more consecutive days.
// Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.

// Example 1:

// Input: n = 2
// Output: 8
// Explanation: There are 8 records with length 2 that are eligible for an award:
// "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
// Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
// Example 2:

// Input: n = 1
// Output: 3
// Example 3:

// Input: n = 10101
// Output: 183236316

// Constraints:

// 1 <= n <= 105
func checkRecord(n int) int {
	const M uint64 = 1000000007
	dp := []uint64{1, 1, 0, 1, 0, 0}
	for i := 1; i < n; i++ {
		ndp := make([]uint64, 6)
		ndp[0] = (dp[0] + dp[1] + dp[2]) % M
		ndp[1] = dp[0]
		ndp[2] = dp[1]
		ndp[3] = (dp[0] + dp[1] + dp[2] + dp[3] + dp[4] + dp[5]) % M
		ndp[4] = dp[3]
		ndp[5] = dp[4]
		dp = ndp
	}
	return int((dp[0] + dp[1] + dp[2] + dp[3] + dp[4] + dp[5]) % M)
}

// Use number of A and how many consecutive L at the end to distinguish different states.
// We have six states and get the following transition functions:
//  states 0A0L 0A1L 0A2L 1A0L 1A1L 1A2L
//  0A0L + P -> 0A0L
//  0A0L + A -> 1A0L
//  0A0L + L -> 0A1L
//  0A1L + P -> 0A0L
//  0A1L + A -> 1A0L
//  0A1L + L -> 0A2L
//  0A2L + P -> 0A0L
//  0A2L + A -> 1A0L
//  0A2L + L -> x
//  1A0L + P -> 1A0L
//  1A0L + A -> x
//  1A0L + L -> 1A1L
//  1A1L + P -> 1A0L
//  1A1L + A -> x
//  1A1L + L -> 1A2L
//  1A2L + P -> 1A0L
//  1A2L + A -> x
//  1A2L + L -> x

//   0A0L 0A1L 0A2L 1A0L 1A1L 1A2L
// 1 1    1    0    1    0    0
// 2 2    1    1    3    1    0
