import flet as ft
from custom_checkbox import Checkbox

def main(page: ft.Page):
    page.title = "ToDo do Juds" #titulo'
    page.window.width = 450 #tamanho da largura
    page.window.height = 650 #tamanho da altura
    page.padding = ft.padding.only(left=10, right=10, top=10, bottom=20) #espaçamento
    page.theme_mode = ft.ThemeMode.DARK
    def add_task(e):
        if new_task.value != '':
            task_list.controls.append(Checkbox(text=new_task.value))
        new_task.value = '' #limpar o campo depois de dar input
        page.update()
        new_task.focus()
        
    #new_title = ft.Text(value='Bem vindo ao app do Café com Palmer') #titulo
    new_task = ft.TextField(hint_text='Insira uma tarefa...', expand=True) #campo digitação
    new_button = ft.FloatingActionButton(icon=ft.icons.ADD_CIRCLE_OUTLINE_SHARP, on_click=add_task, autofocus=True) #botão inferior para adicionar
    task_list = ft.Column()

    card = ft.Column(
        width=400,
                controls=[
                    ft.Row(
                        controls=[
                            new_task,
                            new_button
                        ]
                    )
                    ,task_list
                ],
            )
    
    
    
    page.add(
        card
       # new_task,
       # new_button
    )

ft.app(target=main)