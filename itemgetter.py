
####################################################

from operator import itemgetter

my_list = [10, 20, 30, 40, 50]
getter = itemgetter(0, 2, 4)  # インデックス0, 2, 4の要素を取得するgetter関数を作成

selected_elements = getter(my_list)  # getter関数をリストに適用して要素を取得
print(selected_elements)  # 出力: (10, 30, 50)

####################################################

from operator import itemgetter

my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
getter = itemgetter('a', 'c')  # キー'a'と'c'の要素を取得するgetter関数を作成

selected_elements = getter(my_dict)  # getter関数を辞書に適用して要素を取得
print(selected_elements)  # 出力: (10, 30)

####################################################
