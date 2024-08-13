from sqlalchemy import Column, String, Integer, ForeignKey, Table, Enum as SqlEnum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from db.BaseMixin import BaseMixin, Base, Basics


class Blog(BaseMixin, Base):
    __tablename__ = "blogs"
    
    title = Column(String(100), nullable=False, comment="博客标题")
    content = Column(String(2000), nullable=False, comment="博客内容")


class Departments(BaseMixin, Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False, comment="部门名")
    description = Column(String(256), comment="部门描述")
    
    # 自引用，指向上级部门
    parent_id = Column(Integer, ForeignKey('departments.id'), nullable=True)
    parent = relationship("Departments", remote_side=[id], backref="children")

    users = relationship('Users', back_populates='department')

# 用户表
class Users(BaseMixin, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, comment="用户名")
    password = Column(String(256), nullable=False, comment="密码")
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=True)

    department = relationship('Departments', back_populates='users')
    roles = relationship('Roles', secondary='user_roles', back_populates='users')

# 角色表
class Roles(BaseMixin, Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False, comment="角色名")
    description = Column(String(256), comment="角色描述")

    users = relationship('Users', secondary='user_roles', back_populates='roles')
    permissions = relationship('Permissions', secondary='role_permissions', back_populates='roles')
    menu_permissions = relationship('Menus', secondary='role_menu_permissions', back_populates='roles')
    button_permissions = relationship('Buttons', secondary='role_button_permissions', back_populates='roles')
    data_permissions = relationship('DataPermissions', secondary='role_data_permissions', back_populates='roles')

# 用户角色中间表
user_roles = Table(
    'user_roles', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True)
)

# 权限表
class Permissions(BaseMixin, Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False, comment="权限名")
    description = Column(String(256), comment="权限描述")

    roles = relationship('Roles', secondary='role_permissions', back_populates='permissions')

# 角色权限中间表
role_permissions = Table(
    'role_permissions', Base.metadata,
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True),
    Column('permission_id', Integer, ForeignKey('permissions.id'), primary_key=True)
)

# 菜单表
class Menus(BaseMixin, Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False, comment="菜单名")
    description = Column(String(256), comment="菜单描述")
    buttons = relationship('Buttons', back_populates='menu')

# 按钮表
class Buttons(BaseMixin, Base):
    __tablename__ = "buttons"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False, comment="按钮名")
    menu_id = Column(Integer, ForeignKey('menus.id'), nullable=False)
    description = Column(String(256), comment="按钮描述")

    menu = relationship('Menus', back_populates='buttons')

class DataPermissionScope(str, SqlEnum):
    OWN = "own"            # 自己的数据
    DEPARTMENT = "department"  # 部门下的数据
    ALL = "all"            # 全部数据

class DataPermissions(BaseMixin, Base):
    __tablename__ = "data_permissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False, comment="数据权限名")
    description = Column(String(256), comment="数据权限描述")
    # scope = Column(Enum(DataPermissionScope), default=DataPermissionScope.OWN, nullable=False)
    # cope = Column(SqlEnum(DataPermissionScope), default=DataPermissionScope.OWN, nullable=False)
    table_name = Column(String(50), nullable=False) 

    # 关联角色
    roles = relationship('Roles', secondary='role_data_permissions')

# 角色-菜单权限中间表
role_menu_permissions = Table(
    'role_menu_permissions', Base.metadata,
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True),
    Column('menu_id', Integer, ForeignKey('menus.id'), primary_key=True)
)

# 角色-按钮权限中间表
role_button_permissions = Table(
    'role_button_permissions', Base.metadata,
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True),
    Column('button_id', Integer, ForeignKey('buttons.id'), primary_key=True)
)

role_data_permissions = Table(
    'role_data_permissions', Base.metadata,
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True),
    Column('data_permission_id', Integer, ForeignKey('data_permissions.id'), primary_key=True),
    Column('department_id', Integer, ForeignKey('departments.id'), nullable=True)
)