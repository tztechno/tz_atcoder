try:
    # ここに例外が発生する可能性のあるコードを記述する
    result = some_function()
except ExceptionType1:
    # ExceptionType1 の例外が発生した場合の処理
    handle_exception_type1()
except ExceptionType2:
    # ExceptionType2 の例外が発生した場合の処理
    handle_exception_type2()
# 他の例外の処理をここに追加することもできます
except:
    # 上記以外の例外が発生した場合の共通の処理
    handle_other_exceptions()
