#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints basic info about Python lists.
 * @p: the PyObject list object to print basic info about.
 * Return (void)
 */
void print_python_list(PyObject *p)
{
	int size, allocated, i;
	const char *ob_type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	allocated = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);
	for (i = 0; i < size; i++)
	{
		ob_type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, ob_type);
		if (strcmp(ob_type, "bytes") == 0)
		{
			print_python_bytes(list->ob_item[i]);
		}
	}
}

/**
 * print_python_bytes - prints basic info about Python byte objects.
 * @p: the PyObject byte object to print basic info.
 * Return (void)
 */
void print_python_bytes(PyObject *p)
{
	unsigned char i, ob_size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
	{
		ob_size = 10;
	}
	else
	{
		ob_size = ((PyVarObject *)p)->ob_size + 1;
	}

	printf("  first %d bytes: ", ob_size);

	for (i = 0; i < ob_size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (ob_size - 1))
		{
			printf("\n");
		}
		else
		{
			printf(" ");
		}
	}
}
