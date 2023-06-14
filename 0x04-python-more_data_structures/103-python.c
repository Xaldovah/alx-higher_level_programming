#include "/usr/include/python3.4/Python.h"
#include <stdio.h>

void print_hexn(const char *str, int n)
{
	int i = 0;

	for (; i < n - 1; ++i)
		printf("%02x ", (unsigned char) str[i]);

	printf("%02x", str[i]);
}

void print_python_bytes(PyObject *p)
{
	PyBytesObject *copy = (PyBytesObject *) p;
	int calculate_bytes, copy_size = 0;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(copy))
	{
		copy_size = PyBytes_Size(p);
		calculate_bytes = copy_size + 1;

		if (calculate_bytes >= 10)
			calculate_bytes = 10;

		printf("  size: %d\n", copy_size);
		printf("  trying string: %s\n", copy->ob_sval);
		printf("  first %d bytes: ", calculate_bytes);
		print_hexn(clone->ob_sval, calculate_bytes);
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

void print_python_list(PyObject *p)
{
	int i = 0, len_of_list = 0;
	PyObject *item;
	PyListObject *copy = (PyListObject *) p;

	printf("[*] Python list info\n");
	len_of_list = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %d\n", len_of_list);
	printf("[*] Allocated = %d\n", (int) copy->allocated);

	for (; i < len_of_list; ++i)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
