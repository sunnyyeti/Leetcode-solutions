// Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

// Example 1:

// Input: hour = 12, minutes = 30
// Output: 165
// Example 2:

// Input: hour = 3, minutes = 30
// Output: 75
// Example 3:

// Input: hour = 3, minutes = 15
// Output: 7.5
// Example 4:

// Input: hour = 4, minutes = 50
// Output: 155
// Example 5:

// Input: hour = 12, minutes = 0
// Output: 0

// Constraints:

// 1 <= hour <= 12
// 0 <= minutes <= 59
// Answers within 10^-5 of the actual value will be accepted as correct.
import "math"

func angleClock(hour int, minutes int) float64 {
	hour = hour % 12
	minuteAngle := (float64(minutes) / 60) * 360.0
	hourAngle := float64(hour)*30.0 + (float64(minutes)/60)*30
	deltaAngle := math.Abs(minuteAngle - hourAngle)
	if 360-deltaAngle > deltaAngle {
		return deltaAngle
	}
	return 360 - deltaAngle

}