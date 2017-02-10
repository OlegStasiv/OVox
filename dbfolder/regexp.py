import re
word = "<p>Hello easyqa.thinkmobiles+64804@gmail.com!</p>"

regexp = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
if regexp.search(word) is not None:
  print 'matched'