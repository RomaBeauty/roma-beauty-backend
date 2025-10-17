
## Instalação e Configuração

1. Certifique-se de ter o [Python](https://www.python.org/) instalado em seu sistema.

2. Abra o projeto no vscode e execute o terminal.

2. Crie um ambiente virtual usando o [PDM](https://pdm.fming.dev/):

   ```
   pdm install
   ```

3. Crie o arquivo .env, a partir do arquivo .env.exemplo, e configure as variáveis de ambiente:

   ```
   cp .env.exemplo .env
   ```

4. Execute o servidor de desenvolvimento:

   ```
   pdm run dev
   ```

5. Acesse a API em http://localhost:19003/api/


## Licença

Este projeto está licenciado sob a [Licença GPL](https://www.gnu.org/licenses/gpl-3.0.html), uma licença de software livre.



