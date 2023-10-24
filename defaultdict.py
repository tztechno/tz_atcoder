from collections import defaultdict

# defaultdictの初期化
# 引数にデフォルトの値を指定します
# この例ではint()を指定していますので、デフォルト値は0になります
my_dict = defaultdict(int)

# キーを追加
my_dict['apple'] = 3
my_dict['banana'] = 2

# 存在しないキーを参照してもエラーが発生しない
# デフォルト値が自動的に割り当てられます
print(my_dict['cherry'])  # 出力: 0

# キーが存在しない場合でも、デフォルト値を更新できます
my_dict['cherry'] += 1

# デフォルト値は0から1に更新されます
print(my_dict['cherry'])  # 出力: 1

######################################

from collections import defaultdict

# defaultdictの初期化
# デフォルト値として空のリストを指定しています
dic = defaultdict(lambda: [])

# 新しいキーにアクセス
# 存在しないキーを参照しても、空のリストが自動的に割り当てられます
dic['fruits'].append('apple')

# 存在しないキー 'fruits' が自動的に作成され、リストに 'apple' が追加されます
print(dic)  # 出力: defaultdict(<function <lambda> at 0x7f386a8cc950>, {'fruits': ['apple']})

# 別のキーにアクセス
# 存在しないキー 'vegetables' が自動的に作成され、空のリストに 'carrot' が追加されます
dic['vegetables'].append('carrot')
print(dic)  # 出力: defaultdict(<function <lambda> at 0x7f386a8cc950>, {'fruits': ['apple'], 'vegetables': ['carrot']})

