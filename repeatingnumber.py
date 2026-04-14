def repeating(n):
    seen=set()
    for item in n:
        if item in seen:
            return item
        seen.add()
        return None


hello=[12,432,532,12]
print(repeating(hello))