from os import getcwd, system, path
from sys import platform

# armazenando o caminho do do diretório atual na variável (pwd)
pwd = getcwd().split("/");

# verificando se a plataforma onde a aplicação está rodando é Linux
if(platform == "linux"):
    # verificando se o arquivo (install2.sh) ainda existe
    # verificando também se no caminho tem o diretório (com.termux)
    if("com.termux" in pwd and path.isfile("install2.sh")):
        # executando comandos específicos do (termux)
        system("sh install2.sh");
        # verificando se o arquivo (install.sh) ainda existe
    elif(path.isfile("install.sh")):
        # executando comandos específicos da maioria das distribuições Linux
        system("sh install.sh");

if(platform == "darwin"):
    print("""
  !¡! falando da versão do seu Mac OS x e relacionando-a com o a versão do PHP !¡!

PHP 7.3 (próximo estável) - 10.10 e posterior
curl -s https://php-osx.liip.ch/install.sh | bash -s 7.3

PHP 7.2 (atual estável) - 10.10 e posterior
curl -s https://php-osx.liip.ch/install.sh | bash -s 7.2

PHP 7.1 (estável antigo) - 10.10 e posterior
curl -s https://php-osx.liip.ch/install.sh | bash -s 7.1

PHP 7.0 (antigo estável) - 10.10 e posterior
curl -s https://php-osx.liip.ch/install.sh | bash -s 7.0

PHP 5.6 (antigo estável) - 10.8 e posterior
curl -s https://php-osx.liip.ch/install.sh | bash -s 5.6

PHP 5.5 (fim de vida) - todas as versões do OS X
curl -s https://php-osx.liip.ch/install.sh | bash -s 5.5

PHP 5.4 (fim de vida) - todas as versões OS X
curl -s https://php-osx.liip.ch/install.sh | bash -s 5.4

PHP 5.3 (fim de vida) - todas as versões do OS X
curl -s https://php-osx.liip.ch/install.sh | bash -s 5.3

Ele pedirá sua senha. Instalamos o empacotador em / usr / local / packer e o PHP em / usr / local / php5 e para isso, precisamos de sua senha. Não fazemos nada de mal com isso."""); 



            VOU TER QUE ESTUDAR PELO MENOS DECISÃO NO BASH/SHELL_SCRIPT PARA REPRODUZIR ISSO COM DECISÕES NO (INSTALL3.SH)



# verificando se a plataforma onde a aplicação está rodando é Windows
if(platform == "win32"):
    print("""meu amigo, se vira aí pra atualizar esse seu Windows meu consagrado,
eu não faço a mínima ideia como eu faço isso"""); 
    






