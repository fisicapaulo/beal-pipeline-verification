# Verificação computacional de instâncias ligadas à Conjectura de Beal
Descrição
Pipeline reprodutível para checagens aritméticas relacionadas à Conjectura de Beal. Inclui normalização, congruências, LTE, pinça altura–radical e barreiras do tipo Zsigmondy, com logs, hashes e geração automática de tabelas.

Estado atual

Implementado:
src/check_identities.py: utilitários de altura (h_int) e checagem do bound h(a+b) ≤ max(h(a), h(b)) + log 2.
src/zsigmondy_check.py: fatoração primária e verificação de primos primitivos (estilo Zsigmondy) para a^k ± b^k.
Testes: todos passando localmente.
Instalação

Requisitos: Python 3.9+.
Recomenda-se criar um ambiente virtual (venv). Não há dependências externas por enquanto.
Uso rápido

Bound de altura:
from src.check_identities import verify_sum_bound_by_c
verify_sum_bound_by_c(a, b) -> bool
Primos primitivos (Zsigmondy-like):
from src.zsigmondy_check import has_primitive_prime_divisor, list_primitive_prime_divisors
has_primitive_prime_divisor(a, b, k, plus=True) -> (bool, p_ou_None)
list_primitive_prime_divisors(a, b, k, plus=True) -> list[int]
Notas técnicas

Altura inteira: h_int(0, ±1) = 0 por convenção (estabilidade numérica em testes).
O bound de soma usa tolerância de 1e-12 para evitar falsos negativos por ponto flutuante.
A rotina Zsigmondy assume gcd(a,b)=1 e trata separadamente a^k + b^k e a^k − b^k conforme a paridade (compatível com os testes atuais).
Estrutura do projeto

src/
check_identities.py
zsigmondy_check.py
README.md
LICENSE
Próximos passos (opcional)

Unificar verify_height_upper_c e verify_sum_bound_by_c.
Adicionar docstrings e exemplos.
Integrar CI (pytest, ruff/flake8, mypy).
Licença
Este projeto é licenciado sob a BSD 3-Clause License.

Resumo:

Você pode usar, modificar e distribuir este software, com ou sem modificações.
Deve manter o aviso de copyright, a lista de condições e o disclaimer.
Não é permitido usar o nome dos autores/colaboradores para endossar produtos derivados sem permissão prévia por escrito.
O software é fornecido “no estado em que se encontra”, sem garantias; os autores não se responsabilizam por quaisquer danos.
