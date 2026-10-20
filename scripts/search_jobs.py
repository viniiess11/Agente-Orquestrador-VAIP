"""
VAIP Job Hunter Engine - Módulo de Busca e Notificação de Vagas
Foco: Mogi das Cruzes, Alto Tietê, Guarulhos e Remoto (Área de Dados)
"""

import os
import json
import urllib.parse
from datetime import datetime

# Cidades-alvo do Alto Tietê e Grande SP Leste
LOCATIONS = [
    "Mogi das Cruzes",
    "Suzano",
    "Guararema",
    "Salesopolis",
    "Poa",
    "Itaquaquecetuba",
    "Guarulhos",
    "Remoto"
]

KEYWORDS = [
    "Analista de Dados",
    "Business Intelligence",
    "Power BI",
    "Engenheiro de Dados",
    "Analytics Engineer"
]

def generate_search_links():
    """Gera links diretos e parametrizados nos principais portais para o perfil do Patrik."""
    links = []
    
    # 1. Catho (Filtro últimas 24h a 7 dias)
    for loc in ["mogi-das-cruzes-sp", "suzano-sp", "guarulhos-sp"]:
        links.append({
            "portal": "Catho",
            "regiao": loc.replace("-sp", "").replace("-", " ").title(),
            "termo": "Analista de Dados",
            "data_postagem": "Últimas 24h a 7 dias",
            "url": f"https://www.catho.com.br/vagas/analista-de-dados/{loc}/"
        })
        links.append({
            "portal": "Catho",
            "regiao": loc.replace("-sp", "").replace("-", " ").title(),
            "termo": "Power BI / BI",
            "data_postagem": "Últimas 24h a 7 dias",
            "url": f"https://www.catho.com.br/vagas/business-intelligence/{loc}/"
        })
    
    # 2. LinkedIn Jobs com filtros pré-setados (f_TPR=r86400 para 24h ou r604800 para semana)
    for loc in ["Mogi das Cruzes, São Paulo, Brasil", "Guarulhos, São Paulo, Brasil", "Brasil (Remoto)"]:
        loc_encoded = urllib.parse.quote(loc)
        for term in ["Analista de Dados", "Power BI"]:
            term_encoded = urllib.parse.quote(term)
            links.append({
                "portal": "LinkedIn",
                "regiao": loc.split(",")[0],
                "termo": term,
                "data_postagem": "Recente (Últimas 24h / 7 dias)",
                "url": f"https://www.linkedin.com/jobs/search/?keywords={term_encoded}&location={loc_encoded}&f_TPR=r604800"
            })
            
    # 3. InfoJobs
    for loc in ["mogi-das-cruzes", "suzano", "guarulhos"]:
        links.append({
            "portal": "InfoJobs",
            "regiao": loc.replace("-", " ").title(),
            "termo": "Dados / BI",
            "data_postagem": "Últimos dias",
            "url": f"https://www.infojobs.com.br/vagas-de-emprego-analista-dados-em-{loc},-sp.aspx"
        })

    # 4. Gupy (Portais corporativos)
    links.append({
        "portal": "Gupy / Suzano S.A.",
        "regiao": "Suzano / Alto Tietê",
        "termo": "Vagas Corporativas e Dados",
        "data_postagem": "Ativas / Atualizadas",
        "url": "https://suzano.gupy.io/"
    })
    links.append({
        "portal": "Gupy Geral",
        "regiao": "Remoto",
        "termo": "Dados / Home Office",
        "data_postagem": "Ativas / Publicadas recentemente",
        "url": "https://portal.gupy.io/job-search/term=dados&workplaceType=remote"
    })
    
    return links

def export_daily_report(output_dir=None):
    if output_dir is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        output_dir = os.path.join(base_dir, "data")
    """Gera o arquivo Markdown diário com as oportunidades e links."""
    os.makedirs(output_dir, exist_ok=True)
    today_str = datetime.now().strftime("%Y-%m-%d")
    report_file = os.path.join(output_dir, f"vagas_{today_str}.md")
    
    links = generate_search_links()
    
    content = f"""# 🎯 Relatório Diário de Vagas de Dados - VAIP Hunter
**Data**: {today_str}
**Candidato**: Patrik Ernandes Siqueira (Analista de Dados & BI)
**Região Alvo**: Mogi das Cruzes, Suzano, Guararema, Salesópolis até Guarulhos e Remoto.

---

## 📌 Hub de Links Rápidos para Monitoramento Diário

| Portal | Região | Cargo / Foco | Link Direto |
| :--- | :--- | :--- | :--- |
"""
    for item in links:
        content += f"| **{item['portal']}** | {item['regiao']} | {item['termo']} | [Acessar Vagas]({item['url']}) |\n"
        
    content += """
---
> **Dica do VAIP**: Verifique especialmente as oportunidades postadas nas últimas 24h a 48h para ter prioridade no funil de triagem.
"""

    with open(report_file, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Relatório diário gerado com sucesso em: {report_file}")
    return report_file

if __name__ == "__main__":
    export_daily_report()
