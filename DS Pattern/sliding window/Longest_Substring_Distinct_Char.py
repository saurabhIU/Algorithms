"""
Given a string, find the length of the longest substring, which has all distinct characters. Return the longest substring

Input: String="aabccbb"
Output: abc
Explanation: The longest substring with distinct characters is "abc".

Input: String="abbbb"
Output: ab
Explanation: The longest substring with distinct characters is "ab".

"""
def longestSubstringWithoutDuplication(string):
    # Write your code here.
	char_dict = {}
	window_start = 0
	max_string = ""
	
	for window_end in range(len(string)):
		new_char = string[window_end]
		if new_char in char_dict:
			window_start = max(window_start,char_dict[new_char]+1)
		char_dict[new_char] = window_end
		new_string = string[window_start:window_end+1]
		if len(new_string) > len(max_string):
			max_string = new_string
	return max_string

print(f'Longest substring without duplicate character in string clementisacap is {longestSubstringWithoutDuplication("clementisacap")} ')

        
