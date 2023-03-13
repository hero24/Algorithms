#include <Python.h>
#include "../../c/searching/rk.h"


static PyObject* rabin_karp(PyObject* self, PyObject* args)
{
	char* sample;
	char* test;
	int index;
	if(!PyArg_ParseTuple(args, "ss", &sample, &test))
		return NULL;
	index = rk(test, sample);
	if(index< 0)
		return Py_False;

	return Py_BuildValue("i", index);
}

static PyObject* rabin_karp_shift(PyObject* self, PyObject* args)
{
	char* sample;
	char* test;
	int index;
	if(!PyArg_ParseTuple(args, "ss", &sample, &test))
		return NULL;
	index = rk_shift(test, sample);
	if(index < 0)
		return Py_False;

	return Py_BuildValue("i", index);
}

static PyMethodDef RKMethods[] = {
    {"rabin_karp", rabin_karp, METH_VARARGS,
	    "Search for string in text using rabin-karp algorithm."},
    {"rabin_karp_shift", rabin_karp_shift, METH_VARARGS,
	    "Search for string in text using rabin-karp algorithm. Shift Optimized"},
    {NULL, NULL, 0, NULL} 
};

static struct PyModuleDef RKModule = {
	PyModuleDef_HEAD_INIT,
	"rabin_karp",
	"Rabin-karp algorithm",
	-1,
	RKMethods
};

/* Module initialization */
PyMODINIT_FUNC PyInit_rabin_karp(void)
{
    return PyModule_Create(&RKModule);
}
