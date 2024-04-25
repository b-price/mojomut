from arithmetic import math1, math2, math3
from testing import assert_true

# fn main() raises:
#     test_convert()


# fn test_convert() raises:
#     let test = math1(5, 6)
#     let expected: Int = 11

#     return assert_true(test == expected, "Something went wrong")

fn main() raises:
    print("# test math1")
    print(test_math1())

    print("# test math2")
    print(test_math2())

    print("# test math3")
    print(test_math3())

fn test_math1() raises:
    let test = math1(5, 5)
    return assert_true(test == 10, "Something went wrong")

fn test_math2() raises:
    let test2 = math2(5, 5)
    return assert_true(test2 == -4, "Something went wrong")

fn test_math3() raises:
    let test3 = math3(5, 5)
    return assert_true(test3 == 25, "Something went wrong")