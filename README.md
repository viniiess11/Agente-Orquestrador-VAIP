<div align="center">

# 🧠 VAIP - Agente Orquestrador Mestre
**Vinicius + AI + Patrik • Arquitetura de Orquestração Autônoma, Gestão Multi-Projetos e Segurança Digital**

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![CI/CD GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF.svg?logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Discord Integration](https://img.shields.io/badge/Alerts-Discord_Webhook-5865F2.svg?logo=discord&logoColor=white)](https://discord.com/)
[![Zero-Leak Security](https://img.shields.io/badge/Security-Zero--Leak%20Policy-success.svg?logo=shield&logoColor=white)](#-segurança-e-governança-zero-leak)
[![Status](https://img.shields.io/badge/Status-Produção%20Ativa-brightgreen.svg)](#-projetos-orquestrados)

<p align="center">
  <i>Um ecossistema robusto de agentes especialistas e automações inteligentes projetado para coordenar fluxos analíticos, monitoramento de oportunidades de mercado e esteiras digitais de alta performance.</i>
</p>

---

</div>

## 📌 Visão Geral do Ecossistema

O **VAIP** é o agente supervisor mestre concebido pelos fundadores **Patrik Ernandes Siqueira** e **Vinicius**. O sistema opera desacoplado: o núcleo orquestrador gerencia múltiplos projetos independentes, coordenando subagentes descartáveis, rotinas em nuvem e políticas rígidas de cibersegurança e eficiência de tokens.

```text
                                 ┌─────────────────────────┐
                                 │   VAIP MASTER AGENT     │
                                 │ (Governança & Despacho) │
                                 └───────────┬─────────────┘
                                             │
               ┌─────────────────────────────┴─────────────────────────────┐
               ▼                                                           ▼
┌──────────────────────────────┐                           ┌──────────────────────────────┐
│  PRJ-01: Vagas-dados-Mogi    │                           │  PRJ-02: Canais-Dark-Engine  │
│  - Scraping & Match Semântico│                           │  - Roteirização via LLM      │
│  - Discord Webhook / Forum   │                           │  - TTS + Render Local FFmpeg │
│  - Copiloto de Candidatura   │                           │  - Multi-Upload Automático   │
│  - Nuvem (GitHub Actions)    │                           │  - TikTok, Kwai & YouTube    │
└──────────────────────────────┘                           └──────────────────────────────┘
```

---

## 🚀 Projetos Orquestrados

### 🟢 `PRJ-01`: Vagas-dados-Mogi-e-regiao (Ativo em Produção)
Esteira autônoma de inteligência de mercado focada em oportunidades de **Dados & Business Intelligence** no polo do **Alto Tietê (Mogi das Cruzes, Suzano, Guararema, Salesópolis, Poá), Guarulhos e posições 100% Remoto**.

* **Monitoramento Contínuo:** Varredura diária automatizada via APIs públicas e portais de carreiras (Gupy, LinkedIn Jobs, Catho, InfoJobs).
* **Filtro de Frescor:** Rastreamento com priorização de vagas publicadas nas últimas 24h a 7 dias.
* **Alertas Inteligentes no Discord:** Publicação diária às **17:30** no canal `#vagas-dados` com criação automática de tópicos (*threads*) por data e links diretos parametrizados.
* **Copiloto de Candidatura (`copilot_apply.py`):** Preenchimento assistido de formulários com base no histórico curricular estruturado (`data/profile.json`), gerando cartas de apresentação hiperpersonalizadas alinhadas aos requisitos de cada vaga.
* **Execução Híbrida (Local + Nuvem):**
  * *Local:* Agendador de Tarefas do Windows (`VAIP_Job_Hunter_Daily`).
  * *Nuvem:* GitHub Actions Workflow (`daily_jobs.yml`) programado via Cron para execução diária gratuita e pontual mesmo com o computador desligado.

---

### 🟡 `PRJ-02`: Canais-Dark-Engine (Em Estruturação)
Pipeline automatizado de criação, composição e distribuição de mídia vertical (9:16) para plataformas de vídeo curto: **YouTube Shorts, TikTok e Kwai**.

* **Geração Rápida de Roteiros:** Estrutura de ganchos de alta retenção (3s) e storytelling dinâmico (30-50s) com baixo custo de tokens.
* **Renderização Eficiente:** Composição visual, legendas sincronizadas e mixagem de áudio automatizadas localmente com **FFmpeg** e engines leves de síntese de voz (TTS).
* **Agendamento Inteligente:** Otimização de metadados, títulos com SEO orientado a tendências e tags estratégicas.

---

## 🛡️ Segurança e Governança (Zero-Leak)

Projetado sob rigorosos padrões de segurança da informação e integridade corporativa:

1. **Zero-Leak de Credenciais:** Nenhuma chave de API, webhook, token de sessão ou senha de portal é versionada. Todas as variáveis sensíveis são injetadas exclusivamente via `.env` local ou *GitHub Actions Secrets*.
2. **Defesa contra Injeção de Prompt (Web Shield):** Dados coletados de sites externos são sanitizados antes de serem avaliados por qualquer modelo generativo.
3. **Prevenção de Perda de Dados:** Operações destrutivas exigem confirmação explícita de governança antes da execução.
4. **Eficiência Extrema de Tokens:** Tarefas pesadas de computação, parsing e renderização rodam em scripts locais e workers em nuvem, garantindo respostas rápidas e custo de inferência próximo de zero.

---

## 📂 Arquitetura do Repositório

```text
Agente-Orquestrador-VAIP/
├── .github/
│   └── workflows/
│       └── daily_jobs.yml        # CI/CD & Automação Cron diária às 17:30
├── config/
│   └── security_policy.md       # Diretrizes formais de segurança e economia de tokens
├── ledger/
│   ├── PROJECTS_LEDGER.md       # Painel visual do status de cada projeto
│   └── state.json               # Estado persistente legível por máquina
├── agents/
│   ├── vaip_master.md           # Blueprint e diretrizes do Orquestrador Mestre
│   ├── job_hunter_spec.md       # Especificação técnica do subagente de vagas
│   └── dark_channel_spec.md     # Especificação técnica do subagente de canais dark
├── scripts/
│   ├── vaip.py                  # CLI Master de governança, branches e PRs
│   ├── search_jobs.py           # Motor de busca e parametrização de links por região
│   ├── notify.py                # Integração e disparo de Embeds ricos para o Discord
│   ├── daily_runner.py          # Runner unificado de orquestração diária
│   └── copilot_apply.py         # Copiloto de candidatura e respostas contextuais
├── data/
│   └── profile.json             # Perfil curricular estruturado para auto-fill
├── .env.example                 # Modelo seguro de configuração de ambiente
├── .gitignore                   # Blindagem de dados sensíveis e binários
└── README.md                    # Documentação técnica executiva
```

---

## ⚡ Como Executar Localmente

### 1. Clonar o Repositório
```bash
git clone https://github.com/viniiess11/Agente-Orquestrador-VAIP.git
cd Agente-Orquestrador-VAIP
```

### 2. Configurar o Ambiente
Copie o template seguro e preencha suas variáveis:
```bash
cp .env.example .env
```

### 3. Rodar a Varredura de Vagas Manualmente
```bash
python scripts/daily_runner.py
# ou via orquestrador:
python scripts/vaip.py run PRJ-01
```

---

## 🤝 Fluxo de Trabalho Paralelo (Vinícius & Patrik)

Para que ambos trabalhem em paralelo em suas respectivas casas sem sobrescrever código ou gerar conflitos:

1. **Antes de Iniciar Qualquer Código:**  
   Rode sempre:
   ```bash
   git checkout main
   git pull origin main
   ```
   *Isso garante 100% de certeza de que você está partindo da versão mais recente do projeto.*

2. **Crie uma Branch para Cada Funcionalidade (Nunca comite na `main`):**
   ```bash
   python scripts/vaip.py branch minha-tarefa
   # ou manualmente: git checkout -b feat/vinii-minha-tarefa
   ```

3. **Abra um Pull Request:**
   ```bash
   python scripts/vaip.py pr
   ```

4. **Se Ocorrer Conflito no Git:**  
   Se vocês alterarem exatamente a mesma linha do mesmo arquivo, o Git avisará no Pull Request. Vocês só precisarão abrir o arquivo localmente, escolher qual trecho manter e fazer o commit de resolução.

---

## 👥 Criadores & Autores

* **Patrik Ernandes Siqueira** — *Analista de Dados & Business Intelligence* • [LinkedIn](https://www.linkedin.com/in/patrik-e-siqueira/) • [GitHub](https://github.com/patrikesiqueira93)
* **Vinicius** — *Co-criador e Estrategista de Negócios*

---

<div align="center">
  <sub>Construído com rigor técnico, postura e foco em resultados de alto nível. • <b>VAIP 2026</b></sub>
</div>
