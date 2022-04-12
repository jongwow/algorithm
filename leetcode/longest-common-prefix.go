package main

func longestCommonPrefix(strs []string) string {
	// i와 i+1 비교.
	// 0부터 len까지 같은지.
	// 그 전에 끝나면 len값 갱신.
	minLength := 201
	for i := 0; i < len(strs); i++ {
		if len(strs[i]) < minLength {
			minLength = len(strs[i])
		}
	}
	for i := 0; i < len(strs)-1; i++ {
		a := strs[i]
		b := strs[i+1]
		for j := 0; j < minLength; j++ {
			if a[j] != b[j] {
				minLength = j
				break
			}
		}
	}
	return strs[0][:minLength]
}
