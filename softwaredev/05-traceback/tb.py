import sys
for i in range(sys.getrecursionlimit()):
    try:
        print(f"{i+1}: {sys._getframe(i)}")
    except:
        break
