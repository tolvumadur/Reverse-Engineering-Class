all: shellcode.S shellcode_tester.c
	gcc shellcode_tester.c -o shellcode_test -z execstack -no-pie
	as shellcode.S -o shellcode.o
	ld shellcode.o -o shellcode --oformat=binary
	rm shellcode.o
	python3 x_shellcode.py

evaluate: shellcode.S shellcode_tester.c
	gcc shellcode_tester.c -o shellcode_test -z execstack -no-pie
	as shellcode.S -o shellcode_student.o
	ld shellcode_student.o -o shellcode --oformat=binary
	rm shellcode_student.o
	python3 x_shellcode.py
	./shellcode_test