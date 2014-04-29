%module mylib

// Make mylib_wrap.cxx include this header:
%{
#include "fonction.h"
%}
%include "carrays.i"
%array_class(int, intArray);

// Make SWIG look into this header:
%include "fonction.h"