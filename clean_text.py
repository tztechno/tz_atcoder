import re
def clean_text(text):
    if isinstance(text, str):
        pattern = r"[^\x00-\x7F]+"
        cleaned_text = re.sub(pattern, '', text)
        return cleaned_text
    else:
        return str(text)
