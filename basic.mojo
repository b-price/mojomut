fn main():
    var a: Int = 0
    var b: Int = 1
    var c: Int = 32
    var d: Int = 64
    var e: Int = -128
    var f: Int = 1234567890

    print(add(a, b))
    print(add(c, b))
    print(add(c, f))
    print(add(d, b))
    print(add(c, c))
    print(add(b, a))

fn add(x: Int, y: Int) -> Int:
   var z = x + y
   return z