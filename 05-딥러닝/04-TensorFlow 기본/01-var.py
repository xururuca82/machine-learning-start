import tensorflow as tf

# 상수 정의하기
a = tf.constant(120, name="a")
b = tf.constant(130, name="b")
c = tf.constant(140, name="c")
# 변수 정의하기
v = tf.Variable(0, name="v")

# 데이터 플로우 그래프 정의하기
calc_op = a + b + c
assing_op = tf.assign(v, calc_op)

# 세션 실행하기
sess = tf.Session()
sess.run(assing_op)

# v의 내용 출력하기
print(sess.run(v))