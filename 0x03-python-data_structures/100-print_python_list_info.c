#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
    int a = 0, len_of_list = 0;
    PyObject *elemens;
    PyListObject *clone = (PyListObject *) p;

    len_of_list = Py_SIZE(p);
    printf("[*] Size of the Python List = %d\n", len_of_list);
    printf("[*] Allocated = %d\n", (int) clone->allocated);

    for (; a < len_of_list; ++a)
    {
        elemens = PyList_GET_ITEM(p, a);
        printf("Element %d: %s\n", a, elemens->ob_type->tp_name);
    }

    return;
}
