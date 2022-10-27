from math import sin, cos, sqrt, atan2, radians

"""
>>> casa = (-20.9469873, -48.4601433)
>>> vo = (-20.9318346, -48.49424279999999)
>>> mae = (-20.9468284, -48.458582)
"""

R = 6371.0710

def harvesine(point_a, point_b, rounded=4):
    ''' haversine(θ) = sin²(θ/2)
    a = sin²(φB - φA/2) + cos φA * cos φB * sin²(λB - λA/2)
    c = 2 ⋅ atan2( √a, √(1−a) )
    d = R ⋅ c
    '''
    if point_a[0] == point_b[0] and point_a[1] == point_b[1]:
        return 0.0
    phi_a = radians(point_a[0])
    phi_b = radians(point_b[0])
    delta_phi = phi_b - phi_a
    delta_lambda = radians(point_b[1]) - radians(point_a[1])
    a = sin(delta_phi / 2.0)**2 + cos(phi_a) * cos(phi_b) * sin(delta_lambda / 2.0)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    d = R * c
    return round(d, rounded)


def harvesine_geocep(point_a, point_b, rounded=4):
    phi_a = point_a[0]
    phi_b = point_b[0]
    delta_phi = phi_b - phi_a
    delta_lambda = point_b[1] - point_a[1]
    a = sin(delta_phi / 2.0)**2 + cos(phi_a) * cos(phi_b) * sin(delta_lambda / 2.0)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    d = R * c
    return round(d, rounded)


