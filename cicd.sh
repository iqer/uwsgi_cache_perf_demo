#! /usr/bin/env bash
# 打包镜像
docker build -t iqer/demo_uwsgi:v1 .
# 如果容器存在, 删除容器
docker rm -f mydemo-uwsgi
# 启动容器
docker run -d --name mydemo-uwsgi -p 5000:5000 iqer/demo_uwsgi:v1
# 引入cicd规范(demo)

# 最终进入容器命令行中
docker exec -it mydemo-uwsgi bash
