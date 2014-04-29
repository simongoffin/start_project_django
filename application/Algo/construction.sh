g++ -fPIC -c fonction.cpp fonction.h
g++ -shared -o libmylib.so fonction.o
swig -Wall -c++ -python mylib.i 
g++ -fPIC -Wall -Wextra -shared mylib_wrap.cxx -o _mylib.so -L. -lmylib -I/usr/include/python2.7/ -lpython2.7