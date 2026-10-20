"""
VAIP Notifier - Disparo Seguro e Formatado para o Discord
Suporta canais de texto padrão, canais de fórum e anexos de arquivos (.md).
Lê credenciais exclusivamente do arquivo .env ou variáveis de ambiente.
"""

import os
import json
import urllib.request
from datetime import datetime

def load_env(env_path=None):
    """Carrega as variáveis do arquivo .env de forma segura."""
    if env_path is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        env_path = os.path.join(base_dir, ".env")
        
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    os.environ[key.strip()] = val.strip().strip('"').strip("'")

def send_discord_report(links, candidate_name="Patrik Ernandes Siqueira", file_path=None) -> bool:
    """Envia o relatório diário formatado em Embed e com o arquivo .md anexado para o Discord."""
    load_env()
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print("[!] DISCORD_WEBHOOK_URL não encontrada no .env ou nas Secrets.")
        return False

    today_str = datetime.now().strftime("%d/%m/%Y")
    
    fields = []
    for item in links[:12]:
        data_info = item.get("data_postagem", "Recente")
        fields.append({
            "name": f"📍 {item['portal']} • {item['regiao']}",
            "value": f"**Cargo:** {item['termo']}\n⏱️ **Publicação:** `{data_info}`\n🔗 [Acessar Vagas Filtradas]({item['url']})",
            "inline": False
        })
        
    description_text = (
        f"Salve, **{candidate_name}**! Seguem as vagas filtradas no **Alto Tietê "
        f"(Mogi das Cruzes, Suzano, Guararema, Salesópolis), Guarulhos e Remoto** "
        f"para o seu perfil de Analista de Dados & BI."
    )
    if file_path and os.path.exists(file_path):
        description_text += f"\n\n📎 **Arquivo completo com todas as oportunidades anexado abaixo!**"

    embed = {
        "title": f"🎯 Relatório Diário de Vagas em Dados - {today_str}",
        "description": description_text,
        "color": 3447003, # Azul tecnológico elegante
        "fields": fields,
        "footer": {
            "text": "VAIP Master Orchestrator • Zero-Leak & Nuvem Autônoma",
            "icon_url": "https://cdn-icons-png.flaticon.com/512/4712/4712038.png"
        }
    }
    
    payload = {
        "username": "VAIP - Job Hunter",
        "avatar_url": "https://cdn-icons-png.flaticon.com/512/4712/4712038.png",
        "thread_name": f"🎯 Vagas de Dados - {today_str}", # Suporta canal de fórum
        "embeds": [embed]
    }
    
    try:
        if file_path and os.path.exists(file_path):
            filename = os.path.basename(file_path)
            with open(file_path, "rb") as f:
                file_bytes = f.read()

            boundary = "----VAIPBoundary" + os.urandom(8).hex()
            body = bytearray()
            
            # 1. payload_json
            body.extend(f"--{boundary}\r\n".encode("utf-8"))
            body.extend(b'Content-Disposition: form-data; name="payload_json"\r\n')
            body.extend(b'Content-Type: application/json\r\n\r\n')
            body.extend(json.dumps(payload).encode("utf-8"))
            body.extend(b"\r\n")
            
            # 2. Arquivo anexo
            body.extend(f"--{boundary}\r\n".encode("utf-8"))
            body.extend(f'Content-Disposition: form-data; name="files[0]"; filename="{filename}"\r\n'.encode("utf-8"))
            body.extend(b'Content-Type: text/markdown; charset=utf-8\r\n\r\n')
            body.extend(file_bytes)
            body.extend(b"\r\n")
            
            body.extend(f"--{boundary}--\r\n".encode("utf-8"))
            
            req = urllib.request.Request(
                webhook_url,
                data=bytes(body),
                headers={
                    "Content-Type": f"multipart/form-data; boundary={boundary}",
                    "User-Agent": "Mozilla/5.0"
                }
            )
        else:
            data = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(
                webhook_url,
                data=data,
                headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
            )

        with urllib.request.urlopen(req) as resp:
            print("[+] Relatório e arquivo enviados com sucesso para o Discord!")
            return True
    except Exception as e:
        print(f"[-] Erro ao disparar para Discord: {e}")
        return False

def send_discord_message(content: str) -> bool:
    """Envia uma mensagem de texto simples para o Discord."""
    load_env()
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print("[!] DISCORD_WEBHOOK_URL não encontrada.")
        return False

    payload = {
        "username": "VAIP - Job Hunter",
        "avatar_url": "https://cdn-icons-png.flaticon.com/512/4712/4712038.png",
        "content": content
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        webhook_url,
        data=data,
        headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
    )
    try:
        with urllib.request.urlopen(req) as resp:
            print("[+] Mensagem de texto enviada para o Discord!")
            return True
    except Exception as e:
        print(f"[-] Erro ao enviar mensagem para Discord: {e}")
        return False

def send_telegram_message(content: str) -> bool:
    """Envia mensagem para o Telegram se configurado."""
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        return False
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": content, "parse_mode": "Markdown"}
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as resp:
            return True
    except Exception as e:
        print(f"[-] Erro Telegram: {e}")
        return False

if __name__ == "__main__":
    from search_jobs import generate_search_links
    links = generate_search_links()
    send_discord_report(links)
