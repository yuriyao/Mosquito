#encoding:utf-8
#进行系统的一些加密工作

CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
LIMITS = len(CHARS)

#结果每个字符会被压在字母范围内
def code_undecode(src, key = 0):
	"""进行不可解密的加密, src是待加密的字符串,
		key是加密的'密匙',可以为空"""
	if not src:
		return ''
	length = len(src)
	result = range(length)
	for i in range(length - 1):
		result[i] = ord(src[i]) ^ ord(src[i + 1])
	result[length - 1] = ord(src[length - 1]) ^ ord(src[0])
	if key:
		for i in range(length):
			result[i] ^= key
	for i in range(length):
		result[i] = CHARS[result[i] % LIMITS]
	return ''.join(result)


	



