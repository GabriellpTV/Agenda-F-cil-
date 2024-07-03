# Ideia Geral
Repositório direcionado a explicar o funcionamento do bot para faturamento dos produtos de agenda fácil.

# Problemática
Percebemos uma oportunidade de melhoria no faturamento dos produtos de agenda fácil, considerando que o processo era feito todo de forma manual. O processo
em si é simples, constitui-se basicamente do preenchimento de um formulário no HUB webmotors. Porém, a volumetria desses profutos era muito grande e exigia muito tempo que poderia ser aproveitado de uma forma mais efetiva. Com isso surge a necessidade de que esse proceso seja feito de forma altomática, sem que seja necessário que um funcionario fique hora faturando cada item.

# Solução
Partindo da problemática ser somente a automção de um processo manual, o uso de uma linguem de programação seria o ideal para a realização desse processo. Com o uso de Pytohn e a utilização de Selenum WebDriver com pandas para a interface de usuário, desenvolvi um aplicativo para que esse faturamento seja feito de forma automática.

# Funcionamento
Quando utilizamos um driver apra automações web acaba sendo necessário que de alguma forma tenhamos acesso as informações de login para ter acesso aos sites, para isso desenvolvi uma interface simples de formulário onde o usuário insere suas informações de login. Essas informações por sua vez ficam armazenadas em variáveis e se perdem com a finalização do aplicativo, o intuito disso é que ele possa ser disponibilizado na pasta compartilhada sem que ninguem tenha acesso as informações inseridas anteriormente.

![image](https://github.com/GabriellpTV/Agenda-Facil/assets/138072118/9a924a39-27a3-498b-99eb-ffaeb65d7984)

O resultado da interface criada a cima é esse:

![image](https://github.com/GabriellpTV/Agenda-Facil/assets/138072118/ff51441e-039e-4b97-b996-6dd766576b04)
