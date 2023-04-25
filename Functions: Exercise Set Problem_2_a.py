a=input()
def chat(a):
    if len(a)<=200:
        return a
    else:
        b=a[:200]
        return b
print(chat(a))
