# main.py
from Carrinho import Carrinho
# Importamos a nova classe controladora
from menu import Menu


def listar_produtos(produtos):
    print("\n--- Produtos Disponíveis ---")
    for i, p in enumerate(produtos, start=1):
        print(f"{i}. {p.nmProduto} - R$ {p.vlUnitario:.2f}")

def mostrar_carrinho(carrinho: Carrinho):
    print("\n--- Carrinho ---")
    if not carrinho.produtos:
        print("Vazio.")
        return

    for p in carrinho.produtos:
        print(f"- {p.nmProduto}: R$ {p.vlUnitario:.2f}")

    total_bruto = carrinho._calcular_total_bruto()
    total_final = carrinho.calcularTotalFinal()

    print(f"\nTotal Bruto: R$ {total_bruto:.2f}")
    if carrinho.promocaoAtiva:
        desconto = total_bruto - total_final
        print(f"Desconto Aplicado: - R$ {desconto:.2f}")
    print(f"Total Final: R$ {total_final:.2f}")

def menu_cadastrar_promocao(menu: Menu):
    print("\n--- Cadastrar Promoção ---")
    print("1. Black Friday (50% off)")
    print("2. Desconto Fixo (R$ 10,00 off)")

    tipo = input("Tipo: ")
    cupom = input("Código do cupom (ex: BF50, OFF10): ").upper()

    sucesso = menu.cadastrar_promocao(tipo, cupom)
    if sucesso:
        print(f"Promoção cupom '{cupom}' cadastrada com sucesso.")
    else:
        print("Tipo de promoção inválido.")

def menu_realizar_compra(sistema: Menu):
    carrinho = Carrinho()

    while True:
        print("\n--- Nova Compra ---")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Aplicar Cupom")
        print("4. Ver Carrinho")
        print("5. Finalizar Pedido")
        print("6. Voltar")

        op = input("Opção: ")

        if op == "1":
            listar_produtos(sistema.produtos_disponiveis)
            try:
                idx = int(input("Escolha o nº do produto (0 cancela): "))
                if idx == 0: continue
                # Pede ao sistema o produto pelo índice
                prod = sistema.get_produto_por_indice(idx - 1)
                if prod:
                    carrinho.adicionarProduto(prod)
                else:
                    print("Produto inválido.")
            except ValueError:
                print("Entrada inválida.")

        elif op == "2":
            if carrinho.produtos:
                removido = carrinho.produtos[0]
                carrinho.removerProduto(removido)
                print(f"{removido.nmProduto} removido.")
            else:
                print("Carrinho vazio.")

        elif op == "3":
            cupom_codigo = input("Cupom: ").upper()
            estrategia = sistema.buscar_cupom(cupom_codigo)
            carrinho.setPromocao(estrategia)
            if estrategia:
                print("Cupom aplicado.")
            else:
                print("Cupom inválido ou não encontrado.")

        elif op == "4":
            mostrar_carrinho(carrinho)

        elif op == "5":
            pedido_gerado = sistema.finalizar_pedido(carrinho)
            if pedido_gerado:
                 print(f"\n>>> Pedido {pedido_gerado.nrPedido} finalizado com sucesso! <<<")
                 break 
            else:
                 print("Não é possível finalizar carrinho vazio.")

        elif op == "6":
            break
        else:
            print("Opção inválida.")

def menu_ver_pedidos(sistema: Menu):
    print("\n--- Histórico de Pedidos ---")
    if not sistema.historico_pedidos:
        print("Nenhum pedido ainda.")
        return

    for p in sistema.historico_pedidos:
        print("================================")
        print(p)
        print("Itens:")
        for item in p.produtos:
            print(f" - {item.nmProduto} (R$ {item.vlUnitario:.2f})")


def main():
    sistema = Menu()

    while True:
        print("\n=== SISTEMA DE VAREJO ===")
        print(f"Cliente Logado: {sistema.cliente_atual.nmCliente}")
        print("1. Cadastrar Promoção (Cupom)")
        print("2. Nova Compra")
        print("3. Ver Histórico de Pedidos")
        print("4. Sair")

        op = input("Opção: ")
        if op == "1":
            menu_cadastrar_promocao(sistema)
        elif op == "2":
            menu_realizar_compra(sistema)
        elif op == "3":
            menu_ver_pedidos(sistema)
        elif op == "4":
            print("Saindo...")
            break
        else:
            print("Inválido.")

if __name__ == "__main__":
    main()