#one.py

def func():
	print("FUNC() in ONE.PY")

print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__':
	print("ONE.PY is executed directly")
else:
	print("ONE.PY is imported")