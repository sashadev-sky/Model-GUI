import os
import sqlite3
import tkinter


class ScrollBox(tkinter.Listbox):
    """Class to represent a Tkinter ListBox with a built-in Scrollbar."""

    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(
            window,
            orient=tkinter.VERTICAL,
            command=self.yview
        )

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1,
             **kwargs):
        super().grid(
            row=row,
            column=column,
            sticky=sticky,
            rowspan=rowspan,
            columnspan=columnspan,
            **kwargs
        )
        self.scrollbar.grid(
            row=row,
            column=column,
            sticky='nse',
            rowspan=rowspan
        )
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(ScrollBox):
    """Class to represent a ScrollBox that loads in its own data and is
    capable of linking to another DataListBox or Tkinter Label.

    If linked to another DataListBox, a selection inside a DataListBox
    triggers data loading in the linked DataListBox.
    """

    def __init__(self, window, connection, table, field, sort_order=(),
                 **kwargs):
        """Constructs a DataListBox widget with the parent `window`.

        :param tkinter.Tk window: The root window instance
        :param sqlite3.Connection connection: The database connection instance
        :param str table: The table to load the data from
        :param str field: The table field to display the data from
        :param tuple sort_order: 1+ fields to sort the displayed data by
            (default is ())
        :return: None
        """
        super().__init__(window, **kwargs)

        self.linked_box = None
        self.linked_result = None
        self.link_field = None
        self.link_value = None
        self.result_fields = None

        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.bind('<<ListboxSelect>>', self.on_select)

        self.sql_select = f'SELECT {self.field}, _id FROM {self.table}'

        if sort_order:
            self.sql_sort = f'ORDER BY {",".join(sort_order)}'
        else:
            self.sql_sort = f'ORDER BY {self.field}'

    def clear(self):
        """Deletes all items in the DataListBox.

        :return: None
        """
        self.delete(0, tkinter.END)

    def link(self, widget, link_field):
        """Creates an association to another DataListBox on the specified
        foreign key field.

        :param DataListBox widget: widget to link to
        :param str link_field: field to link on
        :return: None
        """
        self.linked_box = widget
        widget.link_field = link_field

    def link_result(self, text_var, result_fields='*'):
        """Links a DataListBox to a Tkinter Label that will display the values
        of the underlying table's passed fields inside a separate box.

        :param text_var: the 'textvariable' attribute of a tkinter Label
        :type text_var: tkinter.StringVar
        :param tuple result_fields: the fields to display values for.
            (default is all fields)
        :return: None
        """
        self.linked_result = text_var
        self.result_fields = result_fields

    def re_query(self, link_value=None):
        """Refreshes the data in a DataListBox, clear any sub-selections
        from a linked DataListBox (if applicable), and clear any displayed
        result values (if applicable).

        :param int link_value: the id of the foreign key association
            (default is None)
        :return: None
        """
        self.link_value = link_value
        if link_value and self.link_field:
            sql = f'{self.sql_select} WHERE {self.link_field}=? {self.sql_sort}'
            self.cursor.execute(sql, (link_value,))
        else:
            self.cursor.execute(f'{self.sql_select} {self.sql_sort}')

        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

        if self.linked_box:
            self.linked_box.clear()

        if self.linked_result:
            self.linked_result.set('')

    def on_select(self, event):
        """Runs when a DataListBox `<<ListboxSelect>>` event is
        triggered, which is inherited from Tkinter\'s Listbox.

        :return: None
        """
        if self.curselection():
            index = self.curselection()[0]
            value = self.get(index),

            if self.link_value:
                value = value[0], self.link_value
                sql_where = f'WHERE {self.field}=? AND {self.link_field}=?'
                print(f'{self.sql_select} WHERE {self.field}={value[0]} AND'
                      f' {self.link_field}={self.link_value}')
            else:
                sql_where = f'WHERE {self.field}=?'
                print(f'{self.sql_select} WHERE {self.field}={value[0]}')

            link = self.cursor.execute(f'{self.sql_select} {sql_where}',
                                       value).fetchone()
            link_id = link[1]

            if self.linked_box:
                self.linked_box.re_query(link_id)

            if self.linked_result:
                fields_to_select = ",".join(self.result_fields)
                record = self.cursor.execute(
                    f'SELECT {fields_to_select} FROM {self.table} WHERE'
                    f' {self.field}=? AND {self.link_field}=?', value
                ).fetchone()
                self.linked_result.set(f'{record}')


if __name__ == '__main__':

    os.system('cat import_db.sql | sqlite3 painting.db')

    conn = sqlite3.connect('painting.db')

    root = tkinter.Tk()
    root.title('Painting DB Browser')
    root.geometry('1024x768')

    root.columnconfigure(0, weight=2)  # box 1
    root.columnconfigure(1, weight=2)  # box 2
    root.columnconfigure(2, weight=2)  # box 3
    root.columnconfigure(3, weight=1)  # spacer column on right

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=5)
    root.rowconfigure(2, weight=5)
    root.rowconfigure(3, weight=1)

    # ===== labels =====
    tkinter.Label(root, text='Painters').grid(row=0, column=0)
    tkinter.Label(root, text='Paintings').grid(row=0, column=1)
    tkinter.Label(root, text='Painting').grid(row=0, column=2)

    # ===== Painters Listbox =====
    painter_list = DataListBox(root, conn, 'painters', 'name')
    painter_list.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
    painter_list.config(border=2, relief='sunken')

    painter_list.re_query()

    # ===== Paintings Listbox =====
    painting_list = DataListBox(root, conn, 'paintings', 'title',
                                sort_order=('title',))
    painting_list.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
    painting_list.config(border=2, relief='sunken')

    painter_list.link(painting_list, 'painter_id')

    # ===== Painting Result =====
    result_text = tkinter.StringVar()
    result = tkinter.Label(root, textvariable=result_text)
    result.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
    result.config(border=2, relief='sunken')

    painting_list.link_result(result_text, ('title', 'year'))

# ===== Main loop =====
root.mainloop()
print('closing database connection')
conn.close()
