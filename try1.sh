#!/bin/bash
makesmth()
{
	if [ "$(ls -A "$1" 2> /dev/null)" == "" ] # проверяем пустая ли папка
	then
	return
	else
		for var in $1/* # перебор файлов и директорий
		do
			if [ -d $var ]
			then
			makesmth $var
			elif [ -f $var ]
			then
			dir=${var%/*} # получаем путь к файлу
			xbase=${var##*/} 
			name=${xbase%.*} # получаем имя файла
			size=$(wc -c "$var" | awk '{print $1}') # получаем размер файла 
			tip=${var##*.} # получаем расширение файла
			data=$(stat -c %y $var) # получаем дату изменения
			lohg=$(mediainfo --Inform="General;%Duration%" $var) # получаем длительность аудио и видео файлов в микросекундах
			let "long = lohg / 1000"
			echo -e "$name \t $dir \t $tip \t $size \t $data \t $long" >>  result.xls # записываем результат
			fi
		done
	fi
}

IFS=$'\t' # изменяем разделение полей
read -p 'Give me the way ' way
if [ -d $way ] # проверяем существует ли директория
then
if [ -f result.xls ] # создаем результирующий файл
then
rm result.xls
touch result.xls
else
touch result.xls
fi
echo -e "Filename \t Filepath \t Extension \t Size (bytes) \t Modify date \t Duration (sec)" >>  result.xls
makesmth $way
else
echo "It isn't way"
fi


