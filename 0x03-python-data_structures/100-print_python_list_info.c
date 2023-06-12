#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>

void print_python_list_info(PyObject *p) {
    Py_ssize_t size;
    int i;
    size = PyList_Size(p);
    printf("Size of the Python list: %zd\n", size);
    for (i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
