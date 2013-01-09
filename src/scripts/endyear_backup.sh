#! /bin/bash
#====================================================================
# Script per la creazione del bakup di fine anno
# nel server LTSP della scuola
#
#
# v. 1.0 - (it) 10/06/2011 - ivan@riminilug.it
#
#
# TODO: redirigere stdout/err del comando di copia su file di log, da cancellare se ok
#====================================================================
set -u


usage ()
{
	echo "Uso: $0 <percorso_backup>"
	echo "esempio: $0 /backup/2010_2011"
	exit 250
}
#------------------------------------------------
# Controllo se l'esecutore ha i permessi di root
#------------------------------------------------
if [ `id -u` -ne 0 ]; then
	echo "ERRORE: solo l'utente root puo' eseguire questo script"
	exit 1
fi

#------------------------------------------------
# Controllo dei parametri
#------------------------------------------------


if [ $# -gt 0 ]; then
  
	if [ "$1" = "" ]
	then
		usage;
	else
	  PATH_BACKUP=$1
	fi
else
    usage;
fi



#-----------------------------------------------------------------
# Verifica la presenza del path di destinazione o tenta di crearlo
#-----------------------------------------------------------------
if [ -d $PATH_BACKUP ] 
then
    # la directory esiste, verifico se posso scrivere
    if [ ! -w $PATH_BACKUP ]; then
    	echo "ERRORE: Impossibile ottenere il permesso di scrittura in $PATH_BACKUP"
        exit 2
    fi 
else
    # la directory non esiste, tento la creazione 
    mkdir -p $PATH_BACKUP
    if [ $? -ne 0 ]
    then
    	echo "ERRORE: impossibile creare la directory $PATH_BACKUP"
    	exit 3
    fi
fi

#-----------------------------------------------------------------
# Esegue la copia del file /etc/group nel path indicato
#-----------------------------------------------------------------
mkdir -p $PATH_BACKUP/etc && cp --remove-destination /etc/group $PATH_BACKUP/etc/

if [ $? -ne 0 ]; then			
    echo "ERRORE: durante la copia del file /etc/group in $PATH_BACKUP - Errore $?" 
  
    exit 10
fi

#-----------------------------------------------------------------
# Esegue la copia delle home directory nel path indicato
#-----------------------------------------------------------------
tar cp  --exclude-caches-all --exclude='.*' /home | (tar xp -C $PATH_BACKUP)
chmod 755 $PATH_BACKUP
		
if [ $? -eq 0 ]; then			
  echo "----------------------------------------------------"
  echo "[SCR3]Script completato con successo!"
  echo "----------------------------------------------------"
else
  echo "----------------------------------------------------"
  echo "[SCR3]Script completato con errore!"
  echo "----------------------------------------------------"
  exit 50
fi
