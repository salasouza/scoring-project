#!/bin/bash

echo -e "\e[1;34m Oi, qual a boa de hoje? \e[0m"

git status

git add .

dt=$(date +'%Y-%m-%d : %H-%M')

git commit -m "alterações realizadas em $dt"

git push

echo -e "\e[1;31m SUCCESS!!! \e[0m"