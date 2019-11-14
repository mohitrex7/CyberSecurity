def UTF8(string):
	if isinstance(string,unicode):
		return string.encode('UTF-8')
	else:
		return str(string)
