def counter(x):
  t = open(x, 'r')
  t = t.read()
  words = []
  for w in t:
    if w in word:
      words[w] = words [w] +1
    else:
      words[w] = 1

  word_out = words.replace("  ","\n")
