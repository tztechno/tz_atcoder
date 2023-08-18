
import re

def remove_whitespace(text):
    # 改行とタブを削除
    text = re.sub(r'\n|\t', '', text)
    
    # 行頭・行末のスペースを削除
    text = text.strip()
    
    # 全てのスペースを削除
    text = re.sub(r'\s+', '', text)
    
    return text

input_text = """
    This is some text with leading and trailing spaces.    
    It also has tabs and
    newlines.
"""

cleaned_text = remove_whitespace(input_text)
print(cleaned_text)
