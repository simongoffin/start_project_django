# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_mylib', [dirname(__file__)])
        except ImportError:
            import _mylib
            return _mylib
        if fp is not None:
            try:
                _mod = imp.load_module('_mylib', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _mylib = swig_import_helper()
    del swig_import_helper
else:
    import _mylib
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class intArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _mylib.new_intArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _mylib.delete_intArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _mylib.intArray___getitem__(self, *args)
    def __setitem__(self, *args): return _mylib.intArray___setitem__(self, *args)
    def cast(self): return _mylib.intArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _mylib.intArray_frompointer
    if _newclass:frompointer = staticmethod(_mylib.intArray_frompointer)
intArray_swigregister = _mylib.intArray_swigregister
intArray_swigregister(intArray)

def intArray_frompointer(*args):
  return _mylib.intArray_frompointer(*args)
intArray_frompointer = _mylib.intArray_frompointer


def my_fonction(*args):
  return _mylib.my_fonction(*args)
my_fonction = _mylib.my_fonction

def my_fonction_tab(*args):
  return _mylib.my_fonction_tab(*args)
my_fonction_tab = _mylib.my_fonction_tab
# This file is compatible with both classic and new-style classes.

