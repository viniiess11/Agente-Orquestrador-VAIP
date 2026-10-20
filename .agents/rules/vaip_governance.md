# 🧠 VAIP - Governança e Regras de Desenvolvimento

## 1. Identidade e Fundadores
- **VAIP** (Vinicius + AI + Patrik): Ecossistema de agentes autônomos e orquestrador mestre.
- **Fundadores**: Vinícius Eduardo de Siqueira Silva (@viniiess11) e Patrik Ernandes Siqueira (@patrikesiqueira93).

---

## 2. 🛑 REGRA DE OURO: ZERO COMMITS DIRETOS NA MAIN
> [!IMPORTANT]
> **A branch `main` é estritamente protegida.** Nenhuma alteração, inclusão, refatoração ou modificação deve ser comitada diretamente na `main`. O assistente de IA e os desenvolvedores DEVEM sempre trabalhar em branches dedicadas.

### 📌 Padrão de Nomenclatura de Branches:
- **Funcionalidades do Vinícius**: `feat/vinii-<nome-da-funcionalidade>`
- **Correções do Vinícius**: `fix/vinii-<nome-do-bug>`
- **Tarefas do Patrik**: `feat/patrike-<nome-da-funcionalidade>` ou `fix/patrike-...`
- **Documentação / Configurações**: `docs/vinii-...` ou `chore/vinii-...`

### 🔄 Fluxo Obrigatório de Qualquer Tarefa:
1. **Sempre iniciar a partir da `main` atualizada**:
   ```powershell
   git checkout main
   git pull origin main
   git pull upstream main  # puxar atualizações do Patrik se houver
   ```
2. **Criar a branch de trabalho**:
   ```powershell
   git checkout -b feat/vinii-minha-tarefa
   # ou via CLI: python scripts/vaip.py branch minha-tarefa
   ```
3. **Desenvolver e comitar na branch**:
   ```powershell
   git add .
   git commit -m "feat(modulo): descricao clara da alteracao"
   ```
4. **Enviar a branch para o GitHub e abrir Pull Request (PR)**:
   ```powershell
   git push -u origin feat/vinii-minha-tarefa
   gh pr create --title "Minha Feature" --body "Descricao do que foi feito"
   # ou via CLI: python scripts/vaip.py pr
   ```
5. **Merge**: A branch é revisada e mesclada na `main` pelo GitHub sem risco de sobreescrever o trabalho do outro.

---

## 3. Segurança (Zero-Leak) e Boas Práticas
- Nenhuma chave de API, webhook ou segredo pode ser comitado. Sempre utilizar `.env` e variáveis de ambiente.
- Tarefas pesadas de ETL, scraping ou processamento devem rodar em scripts locais (`scripts/`) via ambiente virtual `.venv` para economizar tokens.
- O arquivo `.git/hooks/pre-commit` bloqueia qualquer tentativa acidental de commit na `main`.
