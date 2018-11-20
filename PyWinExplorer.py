from pywinauto import Desktop, Application
Application().start('explorer.exe "C:\\Program Files"')


app = Application(backend="uia").connect(path="explorer.exe", title="Program Files")
app.ProgramFiles.set_focus()
common_files = app.ProgramFiles.ItemsView.get_item('Java')
common_files.right_click_input()
app.ContextMenu.Properties.invoke()

Properties = Desktop(backend='uia').Java_Properties
Properties.print_control_identifiers()
Properties.Cancel.click()
Properties.wait_not('visible')