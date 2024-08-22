#!/bin/bash

# Author: Ang-l
# GitHub: https://github.com/Ang-l/fastapi-template
# Date: 2024-03-10
# Email: lijiang_lja@163.com

APP_DIR="application"
BASE_DIR="$(dirname "$0")"
DATABASE_FILE="$BASE_DIR/db/base.py"
MAIN_FILE="$BASE_DIR/main.py"

create_app() {
    local appname=$1

    if [ -z "$appname" ]; then
        echo "未提供应用名称，请终止进程..."
        exit 1
    fi

    local DIRECTORY="$BASE_DIR/$APP_DIR/$appname"
    if [ -d "$DIRECTORY" ]; then
        echo "应用 $appname 已存在，请终止进程..."
        exit 1
    fi

    mkdir -p "$DIRECTORY"
    touch "$DIRECTORY/__init__.py" "$DIRECTORY/model.py" "$DIRECTORY/views.py" "$DIRECTORY/schemas.py"

    add_mysql_info "$appname"

    add_router "$appname"
}

add_mysql_info() {
    local appname=$1
    cat << EOF >> "$DATABASE_FILE"
from application.$appname import model
EOF
}

add_router() {
    local appname=$1
    cat << EOF >> "$MAIN_FILE"

from application.$appname import views as view_$appname

app.include_router(
    view_$appname.router,
    prefix="/v1/$appname",
    responses={404: {"description": "访问的页面不存在"}, 405:{"description": "请求方式异常"}},
)
EOF

    cat << EOF >> "$BASE_DIR/$APP_DIR/$appname/views.py"
from fastapi import APIRouter

router = APIRouter()
EOF
}

main() {
    local appname=$1
    create_app "$appname"
}

main "$@"
