#include <kvs.h>
#include <python2.6/Python.h>
/*value的长度必须小于8K*/
#define KVS_BUFFER (8 * 1024)

static char buffer[KVS_BUFFER];

static PyObject*
wrap_kv_init(PyObject *self, PyObject *args)
{
	KVS_ENV kvs;
	int init_type, ret;
	if(!PyArg_ParseTuple(args, "nsssnnn", &init_type, &kvs.disk_file_path, 
		&kvs.IMAGE_file_path, &kvs.log_file_path, &kvs.buffer_sleep_time, 
		&kvs.buffer_horizon_size, &kvs.buffer_size))
		return NULL;
	kvs.init_type = (init_type == 0) ? INIT_TYPE_LOAD : INIT_TYPE_CREATE;
	/*printf("%d %s %s %s %d %d %d", init_type, kvs.disk_file_path, 
		kvs.IMAGE_file_path, kvs.log_file_path, kvs.buffer_sleep_time, 
		kvs.buffer_horizon_size, kvs.buffer_size);*/
	ret = kv_init(&kvs);
	return Py_BuildValue("i", ret);
}

static PyObject* 
wrap_kv_put(PyObject *self, PyObject *args)
{
	const char *key, *value;
	int key_size, value_size;
	int ret;
	if(!PyArg_ParseTuple(args, "s#s#", &key, &key_size, &value, &value_size))
		return NULL;
	//printf("%s %d %s %d\n", key, key_size, value, value_size);
	ret = kv_put(key, key_size, value, value_size);
	return Py_BuildValue("i", ret);
}

static PyObject*
wrap_kvs_get(PyObject *self, PyObject *args)
{
	const char *key;
	int key_size, ret, value_size = KVS_BUFFER;
	if(!PyArg_ParseTuple(args, "s#", &key, &key_size))
		return NULL;
	ret = kv_get(key, key_size, (char*)buffer, &value_size);
	if(ret == 0)
		return PyString_FromString(buffer);
	else
		Py_RETURN_NONE;
}

static PyObject*
wrap_kvs_delete(PyObject *self, PyObject *args)
{
	const char *key;
	int key_size, ret;
	if(!PyArg_ParseTuple(args, "s#", &key, &key_size))
		return NULL;
	ret = kv_delete(key, key_size);
	return PyInt_FromLong(ret);
}

static PyObject*
wrap_kvs_exit(PyObject *self, PyObject *args)
{
	int ret = kv_exit();
	return PyInt_FromLong(ret);
}



static PyMethodDef kvsMethods[] = 
{
	{"kvs_init", wrap_kv_init, METH_VARARGS, "kvs init"},
	{"kvs_put", wrap_kv_put, METH_VARARGS, "kvs put key-value"},
	{"kvs_get", wrap_kvs_get, METH_VARARGS, "kvs get value"},
	{"kvs_delete", wrap_kvs_delete, METH_VARARGS, "delete key-value"},
	{"kvs_exit", wrap_kvs_exit, METH_VARARGS, "Exit kvs"},
	{NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initKVS(void)
{
	Py_InitModule("KVS", kvsMethods);
}
