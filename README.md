# GUI Components

- A responsive pair of reusable GUI components made with the Python
 binding of Tkinter
 
- Allows visual dataset interrogation

- Demonstrated with SQLite3 using the Python `sqlite` module.
 
Environment Setup:

- Python 3

### ScrollBox
- `ScrollBox` inherits from `tkinter`s `ListBox` to conveniently combine a
 `ListBox` and a `ScrollBar` together into a single component.

### DataListBox
- `DataListBox` inherits from `ScrollBox` to make it capable of loading its own
 data and, optionally, linking to another `DataListBox` or tkinter `Label`.

## Run the demo
From the root directory, Ubuntu, Linux and Mac users:

```bash
$ python3 db_connection.py
```
From the root directory, Windows users:
```bash
$ python --version  # ensure at least 3.x.x
$ python db_connection.py
```

<hr>

#### Python Concepts (personal use)

<hr>

* **Docstring**
  <blockquote>A docstring is a string literal that occurs as the first
   statement in a module, function, class, or method definition. Such a
    docstring becomes the <code>__doc__</code> special attribute of that object
    .</blockquote>
 
  * Python has the built-in function `help()` that prints out the objects
   docstring to the console. 
    * How is this output generated? 
      1.  Via the `__doc__` property.
      2. The strategic placement of the string literal directly below the
       object will automatically set the `__doc__` value.
  * **Type - Class Docstrings**
    * The docstrings are placed immediately following the class or class
     method indented by one level.
  * **Format - ReST (reStructuredText) format**
    * <pre>
      :param &lt;param_type> &lt;param_name>: &lt;param_description>
      </pre>
      <pre>
      :param &lt;param_name>: &lt;param_description>
      :type &lt;param_name>: &lt;param_type>
      </pre>
    * <pre>
      :return: &lt;return_description>
      :rtype: &lt;return_type>
      </pre>

  

