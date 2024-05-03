
fn main():
    var a: Int = 1
    var b: Int = 2
    var c: Int = 4
    var d: Int = 8
    var e: Int = 16
    var f: Int = -4
    var o: PythonObject = 4
    var p: PythonObject = 7

    print(math1(-2, 3))
    print(math2(5, 0))
    print(math3(3, 0))
    print(math4(2, -3))
    print(math5(0, 0))
    print(math7(5, 2))
    print(math8(2, 3))
    print(math9(8, 9))


fn math1(x: Int, y: Int) -> Int:
    var z: Int = x + y
    if x < 3:
        z = x + 98
    return z

fn math2(x: Int, y: Int) -> Int:
    var z: Int = x - y
    if y > 3:
        z = x - 9
    return z

fn math3(x: Int, y: Int) -> Float64:
    var z: Float64 = x * y
    if x == 3:
        z = x * 9000
    return z

fn math4(x: Int, y: Int) -> Float64:
    var z: Float64 = 0
    if y != 0:
        z = x / y
        if x < 3:
            z = x / 9
    return z

fn math5(x: Int, y: Int) -> Int:
    var z: Int = x ** y
    if x >= 3:
        z = x ** 3
    return z

fn math6(x: Int, y: Int) -> Int:
    var z: Int = x // y
    if x >= 3 or y == 9:
        z = x // 3
    return z

fn math7(x: Int, y: Int) -> Float64:
    var z: Float64 = x + y * 3 - (x + 8) - 1
    if x >= 3 and y != 2:
        z = x * 3
    elif not(x == 5):
        z = +3
    return z

fn math8(x: Int, y: Int) -> Int:
    var z: Int = x >> y
    if x != 7 | y == 9:
        z = y << x
    elif y == 21 & x != 55:
        z = x ^ y
    return z

fn math9(x: PythonObject, y: PythonObject) -> Bool:
    var z: PythonObject = 8
    if x is y:
        return True
    elif z is not x:
        return True
    else:
        return False
