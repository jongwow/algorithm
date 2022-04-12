package main

func canConstruct(ransomNote string, magazine string) bool {
	ransomNoteCount := make([]int, 26)
	magazineCount := make([]int, 26)

	for i := 0; i < len(ransomNote); i++ {
		aa := ransomNote[i]
		val := int(aa) - int('a')
		ransomNoteCount[val]++
	}
	for i := 0; i < len(magazine); i++ {
		aa := magazine[i]
		val := int(aa) - int('a')
		magazineCount[val]++
	}

	for i := 0; i < 26; i++ {
		if ransomNoteCount[i] > magazineCount[i] {
			return false
		}
	}
	return true
}

//func main() {
//
//}
