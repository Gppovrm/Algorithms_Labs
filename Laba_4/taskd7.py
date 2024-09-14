def prefix_function(s):
   j = 0
   prefix = [0] * len(s)
   for i in range(1, len(s)):
       j = prefix[i - 1]
       while j > 0 and s[i] != s[j]:
           j = prefix[j - 1]
       if s[i] == s[j]:
           j += 1
       prefix[i] = j
   return prefix




def minimal_length(s):
   n = len(s)
   p = prefix_function(s)
   return n - p[-1]


with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w", encoding='utf-8') as output_file:
   S = input_file.readline().strip()
   result = minimal_length(S)
   output_file.write(str(result))