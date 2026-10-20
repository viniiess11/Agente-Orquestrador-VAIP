"""
=============================================================================
🧠 VAIP - Core Orchestrator CLI & Master Dispatcher
Vinicius + AI + Patrik • Arquitetura de Orquestração Autônoma & Multi-Projetos
=============================================================================
"""

import os
import sys
import json
import argparse
import subprocess
from datetime import datetime
from pathlib import Path

# Adiciona diretório raiz e scripts ao path
ROOT_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT_DIR / "scripts"
LEDGER_DIR = ROOT_DIR / "ledger"
STATE_FILE = LEDGER_DIR / "state.json"
LEDGER_MD = LEDGER_DIR / "PROJECTS_LEDGER.md"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.append(str(SCRIPTS_DIR))

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich import print as rprint
    console = Console()
except ImportError:
    console = None


def load_state() -> dict:
    if not STATE_FILE.exists():
        return {"projects": {}, "master": {"name": "VAIP", "status": "init"}}
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(state: dict) -> None:
    state["updated_at"] = datetime.now().isoformat()
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def show_status():
    """Exibe o painel visual de governança do VAIP e todos os projetos cadastrados."""
    state = load_state()
    projects = state.get("projects", {})

    if console:
        header = (
            "[bold cyan]🧠 VAIP - Agente Orquestrador Mestre[/bold cyan]\n"
            "[dim]Vinicius + AI + Patrik • Governança Multi-Projetos & Agentes Especialistas[/dim]"
        )
        console.print(Panel(header, border_style="cyan"))

        table = Table(title="📌 Projetos Sob Governança", border_style="blue")
        table.add_column("ID", style="bold yellow", width=10)
        table.add_column("Nome do Projeto", style="bold white")
        table.add_column("Status", justify="center")
        table.add_column("Última Execução", style="dim")
        table.add_column("Checkpoint / Detalhes")

        status_icons = {
            "active": "[bold green]🟢 Ativo[/bold green]",
            "structuring": "[bold yellow]🟡 Em Estruturação[/bold yellow]",
            "paused": "[bold red]🔴 Pausado[/bold red]",
            "ready": "[bold blue]🔵 Pronto[/bold blue]"
        }

        for pid, data in projects.items():
            status_badge = status_icons.get(data.get("status", "structuring"), data.get("status"))
            last_run = data.get("last_run", "Nunca")
            checkpoint = data.get("checkpoint", data.get("niche", "Em andamento"))
            table.add_row(pid, data.get("name", pid), status_badge, str(last_run), str(checkpoint))

        console.print(table)
    else:
        print("=== VAIP MASTER ORCHESTRATOR ===")
        for pid, data in projects.items():
            print(f"- [{pid}] {data.get('name')} | Status: {data.get('status')} | Last Run: {data.get('last_run')}")


def run_project(project_id: str):
    """Executa a rotina do projeto especificado."""
    pid = project_id.upper()
    state = load_state()
    projects = state.get("projects", {})

    if pid not in projects:
        print(f"[!] Projeto '{pid}' não encontrado no ledger. Projetos disponíveis: {list(projects.keys())}")
        return

    if pid == "PRJ-01":
        from daily_runner import run_daily_hunt
        print(f"[*] Despachando execução para {pid} (Vagas-dados-Mogi)...")
        run_daily_hunt()
    elif pid == "PRJ-02":
        print(f"[*] {pid} (Canais Dark) está em fase de estruturação de roteiro e TTS.")
    else:
        custom_script = SCRIPTS_DIR / f"run_{pid.lower().replace('-', '_')}.py"
        if custom_script.exists():
            print(f"[*] Executando script dedicado: {custom_script.name}")
            os.system(f"{sys.executable} {custom_script}")
        else:
            print(f"[!] O projeto '{pid}' ainda não possui um runner automatizado em scripts/.")


def register_project(name: str, slug: str, description: str):
    """Registra um novo projeto no ledger central do VAIP."""
    state = load_state()
    projects = state.setdefault("projects", {})

    existing_nums = [int(p.split("-")[1]) for p in projects.keys() if p.startswith("PRJ-") and p.split("-")[1].isdigit()]
    next_num = max(existing_nums, default=0) + 1
    new_id = f"PRJ-{next_num:02d}"

    projects[new_id] = {
        "id": new_id,
        "slug": slug,
        "name": name,
        "description": description,
        "status": "structuring",
        "created_at": datetime.now().isoformat(),
        "last_run": None,
        "owner": "Vinicius & Patrik"
    }

    save_state(state)
    print(f"[+] Projeto {new_id} ({name}) registrado com sucesso no ledger!")
    return new_id


def sync_upstream():
    """Sincroniza com as atualizações do repositório upstream (Patrike)."""
    print("[*] Sincronizando com o upstream (Patrik)...")
    res1 = os.system("git fetch upstream")
    if res1 == 0:
        res2 = os.system("git merge upstream/main --no-edit")
        if res2 == 0:
            print("[+] Sincronização concluída com sucesso! Seu branch local está atualizado.")
        else:
            print("[!] Houve conflitos ou pendências no merge. Verifique com 'git status'.")
    else:
        print("[!] Não foi possível conectar ao upstream. Verifique sua conexão ou se o remote está configurado.")


def create_branch(name: str, author: str = "vinii", btype: str = "feat"):
    """Cria e muda para uma nova branch padronizada, impedindo trabalho na main."""
    clean_name = name.strip().lower().replace(" ", "-").replace("_", "-")
    branch_name = f"{btype}/{author}-{clean_name}"
    
    print(f"[*] Criando e alternando para a branch: {branch_name}...")
    res = os.system(f"git checkout -b {branch_name}")
    if res == 0:
        print(f"[+] Sucesso! Você está trabalhando na branch '{branch_name}'.")
        print("    Todas as suas modificações agora estão isoladas e não afetarão a 'main'.")
    else:
        print(f"[!] Falha ao criar a branch '{branch_name}'. Verifique o git status.")


def create_pr(title: str = None, body: str = None):
    """Faz o push da branch atual e abre um Pull Request no GitHub."""
    try:
        current_branch = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True
        ).strip()
    except Exception as e:
        print(f"[!] Erro ao detectar branch atual: {e}")
        return

    if current_branch in ["main", "master"]:
        print("[!] Você está na branch 'main'! Pull Requests devem ser criados a partir de uma branch de feature.")
        return

    print(f"[*] Fazendo push da branch '{current_branch}' para origin...")
    push_res = os.system(f"git push -u origin {current_branch}")
    if push_res != 0:
        print("[!] Erro ao enviar a branch para o GitHub.")
        return

    pr_title = title or f"feat: {current_branch.replace('feat/', '').replace('fix/', '').replace('-', ' ').title()}"
    pr_body = body or f"Alterações desenvolvidas na branch {current_branch} para colaboração VAIP."

    print(f"[*] Abrindo Pull Request no GitHub...")
    pr_cmd = f'gh pr create --repo viniiess11/Agente-Orquestrador-VAIP --base main --head {current_branch} --title "{pr_title}" --body "{pr_body}"'
    res = os.system(pr_cmd)
    if res == 0:
        print("[+] Pull Request criado com sucesso no GitHub!")
    else:
        print("[!] Não foi possível criar o PR automaticamente via gh cli.")


def setup_hooks():
    """Instala o git hook de pre-commit que bloqueia commits diretos na main."""
    hooks_dir = ROOT_DIR / ".git" / "hooks"
    hooks_dir.mkdir(parents=True, exist_ok=True)
    pre_commit_file = hooks_dir / "pre-commit"

    hook_script = """#!/bin/sh
branch=$(git rev-parse --abbrev-ref HEAD)
if [ "$branch" = "main" ] || [ "$branch" = "master" ]; then
    echo "=============================================================="
    echo "⛔ BLOQUEIO VAIP: Commits diretos na branch '$branch' são proibidos!"
    echo "Trabalho colaborativo Vinicius & Patrik: crie uma branch antes:"
    echo "  python scripts/vaip.py branch <nome-da-sua-tarefa>"
    echo "=============================================================="
    exit 1
fi
"""
    with open(pre_commit_file, "w", encoding="utf-8") as f:
        f.write(hook_script)

    print("[+] Git Hook de proteção instalado com sucesso em .git/hooks/pre-commit!")
    print("    Commits acidentais na branch 'main' agora serão bloqueados automaticamente.")


def main():
    parser = argparse.ArgumentParser(description="VAIP Master Orchestrator CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Comando status
    subparsers.add_parser("status", help="Mostra o painel de projetos e status do VAIP")

    # Comando run
    run_parser = subparsers.add_parser("run", help="Executa o fluxo de um projeto")
    run_parser.add_argument("project_id", help="ID do projeto (ex: PRJ-01)")

    # Comando new-project
    new_proj_parser = subparsers.add_parser("new-project", help="Cadastra um novo projeto no VAIP")
    new_proj_parser.add_argument("--name", required=True, help="Nome do projeto")
    new_proj_parser.add_argument("--slug", required=True, help="Slug do projeto (ex: meu-novo-app)")
    new_proj_parser.add_argument("--desc", default="", help="Descrição do projeto")

    # Comando sync
    subparsers.add_parser("sync", help="Sincroniza alterações do repositório do Patrik (upstream)")

    # Comando branch
    branch_parser = subparsers.add_parser("branch", help="Cria e alterna para uma nova branch protegida")
    branch_parser.add_argument("name", help="Nome da tarefa (ex: copiloto-vagas)")
    branch_parser.add_argument("--author", default="vinii", help="Autor da branch (padrao: vinii)")
    branch_parser.add_argument("--type", default="feat", help="Tipo (feat, fix, docs, chore)")

    # Comando pr
    pr_parser = subparsers.add_parser("pr", help="Faz push da branch e cria Pull Request no GitHub")
    pr_parser.add_argument("--title", default=None, help="Título do Pull Request")
    pr_parser.add_argument("--body", default=None, help="Descrição do Pull Request")

    # Comando setup-hooks
    subparsers.add_parser("setup-hooks", help="Instala o hook de proteção contra commits na main")

    args = parser.parse_args()

    if args.command == "status" or not args.command:
        show_status()
    elif args.command == "run":
        run_project(args.project_id)
    elif args.command == "new-project":
        register_project(args.name, args.slug, args.desc)
    elif args.command == "sync":
        sync_upstream()
    elif args.command == "branch":
        create_branch(args.name, args.author, args.type)
    elif args.command == "pr":
        create_pr(args.title, args.body)
    elif args.command == "setup-hooks":
        setup_hooks()


if __name__ == "__main__":
    main()
