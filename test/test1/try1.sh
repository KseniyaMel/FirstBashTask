#!/bin/bash
makesmth()
{
if [ "$(ls -A "$1" 2> /dev/null)" == "" ]
then
return
else
for var in $1/*
do
if [ -d $var ]
then
makesmth $var
elif [ -f $var ]
then
dir=${var%/*}
xbase=${var##*/}
name=${xbase%.*}
size=$(wc -c "$var" | awk '{print $1}')
tip=${var##*.}
data=$(stat -c %y $var)
lohg=$(mediainfo --Inform="General;%Duration%" $var)
let "long = lohg / 1000"
echo -e "$name \t $dir \t $tip \t $size \t $data \t $long" >>  result.xls
fi
done
fi
}

read -p 'Give me way ' way
if [ -d $way ]
then
touch result.xls
echo -e "Filename \t Filepath \t Extension \t Size (bytes) \t Modify date \t Duration (sec)" >>  result.xls
makesmth $way
else
echo "It isn't way"
fi

