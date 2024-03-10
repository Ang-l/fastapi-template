import sys, os


class APPExistsError(Exception):
    def __init__(self, message="The app already exists and cannot be created. Love you exists"):
        self.message = message
        super().__init__(self.message)

class Create:
    def __init__(self, app) -> None:
        self.app_name = app
        self.parent_dir = "application"
        self.app_dir =  os.path.join(self.parent_dir, self.app_name)

    def main(self, ):
        self.check_app_exists()
        self.create_folder()
        self.create_file()
        self.increase_app_route()
        self.increase_app_model()

    def increase_app_route(self, ) -> None:
        # app文件写入view层面需要的路由信息
        with open(os.path.join(self.app_dir, "views.py"), 'a') as f:
            print('from fastapi import APIRouter', file=f)
            print('', file=f)
            print('', file=f)
            print('router = APIRouter()', file=f)

        # 主文件引入路由信息
        with open('main.py', 'a') as f:
            print('', file=f)
            print(f'from application.{self.app_name} import views as view_{self.app_name}', file=f)
            print('', file=f)
            print('', file=f)
            print(f'app.include_router(view_{self.app_name}.router,prefix="/v1/{self.app_name}")', file=f)

    def increase_app_model(self, ) -> None:
        with open('db/base.py', 'a') as f:
            print('', file=f)
            print(f'from application.{self.app_name} import model', file=f)
            print('', file=f)
    
    def create_file(self, ) -> None:
        """
        Create the required files for the app
        """
        files = ["__init__.py", "model.py", "schemas.py", "app.py", "test.py", "views.py"]
        [open(os.path.join(self.app_dir, file_name), 'w').close() for file_name in files]

    def create_folder(self, ) -> None:
        """
        Create a folder for the app
        """
        os.makedirs(self.app_dir, exist_ok=True)
    
    def check_app_exists(self, ) -> None:
        """
        Check if the app exists to avoid duplicate creation
        The inspection method is: whether a folder named app exists
        If there is a direct exception thrown
        """
        if os.path.exists(self.app_dir):
            raise APPExistsError()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("未输入app名称将停止进程.....")
        sys.exit(1)

    app_name = sys.argv[1]
    c = Create(app_name)
    c.main()