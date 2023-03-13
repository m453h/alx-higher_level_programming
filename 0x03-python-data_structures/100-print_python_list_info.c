#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints python list basic information
 * @py: The python object to print details about
 **/
void print_python_list_info(PyObject *py)
{
	long int size = PyList_Size(py);
	int i;
	PyListObject *obj = (PyListObject *)py;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);

}
