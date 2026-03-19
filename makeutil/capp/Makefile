.PHONY: another-app
#not all targets are listed in PHONY

#Might be correct, but 'build' and 'app' are different
build: main.c
	gcc main.c -o app

#Correct no PHONY
app: main.c
	gcc main.c -o app

#Incorrect listed in PHONY
another-app: main.c
	gcc main.c -o app