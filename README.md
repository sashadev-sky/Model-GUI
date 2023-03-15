# GUI Components

- A responsive pair of reusable GUI components made with Tkinter, the Python
 binding to the Tk GUI toolkit

- Allows visual dataset interrogation

- Demonstrated with SQLite3

Environment Setup

- Python 3
- SQLite3
- Tkinter

### ScrollBox

- `ScrollBox` inherits from Tkinter\'s `ListBox` to conveniently combine a
 `ListBox` and a `ScrollBar` together into a single component.

### DataListBox

- `DataListBox` inherits from `ScrollBox` to make it capable of loading its own
 data and, optionally, linking to another `DataListBox` or Tkinter `Label`.

## Run the demo

From the root directory, Ubuntu, Linux and Mac users:

```shell
python3 project/db_connection.py
```

From the root directory, Windows users:

```shell
python --version  # ensure at least 3.x.x
python project/db_connection.py
```

---

#### SQLite / Python Concepts (personal use)

---

- **SQLite** is not client-server. The database server is not
 running on a remote machine that you connect to; instead everything is
 running on the same machine.
  - `_id INTEGER PRIMARY KEY`: some Java classes that
   Android uses to handle databases actually require an `_id` column (as
   opposed to `id`) so it's a good habit to get into to use that name for
    Python also.

- **Docstring**
  > A docstring is a string literal that occurs as the first
   statement in a module, function, class, or method definition. Such a docstring becomes the `__doc__` special attribute of that object.

  - Python has the built-in function `help()` that prints out the objects
   docstring to the console.
    - How is this output generated?
      1. Via the `__doc__` property.
      2. The strategic placement of the string literal directly below the
       object will automatically set the `__doc__` value.
  - **Type - Class Docstrings**
    - The docstrings are placed immediately following the class or class
     method indented by one level.
  - **Format - ReST (reStructuredText)**
    - <pre>
      :param &lt;param_type> &lt;param_name>: &lt;param_description>
      </pre>
      <pre>
      :param &lt;param_name>: &lt;param_description>
      :type &lt;param_name>: &lt;param_type>
      </pre>
    - <pre>
      :return: &lt;return_description>
      :rtype: &lt;return_type>
      </pre>
