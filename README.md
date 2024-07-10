# Ideia Geral
Repositório direcionado a explicar o funcionamento do bot para faturamento dos produtos de agenda fácil.

# Problemática
Percebemos uma oportunidade de melhoria no faturamento dos produtos de agenda fácil, considerando que o processo era feito todo de forma manual. O processo
em si é simples, constitui-se basicamente do preenchimento de um formulário no HUB webmotors. Porém, a volumetria desses profutos era muito grande e exigia muito tempo que poderia ser aproveitado de uma forma mais efetiva. Com isso surge a necessidade de que esse proceso seja feito de forma altomática, sem que seja necessário que um funcionario fique hora faturando cada item.

# Solução
Partindo da problemática ser somente a automção de um processo manual, o uso de uma linguem de programação seria o ideal para a realização desse processo. Com o uso de Pytohn e a utilização de Selenum WebDriver com pandas para a interface de usuário, desenvolvi um aplicativo para que esse faturamento seja feito de forma automática.

# Funcionamento
Quando utilizamos um driver para automações web acaba sendo necessário que de alguma forma tenhamos acesso as informações de login para ter acesso aos sites, para isso desenvolvi uma interface simples de formulário onde o usuário insere suas informações de login. Essas informações por sua vez ficam armazenadas em variáveis e se perdem com a finalização do aplicativo, o intuito disso é que ele possa ser disponibilizado na pasta compartilhada sem que ninguem tenha acesso as informações inseridas anteriormente.
                          
O resultado da interface criada anteriormente é esse:

![image](https://github.com/GabriellpTV/Agenda-Facil/assets/138072118/ff51441e-039e-4b97-b996-6dd766576b04)

Após Inserido os dados de login a tela é atualizada com um button "Inserir". Neste passo o usuário irá inserir a base com as informações dos fornecedores a serem faturados.

Formato Padrão da base:
![image](https://github.com/GabriellpTV/Agenda-Facil/assets/138072118/c11e702a-b94b-4c1c-bddb-4e7beefb3edb)

É ideal que a base siga esse formato para o funcionamento correto do faturamento. As colunas "CNPJ" "Total" "Cliente" devem ser preenchidas pelo usuário, são com elas que o bot irá preencher as informações no Hub. As colunas "Status" e "Faturado" serão atualizadas pelo bot, ele irá dizer a situação do clinete e se o cliente foi faturado ou não.
OBS: É importante não mudar o nome das colunas, pois isso ocasionará erros.

Resultado:

![image](https://github.com/GabriellpTV/Agenda-Facil/assets/138072118/ea6eb569-b8e8-4a95-8faf-9e45920f828f)

Ao clicar no botão a função inserir base é chamada, nela utilizei askopenfilename() para que o usuário possa inserir o arquivo, com isso a base é inserida e outro botão surgirá "Faturar". o clicar a função de faturamento se inicia.

Resultado:

![image](https://github.com/GabriellpTV/Agenda-Facil/assets/138072118/d2b3f822-0c7c-44e4-bbce-e935a690f885)

O Processo do Hub é feito com Selenium, onde o driver usa a entrada de email e senha para login e as informações dos produtos da planilha. Para cada linha um novo looping se inicia realizando o processo de forma automática. Nessa parte o usuário não deve interferir no fucionamento do bot e aguardar que o processo seja finalizado.

Caso deseje finalizar a atualização do bot, simplesmente feche a janela do terminal, isso irá interromper todos os processos garantindo que ele seja finaizado de imediato.

![image](https://github.com/GabriellpTV/Agenda-Facil/assets/138072118/843b0bb4-2d8b-4325-88a8-65eeb9752eda)

Com todos os produtos faturados, a tela irá se atualizar. Dando ao usuário a opção de abrir o relatorio, ao clicar uma planilha irá abrir e o usário tera acesso aos produtos e as informações de situação e se ele foi faturado ou não.

![image](https://github.com/GabriellpTV/Agenda-Facil/assets/138072118/55608ea1-e7ce-40d6-bad5-bb897027b8b5)

 
