from flask import Flask, render_template

# Inicialização padrão compatível com Python 3.11
app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def home() -> str:
    # O retorno tipado como string ajuda na leitura e IDEs modernos
    return render_template('quiz.html')

# Handler necessário para Vercel Serverless
# Em ambientes serverless, o 'app' é importado diretamente, 
# mas o bloco abaixo ajuda se você rodar localmente (python api/index.py)
if __name__ == '__main__':
    app.run(debug=True)