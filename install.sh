#!/bin/bash

testPath="./images"
if [[ ! -d "$testPath" ]]; then
    echo "文件夹不存在"
else
    #h2 "[Step $item]: loading Harbor images ..."; let item+=1
	#docker load -i ./test/*.tar
	for file_a in ${testPath}/*
	do 
	temp_file=`basename $file_a` 
	docker load -i ${testPath}/$temp_file 
	done
fi

docker-compose up -d
