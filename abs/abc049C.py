S = input()[::-1]

words = ["dream"[::-1], "erase"[::-1], "eraser"[::-1], "dreamer"[::-1]]
seek = 0

while seek < len(S):
    if S[seek:seek+len(words[0])] == words[0]:
        seek += len(words[0])
    elif S[seek:seek+len(words[1])] == words[1]:
        seek += len(words[1])
    elif S[seek:seek+len(words[2])] == words[2]:
        seek += len(words[2])
    elif S[seek:seek+len(words[3])] == words[3]:
        seek += len(words[3])
    else:
        print("NO")
        break
    if seek >= len(S)-1:
        print("YES")
