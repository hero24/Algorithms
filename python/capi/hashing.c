#include <Python.h>
#include "../../c/hashing.h"

PyObject* SM2(PyObject* self, PyObject* args)
{
	char* str;
	int hash;
	if(!PyArg_ParseTuple(args, "s", &str))
		return NULL;
	index = sum_modulo_2(str);
	if(index < 0)
		return Py_False;
	return Py_BuildValue("i", index);
}

PyObject* SM2RS(PyObject* self, PyObject* args)
{
	char* str;
	int hash;
	if(!PyArg_ParseTuple(args, "s", &str))
		return NULL;
	index = sum_modulo_2_rshift(str);
	if(index < 0)
		return Py_False;
	return Py_BuildValue("i", index);
}

PyObject* Rmax(PyObject* self, PyObject* args)
{
	char* str;
    int rmax;
	int hash;
	if(!PyArg_ParseTuple(args, "si", &str, &rmax))
		return NULL;
	index = Rmax(str, rmax);
	if(index < 0)
		return Py_False;
	return Py_BuildValue("i", index);
}

PyObject* DJB2(PyObject* self, PyObject* args)
{
	char* str;
	unsigned long hash;
	if(!PyArg_ParseTuple(args, "s", &str))
		return NULL;
	index = djb2(str);
	if(index < 0)
		return Py_False;
	return Py_BuildValue("K", index);
}

PyObject* SDBM(PyObject* self, PyObject* args)
{
	char* str;
	unsigned long hash;
	if(!PyArg_ParseTuple(args, "s", &str))
		return NULL;
	index = sdbm_hash(str);
	if(index < 0)
		return Py_False;
	return Py_BuildValue("K", index);
}

PyObject* KNR(PyObject* self, PyObject* args)
{
	char* str;
	unsigned long hash;
	if(!PyArg_ParseTuple(args, "s", &str))
		return NULL;
	index = k_n_r(str);
	if(index < 0)
		return Py_False;
	return Py_BuildValue("K", index);
}

static PyMethodDef HMeth[] = {
	{"SM2", SM2, METH_VARARGS, "sum modulo hashing"},
    {"SM2RS", SM2RS, METH_VARARGS, "sum modulo hashing right shift"},
    {"Rmax", Rmax, METH_VARARGS, "Rmax hashing"},
    {"DJB2", DJB2, METH_VARARGS, "djb2 hashing"},
    {"SDBM", SDBM, METH_VARARGS, "sdbm hashing"},
    {"KNR", KNR, METH_VARARGS, "knr hashing"},
	{NULL, NULL, 0, NULL}	
};

static struct PyModuleDef HMod = {
	PyModuleDef_HEAD_INIT,
	"hashing",
	"string hashing functions",
	-1,
	HMeth
};

PyMODINIT_FUNC PyInit_boyer_moore(void)
{
	return PyModule_Create(&HMod);
}
