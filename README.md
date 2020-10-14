# Reusable GUI Components - ScrollBox, DataListBox

- Responsive pair of reusable GUI components made with the Python
 binding of Tkinter
 
- Allows visual dataset interrogation
 
Environment Setup:

- Python 3

## Overview
- `ScrollBox`: inherits from `tkinter`s `ListBox` to conveniently combine a
 `ListBox` and a `ScrollBar` together into a single component.
- `DataListBox`: inherits from `ScrollBox` to make it capable of loading its own
 data and, optionally, linking to another `DataListBox` or tkinter `Label`
- Demo'ed with SQite3 using the Python `sqlite` module.

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
