#! /bin/bash
#====================================================================
# Script per la predisposizione del nuovo anno
# nel server LTSP della scuola
#
#
# v. 1.0 - (it) 17/06/2011 - ivan@riminilug.it
#
#
# TODO: 
#====================================================================
set -u

usage ()
{
	echo "Uso: $0 <anno-anno>"
	echo "esempio: $0 2011-2012 [prima_sezione] [ultima_sezione]"
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
	  SCHOOL_YEAR=$1

      if [ -n $2 ]; then
        S_START=$2
      else
        S_START="a"
      fi

      if [ -n $3 ]; then
        S_END=$3
      else
        S_END="z"
      fi

	fi
else
    usage;
fi


echo "NUOVO ANNO: $SCHOOL_YEAR - sezioni $S_START - $S_END"
errors=0

#-----------------------------------------------------------------
# Cancella tutti gli utenti appartenenti al gruppo  students
#   questo comando cancella anche le home directory!!!
#-----------------------------------------------------------------
usr_list=`grep ^students: /etc/group|awk -F":" {'print $4}'`
#echo ">>> Processo il gruppo students che contiene i seguenti utenti:"
#echo "    [$usr_list]"

ifstmp=$IFS
IFS=","
for usr_name in $usr_list
do
	echo ">>> Elimino l'utente: $usr_name"
    deluser --remove-home $usr_name
    errors=$(($errors+$?))
done
IFS=$ifstmp


#-----------------------------------------------------------------
# imposta l'elenco delle classi
#-----------------------------------------------------------------

classes_list=""
for cl in $(eval echo {$S_START..$S_END})
do
    classes_list="classe_1$cl classe_2$cl classe_3$cl"


    #-----------------------------------------------------------------
    # Cancella le precedenti directory delle classi 
    #-----------------------------------------------------------------
    for cls in $classes_list
    do

        rm -Rf /home/$cls
        errors=$(($errors+$?))
    done

    #-----------------------------------------------------------------
    # Ricrea le nuove classi (gruppi e home directory)
    #-----------------------------------------------------------------
    echo "DEBUG > $cls"

    eval  $(dirname $0)/create_classes.sh $classes_list
    errors=$(($errors+$?))
done

if [ $errors -eq 0 ]; then
  echo $SCHOOL_YEAR > /home/ANNO_CORRENTE
  echo "-----------------------------------"
  echo "[SCR1]Script completato con successo!"
  echo "-----------------------------------"
else 
  echo "[SCR1]ERR: Si sono verificati $errors errori!"
fi

