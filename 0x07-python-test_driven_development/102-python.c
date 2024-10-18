#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject representing the string.
 */
void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	Py_ssize_t length = PyUnicode_GetLength(p);
	const char *type = PyUnicode_IS_COMPACT_ASCII(p) ?
					   "compact ascii" : "compact unicode object";

	PyObject *utf8_str = PyUnicode_AsUTF8String(p);

	if (utf8_str == NULL)
	{
		printf("  [ERROR] Could not convert to UTF-8\n");
		return;
	}

	const char *value = PyBytes_AsString(utf8_str);

	printf("  type: %s\n", type);
	printf("  length: %zd\n", length);
	printf("  value: %s\n", value);

	Py_DECREF(utf8_str);
}
