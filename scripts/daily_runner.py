"""
VAIP Daily Runner - Executa a varredura completa e dispara as notificacoes.
Pode ser chamado localmente pelo Agendador de Tarefas do Windows ou na Nuvem pelo GitHub Actions.
"""

import os
import sys
import json
from datetime import datetime

# Adicionar diretorio de scripts ao path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from search_jobs import generate_search_links, export_daily_report
from notify import send_discord_report

def run_daily_hunt():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Iniciando VAIP Job Hunter...")
    
    # 1. Gerar relatorio local em Markdown
    report_file = export_daily_report()
    
    # 2. Obter links formatados
    links = generate_search_links()
    
    # 3. Disparar para o Discord (com o arquivo .md anexado)
    success = send_discord_report(links, file_path=report_file)
    
    # 4. Atualizar o Ledger de Estado
    base_dir = os.path.dirname(current_dir)
    state_file = os.path.join(base_dir, "ledger", "state.json")
    if os.path.exists(state_file):
        try:
            with open(state_file, "r", encoding="utf-8") as f:
                state = json.load(f)
            
            state["updated_at"] = datetime.now().isoformat()
            if "PRJ-01" in state.get("projects", {}):
                state["projects"]["PRJ-01"]["last_run"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                state["projects"]["PRJ-01"]["status"] = "active"
                
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(state, f, indent=2, ensure_ascii=False)
            print("[+] Ledger atualizado com sucesso!")
        except Exception as e:
            print(f"[!] Erro ao atualizar state.json: {e}")

    print("[*] Execucao diaria concluida.")

if __name__ == "__main__":
    run_daily_hunt()
