"""
celery的任务存放文件

#### 任务示例

@celery_app.task
def test(task_id):
    print(task_id)


#### 启动异步任务
task_id = 123

test.delay(task_id)   ## 输出 123


#### 10秒后启动异步任务
task_id = 123

test.apply_async((task_id ,), countdown=10)     ## 10秒后输入 123


### 查询任务执行状态
from celery.result import AsyncResult

task_id = 123
result = AsyncResult(task_id, app=celery_app)      ### result.state


### 移除任务

task_id = 123
celery_app.control.revoke(task_id, terminate=True)

"""

from celery_app import celery_app

@celery_app.task
def test(task_id):
    print(task_id)









