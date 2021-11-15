class Utils:
    @staticmethod
    def div(vec, num):
        vec[0] /= num
        vec[1] /= num
        vec[2] /= num

    @staticmethod
    def mul(vec, num):
        vec[0] *= num
        vec[1] *= num
        vec[2] *= num

    @staticmethod
    def add(vec, num):
        vec[0] += num
        vec[1] += num
        vec[2] += num

    @staticmethod
    def sub(vec, num):
        vec[0] -= num
        vec[1] -= num
        vec[2] -= num

    @staticmethod
    def mul_vec(vec, other):
        vec[0] *= other[0]
        vec[1] *= other[1]
        vec[2] *= other[2]

    @staticmethod
    def div_vec(vec, other):
        vec[0] /= other[0]
        vec[1] /= other[1]
        vec[2] /= other[2]

    @staticmethod
    def add_vec(vec, other):
        vec[0] += other[0]
        vec[1] += other[1]
        vec[2] += other[2]

    @staticmethod
    def sub_vec(vec, other):
        vec[0] -= other[0]
        vec[1] -= other[1]
        vec[2] -= other[2]

    
    @staticmethod
    def div_r(vec, num):
        return [vec[0] / num,
                vec[1] / num,
                vec[2] / num]

    @staticmethod
    def mul_r(vec, num):
        return [vec[0] * num,
                vec[1] * num,
                vec[2] * num]

    @staticmethod
    def add_r(vec, num):
        return [vec[0] + num,
                vec[1] + num,
                vec[2] + num]

    @staticmethod
    def sub_r(vec, num):
        return [vec[0] - num,
                vec[1] - num,
                vec[2] - num]

    @staticmethod
    def div_vec_r(vec, other):
        return [vec[0] / other[0],
                vec[1] / other[1],
                vec[2] / other[2]]

    @staticmethod
    def mul_vec_r(vec, other):
        return [vec[0] * other[0],
                vec[1] * other[1],
                vec[2] * other[2]]

    @staticmethod
    def add_vec_r(vec, other):
        return [vec[0] + other[0],
                vec[1] + other[1],
                vec[2] + other[2]]

    @staticmethod
    def sub_vec_r(vec, other):
        return [vec[0] - other[0],
                vec[1] - other[1],
                vec[2] - other[2]]

    @staticmethod
    def normalize(vec):
        mag = Utils.magnitude(vec)

        if mag == 0: return (0, 0, 0)

        Utils.div(vec, mag)

    @staticmethod
    def normalized(vec):
        mag = Utils.magnitude(vec)

        if mag == 0: return (0, 0, 0)

        return Utils.div_r(vec, mag)

    @staticmethod
    def magnitude(vec):
        return Utils.sqrmagnitude(vec)**.5

    @staticmethod
    def sqrmagnitude(vec):
        return vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2

    @staticmethod
    def dot(vec, other):
        return vec[0] * other[0] + vec[1] * other[1] + vec[2] * other[2]

    @staticmethod
    def cross(vec, other):
        return [vec[1] * other[2] - other[1] * vec[2],
                other[0] * vec[2] - vec[0] * other[2],
                vec[0] * other[1] - other[0] * vec[1]]