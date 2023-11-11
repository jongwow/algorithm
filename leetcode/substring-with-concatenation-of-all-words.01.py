from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # words 로 부터 알 수 있는 사실,
        # 단어의 개수 * 단어의 길이 = concat string 의 길이
        # s를 순회. i, i+concat_string_len 만큼 자름.
        # - sub_str 이 permutation 문자열인지 판단
        # - - 단어의 길이만큼 자름. sub_word 가 words_book 에 있는지 확인 -> 있으면 book 에서 -1, 없으면 break
        s_len = len(s)
        word_cnt = len(words)
        word_len = len(words[0])
        word_book = {}
        for word in words:
            if word in word_book:
                word_book[word] += 1
            else:
                word_book[word] = 1
        concat_str_len = word_cnt * word_len
        idx = 0
        ans = []
        while idx + concat_str_len <= s_len:
            sub_s = s[idx:idx+concat_str_len]
            word_book_copy = word_book.copy()
            word_idx = 0
            flag = True
            while word_idx + word_len <= len(sub_s):
                sub_word = sub_s[word_idx:word_idx+word_len]
                if (sub_word in word_book_copy) and (word_book_copy[sub_word] > 0):
                    word_book_copy[sub_word] -= 1
                    word_idx += word_len
                else:
                    flag = False
                    break
            if flag and not any(word_book_copy.values()):
                ans.append(idx)
            idx += 1
        return ans

    def findSubstring_1(self, s: str, words: List[str]) -> List[int]:
        # words 로 부터 알 수 있는 사실,
        # 단어의 개수 * 단어의 길이 = concat string 의 길이
        # s를 순회. i, i+concat_string_len 만큼 자름.
        # - sub_str 이 permutation 문자열인지 판단
        # - - 단어의 길이만큼 자름. sub_word 가 words_book 에 있는지 확인 -> 있으면 book 에서 -1, 없으면 break
        s_len = len(s)
        word_cnt = len(words)
        word_len = len(words[0])
        word_book = {}
        for word in words:
            if word in word_book:
                word_book[word] += 1
            else:
                word_book[word] = 1
        concat_str_len = word_cnt * word_len
        idx = 0
        ans = []
        while idx + concat_str_len <= s_len:
            sub_s = s[idx:idx+concat_str_len]
            # print('sub_s:', sub_s)
            word_book_copy = word_book.copy()
            word_idx = 0
            flag = True
            while word_idx + word_len <= len(sub_s):
                sub_word = sub_s[word_idx:word_idx+word_len]
                # print('sub_word:', sub_word)
                if not (sub_word in word_book_copy):
                    # print('not exist')
                    flag = False
                    break
                word_book_copy[sub_word] -= 1
                if word_book_copy[sub_word] < 0:
                    # print('lower than 0')
                    flag = False
                    break
                word_idx += word_len
            if flag and not any(word_book_copy.values()):
                ans.append(idx)
            idx += 1
        return ans


tcs = [
    ["barfoothefoobarman", ["foo", "bar"]],
    ["wordgoodgoodgoodbestword", ["word", "good", "best", "word"]],
    ["barfoofoobarthefoobarman", ["bar", "foo", "the"]]
]
for tc in tcs:
    sol = Solution().findSubstring(tc[0], tc[1])
    print(sol)
