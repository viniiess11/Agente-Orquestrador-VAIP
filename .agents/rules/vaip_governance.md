# 🧠 VAIP - Governança e Regras de Desenvolvimento

## 1. Identidade e Fundadores
- **VAIP** (Vinicius + AI + Patrik): Ecossistema de agentes autônomos e orquestrador mestre.
- **Fundadores**: Vinícius Eduardo de Siqueira Silva (@viniiess11) e Patrik Ernandes Siqueira (@patrikesiqueira93).

---

## 2. Trabalho Paralelo e Fluxo Git (Vinícius & Patrik)
- **Remotes Configurados**:
  - `origin`: Repositório do Vinícius (`https://github.com/viniiess11/Agente-Orquestrador-VAIP.git`)
  - `upstream`: Repositório do Patrik (`https://github.com/patrikesiqueira93/Agente-Orquestrador-VAIP.git`)
- **Branches de Trabalho**:
  - Criar branches temáticas para novas funcionalidades: `feat/vinii-<funcionalidade>`.
  - Antes de mesclar na `main`, sincronizar com o código do primo:
    ```powershell
    python scripts/vaip.py sync
    # ou manualmente:
    git fetch upstream
    git merge upstream/main
    ```
- **Commits Assertivos**: Mensagens em português ou padrão conventional commits (`feat:`, `fix:`, `refactor:`, `docs:`).

---

## 3. Arquitetura de Novos Projetos e Agentes
- Todo novo projeto deve receber um ID sequencial (`PRJ-03`, `PRJ-04`, etc.) e ser registrado no `ledger/state.json` e no `ledger/PROJECTS_LEDGER.md`.
- Para criar projetos automaticamente:
  ```powershell
  python scripts/vaip.py new-project --name "Nome do Projeto" --slug "slug-projeto" --desc "Descricao"
  ```
- Subagentes especializados devem ser colocados em `agents/` (documentação/blueprint) e `.agents/agents/<nome>/agent.md` (definição para o Antigravity).

---

## 4. Segurança (Zero-Leak) e Eficiência
- Nenhuma chave de API, webhook ou segredo pode ser comitado. Sempre utilizar `.env` e variáveis de ambiente.
- Tarefas pesadas de ETL, scraping ou processamento devem rodar em scripts locais (`scripts/`) via ambiente virtual `.venv` para economizar tokens.
