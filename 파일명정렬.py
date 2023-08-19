import re
def solution(files):
    answer = []
    files = [re.split(r"([0-9]+)",s) for s in files]
    files.sort(key = lambda x :(x[0].lower(),int(x[1])))
    return [''.join(file) for file in files]