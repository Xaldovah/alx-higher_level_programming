#include "/usr/include/python3.4/Python.h"
#include <stdion.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size;
    PyObject *item;
    size = PyList_Size(p);
    printf("list size: %zd\n", size);
    for (int i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("item %d: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
void print_python_bytes(PyObject *p) {
    Py_ssize_t size;
    const char *bytes;
    size = PyBytes_GET_SIZE(p);
    bytes = PyBytes_AS_STRING(p);
    printf("bytes size: %zd\n", size);
    printf("first 10 bytes: %.10s\n", bytes);
}
