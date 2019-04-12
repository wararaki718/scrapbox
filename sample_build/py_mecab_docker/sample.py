import MeCab
mecab = MeCab.Tagger("-Ochasen")
print(mecab.parse("pythonが大好きです"))
