import flet as ft

def main(page: ft.Page):
    page.title = "Youtube downloader"
    page.window_width = 900
    page.window_height = 500
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # ----- Lado Esquerdo -----
    left_side = ft.Container(
        bgcolor="#5e2129",
        expand=3,
        content=ft.Column(
            [
                        ft.Column(
                            [
                                ft.Text(
                                    "Youtube Downloader",
                                    size=50,
                                    weight="bold",
                                    color="white",
                                    text_align="center",
                                )
                            ]
                        ),

                        ft.Column(
                            [
                                ft.Text(
                                    "Baixe seus vídeos com mais facilidade com nossa ferramenta!",
                                    color="white",
                                    size=16,
                                    text_align="center",
                                )
                            ]
                        ),

                        ft.Column(
                            [
                                ft.Text("By: Jean Luca 🧑‍💻",
                                        weight="bold",
                                        color="white"),
                            ]
                        )
                    ],
                    alignment="center",
                    horizontal_alignment="center",
                    spacing=15
            ),
        padding=30,
        border_radius=ft.border_radius.all(10)
    )

    # ----- Lado Direito (Cadastro) -----
    right_side = ft.Container(
        bgcolor="#000000",
        expand=7,
        content=ft.Column(
            [
                # Bloco 1: Link + botão
                ft.Column(
                    [
                        ft.TextField(label="Digite o link:", border_color="#5e2129"),
                        ft.ElevatedButton(
                            "DOWNLOAD",
                            bgcolor="#5e2129",
                            color="white",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=5)
                            )
                        ),
                    ],
                    spacing=20,
                    alignment="start",
                    horizontal_alignment="start"
                ),


                # Bloco 2: Provai e Vede
                ft.Column(
                    [
                        ft.Text(
                            "Download do Provai Vede",
                            size=20,
                            weight="bold",
                            color="white"),

                        ft.ElevatedButton(
                            "DOWNLOAD",
                            bgcolor="#5e2129",
                            color="white",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=5)
                            )
                        )
                    ],
                    spacing=20,
                    alignment="start",  # Alinha à esquerda
                    horizontal_alignment="start"
                ),

                # Bloco 3: Informativo Mundial
                ft.Column(
                    [
                        ft.Text(
                            "Download do Informativo Mundial das Missões",
                            size=20,
                            weight="bold",
                            color="white"),

                        ft.ElevatedButton(
                            "DOWNLOAD",
                            bgcolor="#5e2129",
                            color="white",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=5)
                                )
                        )
                    ],
                    spacing=20,
                    alignment="start",  # Alinha à esquerda
                    horizontal_alignment="start"
                ),
            ],
            spacing=55  # espaço entre os blocos
        ),
        padding=145,
        border_radius=ft.border_radius.all(10)
    )

    # ----- Row principal (Divide a tela em 2 partes) -----
    layout = ft.Row(
        [
                    left_side,
                    right_side
                ],
        expand=True,
        spacing=0
    )

    page.add(layout)


ft.app(target=main)
