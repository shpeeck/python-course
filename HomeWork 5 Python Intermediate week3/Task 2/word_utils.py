
def clean(str):
    symbols = '''!()-[]{};?@#$%:'",\./^&amp;*_'''
    for i in symbols:
        str = str.replace(i, "")
    return str.strip()

def words_list(str):
    return list(set(clean(str).split(" ")))

def long(str):
    return max(words_list(str), key=len)

if __name__ == "__main__":
    print("word_utils module")