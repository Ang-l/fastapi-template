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
    add_mysql_info
    add_router
}

mkdir_app_dir() {
    mkdir -p "$(dirname "$0")/application/$appname/"
}

touch_py() {
    touch $DIRECTORY/__init__.py $DIRECTORY/model.py $DIRECTORY/views.py $DIRECTORY/schemas.py 
}

add_mysql_info() {

    cat << EOF >> db/base.py

from application.$appname import model
EOF

}

add_router() {
    cat << EOF >> main.py

from application.$appname import views as view_$appname

app.include_router(
    view_$appname.router,
    prefix="/v1/$appname",
    responses={404: {"description": "访问的页面不存在"}, 405:{"description": "请求方式异常"}},

)

EOF

   cat << EOF >> application/$appname/views.py
from fastapi import APIRouter



router = APIRouter()
EOF


}

create_app
