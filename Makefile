debug:
	python3 src/PasswordGenerator.py

release:
	pyinstaller -w -F -i images/PasswordGenerator.ico src/PasswordGenerator.py && mv dist/PasswordGenerator.exe ../PasswordGenerator-Python