import re

# 元の文字列
text = "これは(123) サンプル(456) 文字列です。"

# 正規表現パターンを定義
pattern = r'\(\d+\)'

# 正規表現パターンに一致する部分を削除
result = re.sub(pattern, '', text)

# 結果を出力
print(result)
