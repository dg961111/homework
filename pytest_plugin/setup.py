from setuptools import setup, find_packages

setup(
    name='pytest_log',
    url='https://github.com/xxx/pytest-log',
    version='1.0',
    author="dong",
    author_email='275915667@qq.com',
    description='set your encoding and logger',
    long_description='Show Chinese for your mark.parametrize(). Define logger variable for getting your log',
    classifiers=[  # 分类索引 ，pip 对所属包的分类
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.8',
    ],
    license='proprietary',
    packages=find_packages(),
    keywords=[
        'pytest', 'py.test', 'pytest_log',
    ],
    # 需要安装的依赖
    install_requires=[
        'pytest'
    ],
    # 入口模块 或者入口函数
    entry_points={
        'pytest11': [
            'pytest-log = pytest_log.main',
        ]
    },
    zip_safe=False
)
