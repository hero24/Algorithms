#include <Python.h>
#include "../../c/searching/bm.h"

PyObject* boyer_moore(PyObject* self, PyObject* args)
{
	char* sample;
	char* test;
	int index;
	if(!PyArg_ParseTuple(args, "ss", &sample, &test))
		return NULL;
	index = bm(test, sample);
	if(index < 0)
		return Py_False;
	return Py_BuildValue("i", index);
}

static PyMethodDef BMMeth[] = {
	{"boyer_moore", boyer_moore, METH_VARARGS,
	       "Search for text in string using Boyer-Moore algorithm"},
	{NULL, NULL, 0, NULL}	
};

static struct PyModuleDef BMMod = {
	PyModuleDef_HEAD_INIT,
	"boyer_moore",
	"Boyer-Moore algorithm",
	-1,
	BMMeth
};

PyMODINIT_FUNC PyInit_boyer_moore(void)
{
	return PyModule_Create(&BMMod);
}
