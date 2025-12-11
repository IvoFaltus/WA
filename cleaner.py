import sys
import re




def strip_comments(code, lang):
    if lang == "python":
        # remove # comments
        code = re.sub(r"#.*", "", code)
        # remove triple-quoted docstrings
        code = re.sub(r'("""|\'\'\')(.*?)\1', "", code, flags=re.DOTALL)
    elif lang == "c" or lang == "cpp" or lang == "java":
        # remove // comments
        code = re.sub(r"//.*", "", code)
        # remove /* */ comments
        code = re.sub(r"/\*.*?\*/", "", code, flags=re.DOTALL)
    elif lang == "html":
        # remove <!-- --> comments
        code = re.sub(r"<!--.*?-->", "", code, flags=re.DOTALL)
    elif lang == "js":
        # remove // comments
        code = re.sub(r"//.*", "", code)
        # remove /* */ comments
        code = re.sub(r"/\*.*?\*/", "", code, flags=re.DOTALL)
    elif lang == "css":
        # remove /* */ comments
        code = re.sub(r"/\*.*?\*/", "", code, flags=re.DOTALL)
    return code

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: cleaner.py <filePath> <lang>")
        sys.exit()

    path = sys.argv[1]
    lang = sys.argv[2].lower()

    with open(path, "r") as f:
        content = f.read()

    cleaned = strip_comments(content, lang)
    
    with open(path, "w") as f:
        f.write(cleaned)
