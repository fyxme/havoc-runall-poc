all: getalivebof

getalivebof: getalivebof.c
	x86_64-w64-mingw32-gcc -o getalivebof.o -c getalivebof.c -Wno-write-strings 
	
	#-Os -s -Qn -nostdlib -Wl,-s,--exclude-all-symbols

clean:
	@rm *.o
