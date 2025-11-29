import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

class DatabaseConnector:
    def __init__(self, user, password, host, port, dbname, db_type="postgresql"):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.dbname = dbname
        self.db_type = db_type.lower()

        # 构建数据库连接字符串
        self.db_url = self._get_db_url()

        # 创建数据库连接引擎
        self.engine = create_engine(self.db_url)

    def _get_db_url(self):
        """
        根据不同数据库类型，生成数据库连接URL
        """
        if self.db_type == "postgresql":
            return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"
        elif self.db_type == "mysql":
            return f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"
        elif self.db_type == "sqlite":
            return f"sqlite:///{self.dbname}"
        else:
            raise ValueError("Unsupported database type")

    def fetch_data(self, query):
        """
        执行 SQL 查询并将结果加载到 DataFrame 中
        """
        try:
            # 使用 pandas 直接从数据库读取数据
            return pd.read_sql(query, self.engine)
        except SQLAlchemyError as e:
            print(f"数据库查询失败: {e}")
            return None

    def close_connection(self):
        """
        关闭数据库连接
        """
        try:
            self.engine.dispose()  # 关闭连接池
            print("数据库连接已关闭。")
        except Exception as e:
            print(f"关闭数据库连接失败: {e}")
