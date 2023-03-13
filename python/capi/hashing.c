#include <Python.h>
#include "../../c/hashing.h"

PyObject* SM2(PyObject* self, PyObject* args)
{
	char* str;
	int hash;
	if(!PyArg_ParseTuple(args, "s", &str))
		return NULL;
	hash = sum_modulo_2(str);
	if(hash < 0)
		return Py_False;
	return Py_BuildValue("i", hash);
}

PyObject* SM2RS(PyObject* self, PyObject* args)
{
	char* str;
	int hash;
	if(!PyArg_ParseTuple(args, "s", &str))
		return NULL;
	hash = sum_modulo_2_rshift(str);
	if(hash < 0)
		return Py_False;
	return Py_BuildValue("i", hash);
}

PyObject* RMAX(PyObject* self, PyObject* args)
{
	char* str;
    int rmax;
	int hash;
	if(!PyArg_ParseTuple(args, "si", &str, &rmax))
		return NULL;
	hash = Rmax(str, rmax);
	if(hash < 0)
		return Py_False;
	return Py_BuildValue("i", hash);
}

PyObject* DJB2(PyObject* self, PyObject* args)
{
	char* str;
	unsigned long hash;
	if(!PyArg_ParseTuple(args, "s", &str))
		return NULL;
	hash = djb2(str);
	if(hash < 0)
		return Py_False;
	return Py_BuildValue("K", hash);
}

PyObject* SDBM(PyObject* self, PyObject* args)
{
	char* str;
	unsigned long hash;
	if(!PyArg_ParseTuple(args, "s", &str))
		return NULL;
	hash = sdbm_hash(str);
	if(hash < 0)
		return Py_False;
	return Py_BuildValue("K", hash);
}

PyObject* KNR(PyObject* self, PyObject* args)
{
	char* str;
	unsigned long hash;
	if(!PyArg_ParseTuple(args, "s", &str))
		return NULL;
	hash = k_n_r(str);
	if(hash < 0)
		return Py_False;
	return Py_BuildValue("K", hash);
}

static PyMethodDef HMeth[] = {
	{"SM2", SM2, METH_VARARGS, "sum modulo hashing"},
    {"SM2RS", SM2RS, METH_VARARGS, "sum modulo hashing right shift"},
    {"RMAX", RMAX, METH_VARARGS, "Rmax hashing"},
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

PyMODINIT_FUNC PyInit_hashing(void)
{
	return PyModule_Create(&HMod);
}
