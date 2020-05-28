
def sqli_check(input): #Method to escape query parameters to prevent sql injection
	dangerous_chars = {"\"": "\\\"", "'": "\\'"}
	for key in dangerous_chars:
		input = input.replace(key, dangerous_chars[key])
	return input
