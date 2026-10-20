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

---

## 3. 🔄 Diretrizes Obrigatórias de Trabalho Colaborativo

### 1️⃣ Antes de Iniciar Qualquer Código:
> **Rode sempre:**
> ```powershell
> git checkout main
> git pull origin main
> ```
> *(E, opcionalmente, `git pull upstream main` para trazer commits do repositório do Patrik).*  
> Isso garante 100% de certeza de que você está partindo da **versão mais recente e estável do projeto**, evitando retrabalho.

### 2️⃣ Criar a Branch de Trabalho:
```powershell
git checkout -b feat/vinii-minha-tarefa
# ou diretamente via CLI:
python scripts/vaip.py branch minha-tarefa
```

### 3️⃣ Desenvolver e Comitar na Branch:
```powershell
git add .
git commit -m "feat(modulo): descricao clara da alteracao"
```

### 4️⃣ Enviar e Abrir Pull Request (PR):
```powershell
python scripts/vaip.py pr
# ou via gh cli:
git push -u origin feat/vinii-minha-tarefa
gh pr create --repo viniiess11/Agente-Orquestrador-VAIP --base main --head feat/vinii-minha-tarefa --title "Titulo" --body "Descricao"
```

### 5️⃣ Se Ocorrer Conflito no Git:
> Se vocês alterarem exatamente a mesma linha do mesmo arquivo, o Git avisará no Pull Request ou durante o merge:
> 1. O Git inserirá marcadores no arquivo indicando as duas versões:
>    ```text
>    <<<<<<< HEAD (sua versao)
>    trecho de codigo A
>    =======
>    trecho de codigo B (versao do primo)
>    >>>>>>>
>    ```
> 2. Vocês só precisarão **abrir o arquivo localmente**, escolher qual trecho manter (ou combinar os dois), apagar os marcadores (`<<<<<<<`, `=======`, `>>>>>>>`), salvar o arquivo e rodar:
>    ```powershell
>    git add <arquivo-resolvido>
>    git commit -m "fix: resolve merge conflict"
>    git push
>    ```

---

## 4. Segurança (Zero-Leak) e Boas Práticas
- Nenhuma chave de API, webhook ou segredo pode ser comitado. Sempre utilizar `.env` e variáveis de ambiente.
- Tarefas pesadas de ETL, scraping ou processamento devem rodar em scripts locais (`scripts/`) via ambiente virtual `.venv` para economizar tokens.
- O arquivo `.git/hooks/pre-commit` bloqueia qualquer tentativa acidental de commit na `main`.
