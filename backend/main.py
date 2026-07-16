from api import generate_content


product = """
产品：迷你吹风机

特点：
- 小巧便携
- 出差旅行方便
- 风力集中
- 快速干发
- 不容易烫头皮
"""


result = generate_content(product)

print(result)
