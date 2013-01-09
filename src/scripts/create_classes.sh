#!/bin/bash
#====================================================================
# Sript per la creazione dei gruppi <classe> e delle directory
# accessorie nel server LTSP della scuola
#
# 
# v. 1.0 - (it) 10/09/2010 - ivan@riminilug.it
# v. 1.1 - (it) 29/06/2011 - ivan@riminilug.it
#
# -------------------------------------------------------------------
# Per l'utilizzo dello script passare come parametro l'elenco delle
# classi separate da spazi
#
#
#====================================================================
set -u


#------------------------------------------------
# Controllo se l'esecutore ha i permessi di root
#------------------------------------------------
if [ `id -u` -ne 0 ]; then
  echo "ERRORE: solo l'utente root puo' eseguire questo script"
  exit 250
fi

#------------------------------------------------
# Controllo dei parametri
#------------------------------------------------
if [ "$#" -gt 0 ]; then
  echo "Avvio script..... "
else
    echo "Errore: Passare almeno un nome di classe!"
    exit 251
fi


errors=0

#------------------------------------------------
# Modifica ai files di cfg 
#------------------------------------------------

if [ -z "$(grep "DIR_MODE=0750" /etc/adduser.conf)" ]; then
  echo "DIR_MODE=0750" >> /etc/adduser.conf
fi

if [ -z "$(grep "^umask.*027" /etc/profile)" ]; then
  echo "umask 027" >> /etc/profile
  errors=$(($errors+$?))

fi

if [ -z "$(grep "^UMASK.*027" /etc/login.defs)" ]; then
  echo "UMASK 027" >> /etc/login.defs
  errors=$(($errors+$?))
fi

#------------------------------------------------------
# creo il gruppo teacher e la directory /home/teachers 
#------------------------------------------------------

addgroup teachers
#errors=$(($errors+$?)) 
#non processo l'errore in quanto non posso discriminare gruppo già presente

dir_name=/home/teachers
echo "Creo la directory: ["$dir_name"]" 
mkdir -p -m2770 $dir_name
errors=$(($errors+$?))

chown root:teachers $dir_name
errors=$(($errors+$?))

#------------------------------------------------------
# creo il gruppo students 
#------------------------------------------------------

addgroup students
#errors=$(($errors+$?)) 
#non processo l'errore in quanto non posso discriminare gruppo già presente



	
#-------------------------------------------
# Aggiungo un gruppo per ogni classe passata
# e un gruppo per gli insegnanti di tale classe
#-------------------------------------------
for nome_classe in $@
do

  echo "Aggiungo il gruppo: ["$nome_classe"]" 
  addgroup $nome_classe
  #errors=$(($errors+$?))
  #non processo l'errore in quanto non posso discriminare gruppo già presente

  echo "Aggiungo il gruppo: [t_"$nome_classe"]" 
  addgroup t_$nome_classe
  #errors=$(($errors+$?))
  #non processo l'errore in quanto non posso discriminare gruppo già presente
done

#------------------------------------------------
# creo una directory in /home per ogni classe 
#------------------------------------------------
for nome_classe in $@
do
  dir_name=/home/$nome_classe
  echo "Creo la directory: ["$dir_name"]" 
  mkdir -p -m2770 $dir_name
  errors=$(($errors+$?))

  chown root:$nome_classe $dir_name
  errors=$(($errors+$?))

done


if [ $errors -eq 0 ]; then
  echo "-----------------------------------"
  echo "[SCR2]Script completato con successo!"
  echo "-----------------------------------"
else 
  echo "[SCR2]ERR: Si sono verificati $errors errori!"
  exit 200
fi

