# Documentação Técnica – Juvo DevOps Challenge

## Visão Geral
Este projeto implementa uma API de score de crédito simulada, desenvolvida em Flask, containerizada com Docker e orquestrada via Docker Compose. O pipeline CI/CD foi configurado com GitHub Actions, simulando um ambiente produtivo localmente, conforme solicitado no desafio.

## Estrutura do Projeto
- `app.py`: Código principal da API Flask.
- `requirements.txt`: Dependências Python.
- `Dockerfile`: Build da imagem Docker da API.
- `docker-compose.yml`: Orquestração dos containers.
- `features/`: Testes BDD (Behave).
- `tests/`: Testes unitários (Pytest).
- `docs/architecture/`: Diagramas da arquitetura proposta (draw.io, PNG, SVG).
- `.github/workflows/ci.yml`: Pipeline CI/CD automatizado.

## Como Executar Localmente
1. **Pré-requisitos:**
   - Docker e Docker Compose instalados.
2. **Build e execução:**
   ```sh
   docker-compose up --build
   ```
3. **Acessar a API:**
   - Endpoint: `http://localhost:5000/score/<cpf>`
   - Exemplo: `http://localhost:5000/score/12345678900`

## Pipeline CI/CD
- **CI:** Build, testes BDD e unitários automatizados.
- **CD:** Deploy automatizado local via Docker Compose, healthcheck pós-deploy, notificações de sucesso/falha, limpeza de containers antigos.
- **Workflow:** `.github/workflows/ci.yml`

## Testes
- **BDD:**
  - Arquivos em `features/`.
  - Executados automaticamente no pipeline.
- **Unitários:**
  - Arquivos em `tests/`.
  - Executados automaticamente no pipeline.

## Arquitetura Proposta
- Diagramas em `docs/architecture/`:
  - `Proposta de Arquitetura.drawio` (editável)
  - `Proposta de Arquitetura.drawio.png` (visualização)
  - `Proposta de Arquitetura.svg`

## Progresso do Projeto
### O que já foi feito
- API Flask implementada e testada.
- Containerização e orquestração com Docker Compose.
- Pipeline CI/CD completo (CI + CD) com healthcheck e notificações.
- Testes BDD e unitários automatizados.
- Diagrama de arquitetura AWS proposto.

### O que falta para completar
- Revisar e detalhar decisões técnicas no README principal.
- (Opcional) Adicionar exemplos de uso (curl/Postman) e instruções de rollback.
- Ajustar conforme feedback final do avaliador.

## Instruções para Testes Manuais
- Teste um CPF válido:
  ```sh
  curl http://localhost:5000/score/12345678900
  ```
- Teste um CPF inválido:
  ```sh
  curl http://localhost:5000/score/00000000000
  ```

## Instruções de Rollback Manual

Caso o deploy automatizado apresente falhas ou a nova versão da API apresente problemas, siga os passos abaixo para realizar o rollback manual:

1. **Identifique a versão anterior estável**
   - Se estiver usando versionamento de imagens Docker, utilize a tag correspondente à última versão estável.
   - Caso não utilize tags, utilize o commit anterior do repositório.

2. **Faça o checkout do commit estável**
   ```sh
   git checkout <commit_hash_estavel>
   ```

3. **Reconstrua e reinicie os containers**
   ```sh
   docker-compose down
   docker-compose up --build -d
   ```

4. **Verifique se a API voltou a funcionar**
   ```sh
   curl http://localhost:5000/score/12345678900
   ```

5. **(Opcional) Limpe imagens antigas**
   ```sh
   docker system prune -f
   ```

> Dica: Para facilitar rollbacks futuros, considere adotar versionamento explícito das imagens Docker (ex: juvo-api:<tag>).

## Contato
Dúvidas ou sugestões: Daniel F. Muniz (dfmuniz74@gmail.com)
