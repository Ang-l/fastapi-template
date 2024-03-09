# Author: Ang-l
# github: https://github.com/Ang-l/fastapi-template
# Date: 2024-03-10
# email: lijiang_lja@163.com

#!/bin/bash

appname=$1

if [ -z "$appname" ]; then
    echo "app名称不存在将终止进程...."
    exit
fi

DIRECTORY="$(dirname "$0")/application/$appname/"

if [ -d "$DIRECTORY" ]; then
  echo "app $appname 已存在即将终止进程...."
  exit
fi


create_app(){
    mkdir_app_dir
    touch_py
}

mkdir_app_dir() {
    mkdir -p "$(dirname "$0")/application/$appname/"
}

touch_py() {
    touch $DIRECTORY/__init__.py $DIRECTORY/model.py $DIRECTORY/views.py $DIRECTORY/schemas.py 
}

create_app
