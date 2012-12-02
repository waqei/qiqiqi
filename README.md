汽配商城展示页

创建数据库

    CREATE DATABASE `name` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci



south
    #检测对models的更改
    python manage.py schemamigration car --auto

    #将更改反应到数据库
    python manage.py migrate car