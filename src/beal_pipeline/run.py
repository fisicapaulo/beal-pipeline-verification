# beal_pipeline/run.py

import argparse
import json
import logging
from logging import FileHandler
import os
from pathlib import Path
from datetime import datetime, timezone
from dataclasses import dataclass, asdict

# Estrutura de configuração da execução (facilita salvar em metrics.json)
@dataclass
class RunConfig:
    run_id: str
    hstar: float
    max_base: int
    max_exp: int
    min_exp: int
    odd_exponents: bool
    modules: list
    processes: int
    epsilon: float
    output_dir: str

def parse_args():
    p = argparse.ArgumentParser(description="beal-pipeline-verification runner")
    p.add_argument("--run-id", required=True)
    p.add_argument("--hstar", type=float, required=True)
    p.add_argument("--max-base", type=int, required=True)
    p.add_argument("--max-exp", type=int, required=True)
    p.add_argument("--min-exp", type=int, default=3)
    p.add_argument("--odd-exponents", action="store_true")
    p.add_argument("--modules", type=str, required=True, help="Lista separada por vírgulas")
    p.add_argument("--processes", type=int, default=1)
    p.add_argument("--epsilon", type=float, default=1e-12)
    p.add_argument("--output-dir", type=str, required=True)
    return p.parse_args()

def ensure_dirs(base: Path):
    (base / "logs").mkdir(parents=True, exist_ok=True)
    (base / "tables").mkdir(parents=True, exist_ok=True)
    (base / "hashes").mkdir(parents=True, exist_ok=True)

def setup_logger(log_dir: Path) -> logging.Logger:
    logger = logging.getLogger("beal_pipeline")
    logger.setLevel(logging.INFO)

    # Evita múltiplos handlers ao chamar main() mais de uma vez
    if not any(isinstance(h, FileHandler) and getattr(h, "_bp_main", False) for h in logger.handlers):
        fh = logging.FileHandler(log_dir / "main.log", encoding="utf-8")
        fh.setLevel(logging.INFO)
        fh._bp_main = True  # marca para evitar duplicidade
        fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        fh.setFormatter(fmt)
        logger.addHandler(fh)

    # Também loga no console quando for execução interativa
    if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        ch.setFormatter(fmt)
        logger.addHandler(ch)

    return logger

def module_logger(base_log_dir: Path, name: str) -> logging.Logger:
    """Cria/retorna um logger específico de módulo com arquivo próprio."""
    logger = logging.getLogger(f"beal_pipeline.{name}")
    logger.setLevel(logging.INFO)
    if not any(isinstance(h, FileHandler) and getattr(h, "_bp_mod", None) == name for h in logger.handlers):
        fh = logging.FileHandler(base_log_dir / f"{name}.log", encoding="utf-8")
        fh.setLevel(logging.INFO)
        fh._bp_mod = name
        fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        fh.setFormatter(fmt)
        logger.addHandler(fh)
    return logger

def write_metrics(outdir: Path, content: dict):
    with open(outdir, "a"):
        pass  # garante que o diretório existe
    with open(Path(outdir) / "metrics.json", "w", encoding="utf-8") as f:
        json.dump(content, f, indent=2, ensure_ascii=False)

def main():
    args = parse_args()
    outdir = Path(args.output_dir)
    ensure_dirs(outdir)

    logger = setup_logger(outdir / "logs")

    # Normaliza lista de módulos
    modules = [m.strip() for m in args.modules.split(",") if m.strip()]
    cfg = RunConfig(
        run_id=args.run_id,
        hstar=args.hstar,
        max_base=args.max_base,
        max_exp=args.max_exp,
        min_exp=args.min_exp,
        odd_exponents=bool(args.odd_exponents),
        modules=modules,
        processes=args.processes,
        epsilon=args.epsilon,
        output_dir=args.output_dir,
    )

    start = datetime.now(timezone.utc)
    logger.info("Run %s started", cfg.run_id)
    logger.info("Params: %s", asdict(cfg))

    # Loggers de módulos (placeholders; integraremos nos próximos passos)
    mod_logs = {name: module_logger(outdir / "logs", name) for name in modules}

    errors = 0
    counts = {
        "instances_generated": 0,
        "filtered_congruences": 0,
        "pass_lte": 0,
        "blocked_height_radical": 0,
        "zsigmondy_barriers": 0,
        "survivors_after_congruences": 0,
        "survivors_after_lte": 0,
        "survivors_after_height_radical": 0,
    }

    try:
        # Placeholder: integração real virá nos próximos passos.
        for name, logg in mod_logs.items():
            logg.info("Módulo %s inicializado (placeholder). Integração virá nos próximos passos.", name)

    except Exception as e:
        errors += 1
        logger.exception("Erro durante a execução: %s", e)

    finished = datetime.now(timezone.utc)
    metrics = {
        "run_id": cfg.run_id,
        "started_at_utc": start.isoformat(),
        "finished_at_utc": finished.isoformat(),
        "duration_seconds": (finished - start).total_seconds(),
        "params": asdict(cfg),
        "counts": counts,
        "errors": errors,
        "host_env": {
            "python_version": os.sys.version,
            "platform": os.name,
        },
    }
    write_metrics(outdir, metrics)
    logger.info("Run %s finished (errors=%d). Metrics salvas em %s", cfg.run_id, errors, outdir / "metrics.json")

if __name__ == "__main__":
    main()

