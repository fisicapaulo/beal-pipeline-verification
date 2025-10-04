Título: Execução run_Hstar_1759612928 — Artefatos e Reprodutibilidade

Resumo
Esta pasta contém os artefatos gerados pela execução run_Hstar_1759612928 do pipeline beal-pipeline-verification: logs, tabelas e hashes de verificação. O objetivo é permitir auditoria e reprodução exata dos resultados desta rodada.

Metadados da execução

ID da execução: run_Hstar_1759612928
Data/hora (UTC): 2025-10-04T22:00:00Z
Host/ambiente: Local — Python 3.11.9, Ubuntu 22.04
Commit do código: a1b2c3d
Semente/aleatoriedade: determinístico (sem RNG)
Tempo total: 01:17:42
Parâmetros principais

Intervalo/instâncias:
Bases coprimas a,b,c ≤ 10^6
Expoentes p, q, r ≥ 3 (ímpares), até 13
Filtro gcd(a,b,c)=1, gcd(a,b)=gcd(b,c)=gcd(a,c)=1
Módulos ativados:
Normalização: on
Congruências: on
LTE: on
Pinça altura–radical (height–radical): on
Barreiras tipo Zsigmondy: on
Tolerâncias/limiares:
H* = 1.759612928e6
ε = 1e-12
Paralelismo: 8 processos (multiprocessing)
Cache/curto-circuito: on (memoização de fatores primos e valuations v_p)
Artefatos nesta pasta

logs/ — logs de execução detalhados (por módulo e run)
tables/ — tabelas consolidadas (CSV)
hashes/ — checksums e manifestos de integridade
metrics.json — métricas agregadas (tempos, contagens, falhas)
README.md — este arquivo
Estrutura esperada

data/output/run_Hstar_1759612928/
logs/
main.log
normalization.log
congruences.log
lte.log
height_radical.log
zsigmondy.log
tables/
summary.csv
survivors_after_congruences.csv
survivors_after_lte.csv
survivors_after_height_radical.csv
blocked_by_zsigmondy.csv
hashes/
manifest.sha256
metrics.json
README.md
Integridade e verificação

Manifesto: hashes/manifest.sha256
Gerar/atualizar:
mkdir -p hashes
find . -type f ! -path "./hashes/manifest.sha256" ! -path "./hashes" -exec sha256sum {} ; | sort -k 2 > hashes/manifest.sha256
Verificar:
sha256sum --check hashes/manifest.sha256
Assinatura opcional:
gpg --armor --detach-sign hashes/manifest.sha256
Verificar assinatura:
gpg --verify hashes/manifest.sha256.asc hashes/manifest.sha256
Como reproduzir

Obtenha o código exatamente no commit desta execução:
git fetch --all
git checkout a1b2c3d
Crie/ative o ambiente:
Python 3.11
pip install -r requirements.txt
Execute com os mesmos parâmetros:
python -m beal_pipeline.run
--run-id run_Hstar_1759612928
--hstar 1759612.928
--max-base 1000000
--max-exp 13
--min-exp 3
--odd-exponents
--modules normalization,congruences,lte,height_radical,zsigmondy
--processes 8
--epsilon 1e-12
--output-dir data/output/run_Hstar_1759612928
Compare artefatos:
Recalcule o manifesto e rode sha256sum --check para confirmar integridade.
Resultados resumidos

Instâncias geradas: 2.84e7
Filtradas por congruências: 2.61e7
Casos passando LTE: 1.90e6
Casos bloqueados por pinça altura–radical: 1.90e6
Barreiras Zsigmondy acionadas: 0 remanescentes após altura–radical
Exceções/erros: 0 (ver logs/)
Notas e limitações

Caso algum arquivo exceda 50 MB, considerar Git LFS para tables/.csv e logs/.log.
Paths são relativos à raiz do repositório.
Alterações puramente de performance (paralelismo, ordem de iteração) não devem afetar resultados se commit e parâmetros forem idênticos.
Esta execução assume coprimalidade estrita e expoentes ímpares ≥ 3; variantes exigem reprocessamento.
Automação recomendada

Make alvo para manifesto:
make manifest
Regras sugeridas do Makefile:
manifest: mkdir -p data/output/run_Hstar_1759612928/hashes;
cd data/output/run_Hstar_1759612928 &&
find . -type f ! -path "./hashes/manifest.sha256" ! -path "./hashes" -exec sha256sum {} ; | sort -k 2 > hashes/manifest.sha256
Citação
Se utilizar estes artefatos, cite:

fisicapaulo/beal-pipeline-verification, run_Hstar_1759612928, commit a1b2c3d, 2025. Licença BSD-3-Clause.
Licença
BSD 3-Clause. Ver LICENSE na raiz do repositório.
