import requests
from bs4 import BeautifulSoup

def extrair_livros(url):
    resposta = requests.get(url)
    if resposta.status_code != 200:
        print("Erro ao acessar o site.")
        return

    soup = BeautifulSoup(resposta.text, 'html.parser')
    livros = soup.select('article.product_pod')

    for livro in livros:
        titulo = livro.h3.a['title']
        preco = livro.select_one('.price_color').text
        disponibilidade = livro.select_one('.availability').text.strip()

        print(f"📘 {titulo}")
        print(f"💰 Preço: {preco}")
        print(f"📦 Disponibilidade: {disponibilidade}")
        print("-" * 40)

if __name__ == "__main__":
    URL = "https://books.toscrape.com/catalogue/page-1.html"
    extrair_livros(URL)
