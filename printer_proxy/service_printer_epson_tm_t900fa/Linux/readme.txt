Instrucciones de instalacion:

Linux
Paso 1 - Copiar la carpeta service_printer_epson_tm_t900fa/Linux en un directorio dentro de cada computadora con sistema Linux a la cual se quiera conectar 
el impresor fiscal Epson 
Ej. /home/usuario/service_printer_epson_tm_t900fa/Linux



#Paso 2 - Instalar requerimientos
cd /carpeta donde se copio service_printer_epson_tm_t900fa/Linux. Ej. /home/usuario/service_printer_epson_tm_t900fa/Linux


cd /home/usuario/service_printer_epson_tm_t900fa/Linux
pip3 install -r requirements.txt


sudo nano /etc/sudoers:
#agregar despues de la linea = root    ALL=(ALL:ALL) ALL				
NombreUsuario    ALL=(ALL:ALL) ALL

#Adicionar linea  sudo crontab -e 

@reboot python3 /home/usuario/service_printer_epson_tm_t900fa/Linux/server.py


Soporte: soporte@pronexo.com