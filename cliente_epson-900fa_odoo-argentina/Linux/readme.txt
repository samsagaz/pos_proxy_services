-	pip3 install -r requeriments.txt
- sudo nano /etc/sudoers:
	-  agregar despues de la linea = root    ALL=(ALL:ALL) ALL				
		NombreUsuario    ALL=(ALL:ALL) ALL
-  Adicionar linea  sudo crontab -e
	-	@reboot python3 DirectorioDelArchivo/Linux/server.py
