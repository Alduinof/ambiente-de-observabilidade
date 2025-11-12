#atualizar o zabiix versao 1

================================
1 - Parar Zabbix por completo
================================
 
- Ordem de parada : proxy, frontend e server
 
OBS: logar em todos os servidores como root
 
1) Acessar servidor do proxy
 
2) Parar container do proxy zabbix
 
	cd /opt/programas/pro_84006_zabbix
	docker compose down
 
3) Acessar servidor de frontend
 
4) Parar container de frontend
 
	cd /opt/programas/pro_84006_zabbix
	docker compose down
 
5) Acessar servidor do Zabbix
 
6) Parar container do servidor zabbix
 
	cd /opt/programas/pro_84006_zabbix
	docker compose down
===================================
2 - Fazer backup do banco de dados
===================================
 
1) Acessar o servidor de banco. Logar como root
 
2) logar como postgres
 
	su - postgres
 
3) Fazer o backup do banco. A senha do banco será pedida na execução do comando
 
	pg_dump -d zabbix -U zabbix -c -C -v -W -h localhost|gzip -c > zabbix7.0_dbbackup.gz
 
=======================
3 - Atualizar server
=======================
 
OBS: logar como root
 
1) Acessar servidor do zabbix
 
 
2) Criar backup do arquivo compose
 
	cd /opt/programas/pro_84006_zabbix
	cp -a docker-compose.yml docker-compose_$(date +%Y%m%d)
 
3) alterar imagem para a versão 7.4
 
	cd /opt/programas/pro_84006_zabbix
	sed -i "s/alpine-7.0-latest/alpine-7.4-latest/g" docker-compose.yml
 
	OBS:altera a imagem de "zabbix/zabbix-server-pgsql:alpine-7.0-latest" para "zabbix/zabbix-server-pgsql:alpine-7.4-latest"
4) Reiniciar docker
	systemctl restart docker
 
 
========================
4 - Atualizar frontend
========================
 
OBS: logar como root
 
1) Acessar servidor do frontend
 
2) Criar backup do arquivo compose
 
	cd /opt/programas/pro_84006_zabbix
	cp -a docker-compose.yml docker-compose_$(date +%Y%m%d)
 
3) alterar imagem para a versão 7.4
 
    cd /opt/programas/pro_84006_zabbix
	sed -i "s/alpine-7.0-latest/alpine-7.4-latest/g" docker-compose.yml
 
	OBS:alterar a imagem de "zabbix/zabbix-web-apache-pgsql:alpine-7.0-latest" para "zabbix/zabbix-web-apache-pgsql:alpine-7.4-latest"
4) Reiniciar docker
	systemctl restart docker
 
=======================	
5 - Atualizar proxy
=======================
 
OBS: logar como root
 
1) Acessar servidor do proxy
 
2) Criar backup do arquivo compose
 
	cd /opt/programas/pro_84006_zabbix
	cp -a docker-compose.yml docker-compose_$(date +%Y%m%d)
 
3) alterar imagem para a versão 7.4
 
    cd /opt/programas/pro_84006_zabbix
	sed -i "s/alpine-7.0-latest/alpine-7.4-latest/g" docker-compose.yml
 
	OBS:altera a imagem de "zabbix/zabbix-proxy-sqlite3:alpine-7.0-latest" para "zabbix/zabbix-proxy-sqlite3:alpine-7.4-latest"
 
4) Reiniciar docker
   systemctl restart docker
 
=================================
6 - Iniciar Zabbix por completo
=================================
 
- Ordem de inicialização : server, frontend e proxy
 
OBS: logar em todos os servidores como root
 
1) Acessar servidor do Zabbix
 
2) Iniciar container do servidor zabbix
 
	cd /opt/programas/pro_84006_zabbix
	docker compose up -d
 
3) Acessar servidor do frontend
 
4) Iniciar container do frontend
 
	cd /opt/programas/pro_84006_zabbix
	docker compose up -d
 
5) Acessar servidor do proxy
 
6) Iniciar container do proxy zabbix
 
	cd /opt/programas/pro_84006_zabbix
	docker compose up -d================================
1 - Parar Zabbix por completo
================================
 
- Ordem de parada : proxy, frontend e server
 
OBS: logar em todos os servidores como root
 
1) Acessar servidor do proxy
 
2) Parar container do proxy zabbix
 
	cd /opt/programas/pro_84006_zabbix
	docker compose down
 
3) Acessar servidor de frontend
 
4) Parar container de frontend
 
	cd /opt/programas/pro_84006_zabbix
	docker compose down
 
5) Acessar servidor do Zabbix
 
6) Parar container do servidor zabbix
 
	cd /opt/programas/pro_84006_zabbix
	docker compose down
===================================
2 - Fazer backup do banco de dados
===================================
 
1) Acessar o servidor de banco. Logar como root
 
2) logar como postgres
 
	su - postgres
 
3) Fazer o backup do banco. A senha do banco será pedida na execução do comando
 
	pg_dump -d zabbix -U zabbix -c -C -v -W -h localhost|gzip -c > zabbix7.0_dbbackup.gz
 
=======================
3 - Atualizar server
=======================
 
OBS: logar como root
 
1) Acessar servidor do zabbix
 
 
2) Criar backup do arquivo compose
 
	cd /opt/programas/pro_84006_zabbix
	cp -a docker-compose.yml docker-compose_$(date +%Y%m%d)
 
3) alterar imagem para a versão 7.4
 
	cd /opt/programas/pro_84006_zabbix
	sed -i "s/alpine-7.0-latest/alpine-7.4-latest/g" docker-compose.yml
 
	OBS:altera a imagem de "zabbix/zabbix-server-pgsql:alpine-7.0-latest" para "zabbix/zabbix-server-pgsql:alpine-7.4-latest"
4) Reiniciar docker
	systemctl restart docker
 
 
========================
4 - Atualizar frontend
========================
 
OBS: logar como root
 
1) Acessar servidor do frontend
 
2) Criar backup do arquivo compose
 
	cd /opt/programas/pro_84006_zabbix
	cp -a docker-compose.yml docker-compose_$(date +%Y%m%d)
 
3) alterar imagem para a versão 7.4
 
    cd /opt/programas/pro_84006_zabbix
	sed -i "s/alpine-7.0-latest/alpine-7.4-latest/g" docker-compose.yml
 
	OBS:alterar a imagem de "zabbix/zabbix-web-apache-pgsql:alpine-7.0-latest" para "zabbix/zabbix-web-apache-pgsql:alpine-7.4-latest"
4) Reiniciar docker
	systemctl restart docker
 
=======================	
5 - Atualizar proxy
=======================
 
OBS: logar como root
 
1) Acessar servidor do proxy
 
2) Criar backup do arquivo compose
 
	cd /opt/programas/pro_84006_zabbix
	cp -a docker-compose.yml docker-compose_$(date +%Y%m%d)
 
3) alterar imagem para a versão 7.4
 
    cd /opt/programas/pro_84006_zabbix
	sed -i "s/alpine-7.0-latest/alpine-7.4-latest/g" docker-compose.yml
 
	OBS:altera a imagem de "zabbix/zabbix-proxy-sqlite3:alpine-7.0-latest" para "zabbix/zabbix-proxy-sqlite3:alpine-7.4-latest"
 
4) Reiniciar docker
   systemctl restart docker
 
=================================
6 - Iniciar Zabbix por completo
=================================
 
- Ordem de inicialização : server, frontend e proxy
 
OBS: logar em todos os servidores como root
 
1) Acessar servidor do Zabbix
 
2) Iniciar container do servidor zabbix
 
	cd /opt/programas/pro_84006_zabbix
	docker compose up -d
 
3) Acessar servidor do frontend
 
4) Iniciar container do frontend
 
	cd /opt/programas/pro_84006_zabbix
	docker compose up -d
 
5) Acessar servidor do proxy
 
6) Iniciar container do proxy zabbix
 
	cd /opt/programas/pro_84006_zabbix
	docker compose up -d
