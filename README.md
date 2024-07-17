# Ideia Geral
Repositório direcionado a explicar o funcionamento do bot para faturamento dos produtos do Agenda Fácil.

# Problemática
Percebemos uma oportunidade de melhoria no faturamento dos produtos do Agenda Fácil, considerando que o processo era feito todo de forma manual. O processo em si é simples, consiste basicamente no preenchimento de um formulário no HUB WebMotors. Porém, a volumetria desses produtos era muito grande e exigia muito tempo que poderia ser aproveitado de forma mais efetiva. Com isso, surge a necessidade de que esse processo seja feito de forma automática, sem que seja necessário que um funcionário fique horas faturando cada item.

# Solução
Partindo da problemática ser somente a automação de um processo manual, o uso de uma linguagem de programação seria o ideal para a realização desse processo. Com o uso de Python e a utilização de Selenium WebDriver com pandas para a interface de usuário, desenvolvi um aplicativo para que esse faturamento seja feito de forma automática.

# Funcionamento
Quando utilizamos um driver para automações web, acaba sendo necessário que de alguma forma tenhamos acesso às informações de login para ter acesso aos sites. Para isso, desenvolvi uma interface simples de formulário onde o usuário insere suas informações de login. Essas informações, por sua vez, ficam armazenadas em variáveis e se perdem com a finalização do aplicativo. O intuito disso é que ele possa ser disponibilizado na pasta compartilhada sem que ninguém tenha acesso às informações inseridas anteriormente.
                          
O resultado da interface criada anteriormente é esse:

![image](https://github.com/GabriellpTV/Agenda-Facil/assets/138072118/ff51441e-039e-4b97-b996-6dd766576b04)

Após inserir os dados de login, a tela é atualizada com um botão "Inserir". Neste passo, o usuário irá inserir a base com as informações dos fornecedores a serem faturados.

Formato Padrão da base:
![image](https://github.com/GabriellpTV/Agenda-Facil/assets/138072118/c11e702a-b94b-4c1c-bddb-4e7beefb3edb)

É ideal que a base siga esse formato para o funcionamento correto do faturamento. As colunas "CNPJ", "Total" e "Cliente" devem ser preenchidas pelo usuário, são com elas que o bot irá preencher as informações no Hub. As colunas "Status" e "Faturado" serão atualizadas pelo bot, que irá dizer a situação do cliente e se ele foi faturado ou não.
OBS: É importante não mudar o nome das colunas, pois isso ocasionará erros.

Resultado:

![image](https://github.com/GabriellpTV/Agenda-Facil/assets/138072118/ea6eb569-b8e8-4a95-8faf-9e45920f828f)

Ao clicar no botão, a função inserir base é chamada. Nela utilizei `askopenfilename()` para que o usuário possa inserir o arquivo. Com isso, a base é inserida e outro botão surgirá, "Faturar". Ao clicar, a função de faturamento se inicia.

Resultado:

![image](https://github.com/GabriellpTV/Agenda-Facil/assets/138072118/d2b3f822-0c7c-44e4-bbce-e935a690f885)

O processo do Hub é feito com Selenium, onde o driver usa a entrada de e-mail e senha para login e as informações dos produtos da planilha. Para cada linha, um novo loop se inicia realizando o processo de forma automática. Nessa parte, o usuário não deve interferir no funcionamento do bot e deve aguardar que o processo seja finalizado.

Caso deseje finalizar a execução do bot, simplesmente feche a janela do terminal. Isso irá interromper todos os processos, garantindo que ele seja finalizado de imediato.

![image](https://github.com/GabriellpTV/Agenda-Facil/assets/138072118/843b0bb4-2d8b-4325-88a8-65eeb9752eda)

Com todos os produtos faturados, a tela irá se atualizar, dando ao usuário a opção de abrir o relatório. Ao clicar, uma planilha irá abrir e o usuário terá acesso aos produtos e às informações de situação e se ele foi faturado ou não.

![image](https://github.com/GabriellpTV/Agenda-Facil/assets/138072118/55608ea1-e7ce-40d6-bad5-bb897027b8b5)

Link para download:

[https://drive.google.com/file/d/1jta7C_qColEeAtJOH2-F8uWzeYSDxHXt/view?usp=drive_link](https://drive.google.com/drive/folders/1IaakGTT_W5Tr98qnnYJC7OAUpGfaZIr2?usp=drive_link)
---
