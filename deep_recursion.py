
def deep_recursion():
  import sys
  import pypyjit
  sys.setrecursionlimit(550000)
  pypyjit.set_param('max_unroll_recursion=-1')

# このコードは、Pythonにおける再帰呼び出しの深さを設定し、PyPy JITコンパイラの最適化パラメータを変更しています。

sys.setrecursionlimit(550000):

# Pythonのデフォルトの再帰深さ制限を大幅に引き上げています.
# デフォルトでは再帰深さの制限は通常1000ですが、このコードではそれを550,000に設定しています。

pypyjit.set_param('max_unroll_recursion=-1'):

# PyPyのJIT（Just-In-Time）コンパイラに対するパラメータ設定です。
# この設定では、再帰のアンローリング（unrolling）の深さに制限を設けないようにしています。
# max_unroll_recursionを-1に設定することで、再帰的な関数呼び出しの最適化を制限なしで行うようPyPyに指示しています。
