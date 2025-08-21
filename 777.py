# Importação das bibliotecas necessárias do Kivy
from kivy.app import App  # Classe base para criar aplicativos Kivy
from kivy.uix.boxlayout import BoxLayout  # Layout para organizar widgets em caixa
from kivy.uix.label import Label  # Widget para exibir texto
from kivy.uix.textinput import TextInput  # Campo de entrada de texto
from kivy.uix.button import Button  # Botão clicável
from kivy.core.window import Window  # Para configurar propriedades da janela

# Classe principal que herda de BoxLayout (organiza os widgets verticalmente)
class MeuApp(BoxLayout):
    def __init__(self, **kwargs):
        # Chama o construtor da classe pai (BoxLayout)
        super().__init__(**kwargs)
        
        # Configuração do layout principal
        self.orientation = 'vertical'  # Organiza os widgets verticalmente
        self.spacing = 15  # Espaço de 15 pixels entre os widgets
        self.padding = 40  # Espaço interno de 40 pixels nas bordas
        Window.clearcolor = (0.95, 0.95, 0.95, 1)  # Define cor de fundo (cinza claro)
        
        # Título do aplicativo (Label estilizado)
        titulo = Label(
            text="App de Boas-Vindas",  # Texto do título
            font_size='24sp',  # Tamanho da fonte (24 scale-independent pixels)
            bold=True,  # Texto em negrito
            color=(0.2, 0.4, 0.6, 1),  # Cor do texto (azul)
            size_hint=(1, 0.3)  # Ocupa 100% da largura e 30% da altura disponível
        )
        self.add_widget(titulo)  # Adiciona o título ao layout
        
        # Campo de texto para digitar o nome
        self.text_input = TextInput(
            hint_text="Digite seu nome aqui...",  # Texto de placeholder
            size_hint=(1, 0.2),  # Ocupa 100% da largura e 20% da altura
            font_size='18sp',  # Tamanho da fonte
            multiline=False,  # Permite apenas uma linha de texto
            padding=[15, 10],  # Espaço interno (15px horizontal, 10px vertical)
            background_color=(1, 1, 1, 1)  # Cor de fundo branca
        )
        self.add_widget(self.text_input)  # Adiciona o campo de texto ao layout
        
        # Botão Enviar estilizado
        self.botao = Button(
            text="Enviar",  # Texto do botão
            size_hint=(1, 0.2),  # Ocupa 100% da largura e 20% da altura
            font_size='20sp',  # Tamanho da fonte
            bold=True,  # Texto em negrito
            background_color=(0.2, 0.6, 0.8, 1),  # Cor de fundo azul (RGBA)
            color=(1, 1, 1, 1)  # Cor do texto branco
        )
        # Conecta o evento de clique do botão à função enviar_nome
        self.botao.bind(on_press=self.enviar_nome)
        self.add_widget(self.botao)  # Adiciona o botão ao layout
        
        # Label para mostrar as mensagens de boas-vindas ou erro
        self.mensagem = Label(
            text="",  # Texto inicial vazio
            font_size='18sp',  # Tamanho da fonte
            size_hint=(1, 0.3),  # Ocupa 100% da largura e 30% da altura
            color=(0.3, 0.3, 0.3, 1),  # Cor do texto (cinza)
            halign='center',  # Alinhamento horizontal centralizado
            valign='middle'   # Alinhamento vertical centralizado
        )
        # Necessário para o alinhamento funcionar corretamente
        self.mensagem.bind(size=self.mensagem.setter('text_size'))
        self.add_widget(self.mensagem)  # Adiciona o label de mensagem ao layout
    
    # Função chamada quando o botão é pressionado
    def enviar_nome(self, instance):
        # Obtém o texto do campo e remove espaços em branco do início e fim
        nome = self.text_input.text.strip()
        
        # Verifica se o campo não está vazio
        if nome:
            # Se há nome, exibe mensagem de boas-vindas
            self.mensagem.text = f"Bem-vindo(a), {nome}!"
            self.mensagem.color = (0, 0.5, 0, 1)  # Muda cor para verde (sucesso)
        else:
            # Se está vazio, exibe mensagem de erro
            self.mensagem.text = "Por favor, digite seu nome."
            self.mensagem.color = (0.8, 0, 0, 1)  # Muda cor para vermelho (erro)

# Classe do aplicativo que herda de App
class BoasVindasApp(App):
    # Método obrigatório que constrói a interface
    def build(self):
        return MeuApp()  # Retorna uma instância da nossa interface

# Ponto de entrada do programa
if __name__ == '__main__':
    # Cria e executa a aplicação
    BoasVindasApp().run()