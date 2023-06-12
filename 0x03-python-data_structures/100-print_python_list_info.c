#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	int size_of_list = PyList_Size(p);
	int allocated = ((PyListObject *)p)->allocated;
	int i;

	printf("[*] Size of the Python List = %d\n", size_of_list);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size_of_list; i++)
	{
		PyObject *element = PyList_GetItem(p, i);
		const char *element_type = element->ob_type->tp_name;
		printf("Element %d: %s\n", i, element_type);
	}
}
