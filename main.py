import flet as ft
from custom_checkbox import Checkbox

def main(page: ft.Page):
    page.title = "Bem vindo ao app do Café com Palmer" #titulo'
    page.window.width = 500 #tamanho da largura
    page.window.height = 650 #tamanho da altura
    page.padding = ft.padding.only(left=10, right=10, top=10, bottom=20) #espaçamento
    page.theme_mode = ft.ThemeMode.LIGHT
    def add_task(e):
        print(f'\033[33m {new_task.value}\033[0m')
        task_list.controls.append(Checkbox(text=new_task.value))
        #task_list.controls.append(ft.Checkbox(label=new_task.value))
        new_task.value = '' #limpar o campo depois de dar input
        page.update()
        
    #new_title = ft.Text(value='Bem vindo ao app do Café com Palmer') #titulo
    new_task = ft.TextField(hint_text='Insira uma tarefa...', expand=True) #campo digitação
    new_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_task) #botão inferior para adicionar
    
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