import flet as ft

class Checkbox(ft.Row):
    def __init__(self, text):
        super().__init__()
        self.text_view = ft.Text(text)
        self.text_edit = ft.TextField(text, visible=False)
        self.edit_button = ft.IconButton(icon=ft.icons.EDIT, icon_color='yellow', on_click=self.edit)
        self.save_button = ft.IconButton(icon=ft.icons.SAVE, on_click=self.save, visible=False)
        self.delete_button = ft.IconButton(icon=ft.icons.DELETE, icon_color='red', on_click=self.delete)
        self.controls.extend([
                            ft.Checkbox(),
                            self.text_view,
                            self.text_edit,
                            self.edit_button,
                            self.save_button,
                            self.delete_button
        ])

        
    def edit(self, e):
        self.text_view.visible = False
        self.text_edit.visible = True
        self.edit_button.visible = False
        self.save_button.visible = True
        self.delete_button.visible = False
        self.update()
    
    def save(self, e):
        self.text_view.visible = True
        self.text_edit.visible = False
        self.edit_button.visible = True
        self.save_button.visible = False
        self.delete_button.visible = True
        if self.text_edit.value = "":
            return
        self.text_view.value = self.text_edit.value
        self.update()
    
    def delete(self, e):
        self.visible = False
        self.update()
        pass