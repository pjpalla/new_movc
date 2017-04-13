__author__ = 'pg'

# from tkinter import *
# from tkinter import ttk
#
#
# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
#     except ValueError:
#         pass
#
# root = Tk()
# root.title("Movc Generator")
# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# mainframe.columnconfigure(0, weight=1)
# mainframe.rowconfigure(0, weight=1)
#
# feet = StringVar()
# meters = StringVar()
# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
#
# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
#
# for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
# feet_entry.focus()
# root.bind('<Return>', calculate)
#
# root.mainloop()

# import tkinter as tk
#
#
# class ExampleApp(tk.Frame):
#     ''' An example application for TkInter.  Instantiate
#         and call the run method to run. '''
#
#     def __init__(self, master):
#         # Initialize window using the parent's constructor
#         tk.Frame.__init__(self,
#                           master,
#                           width=400,
#                           height=500)
#         # Set the title
#         self.master.title('New MOVC Generator')
#
#         # This allows the size specification to take effect
#         self.pack_propagate(0)
#
#         # We'll use the flexible pack layout manager
#         self.pack()
#
#         # The greeting selector
#         # Use a StringVar to access the selector's value
#         self.greeting_var = tk.StringVar()
#         self.greeting = tk.OptionMenu(self,
#                                       self.greeting_var,
#                                       'hello',
#                                       'goodbye',
#                                       'heyo')
#         self.greeting_var.set('hello')
#
#         # The recipient text entry control and its StringVar
#         self.recipient_var = tk.StringVar()
#         self.recipient = tk.Entry(self,
#                                   textvariable=self.recipient_var)
#         self.recipient_var.set('world')
#
#         # The go button
#         self.go_button = tk.Button(self,
#                                    text='Go',
#                                    command=self.print_out)
#
#         # Put the controls on the form
#         self.go_button.pack(fill=tk.X, side=tk.BOTTOM)
#         self.greeting.pack(fill=tk.X, side=tk.TOP)
#         self.recipient.pack(fill=tk.X, side=tk.TOP)
#
#     def print_out(self):
#         ''' Print a greeting constructed
#             from the selections made by
#             the user. '''
#         print('%s, %s!' % (self.greeting_var.get().title(),
#                            self.recipient_var.get()))
#
#     def run(self):
#         ''' Run the app '''
#         self.mainloop()
#
#
# app = ExampleApp(tk.Tk())
# app.run()
# import tkinter
#
# class MovGUI(tkinter.Tkinter.tk):
#
#     def __init__(self, parent):
#         tkinter.Tkinter.tk.__init__(self, parent)
#         self.parent = parent
#         self.initialize()
#
#
#     def initialize(self):
#         pass
#
#
#
#
#     if __name__ == "__main__":
#         pass
#         # app = MovGUI(None)
#         # app.title = "MOVC "
