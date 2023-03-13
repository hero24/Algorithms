#include <Python.h>
#include "../../c/searching/kmp.h"

PyObject* knuth_morris_pratt(PyObject* self, PyObject* args)
{
	char* sample;
	char* test;
	int index;
	if(!PyArg_ParseTuple(args, "ss", &sample, &test))
		return NULL;
	index = kmp(test, sample);
	if(index < 0)
		return Py_False;
	return Py_BuildValue("i", index);
}

static PyMethodDef KMPMeth[] = {
	{"knuth_morris_pratt", knuth_morris_pratt, METH_VARARGS,
	       "Search for text in string using knuth-morris-pratt algorithm"},
	{NULL, NULL, 0, NULL}	
};

static struct PyModuleDef KMPMod = {
	PyModuleDef_HEAD_INIT,
	"knuth_morris_pratt",
	"Kunth-Morris-Pratt algorithm",
	-1,
	KMPMeth
};

PyMODINIT_FUNC PyInit_knuth_morris_pratt(void)
{
	return PyModule_Create(&KMPMod);
}
