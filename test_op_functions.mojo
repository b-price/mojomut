from op_functions import math1, math2, math3, math4, math5, math6, math7, math8, math9
from testing import assert_true

fn main() raises:

    test_math1()
    test_math2()
    test_math3()
    test_math4()
    test_math5()
    test_math6()
    test_math7()
    test_math8()
    test_math9()


fn test_math1() raises:
    print("# test math1")
    var test1 = math1(2, 4)
    assert_true(test1 == 100, "Test failed for math1(2, 4)")

    var test2 = math1(4, 2)
    assert_true(test2 == 6, "Test failed for math1(4, 2)")

    var test3 = math1(0, 0)
    assert_true(test3 == 98, "Test failed for math1(0, 0)")

    var test4 = math1(5, 0)
    assert_true(test4 == 5, "Test failed for math1(5, 0)")

    var test5 = math1(-2, 3)
    assert_true(test5 == 96, "Test failed for math1(-2, 3)")

fn test_math2() raises:
    print("# test math2")
    var test1 = math2(5, 4)
    assert_true(test1 == -4, "Test failed for math2(5, 4)")

    var test2 = math2(4, 5)
    assert_true(test2 == -5, "Test failed for math2(4, 5)")

    var test3 = math2(0, 0)
    assert_true(test3 == 0, "Test failed for math2(0, 0)")

    var test4 = math2(5, 0)
    assert_true(test4 == 5, "Test failed for math2(5, 0)")

    var test5 = math2(-2, -3)
    assert_true(test5 == 1, "Test failed for math2(-2, -3)")

fn test_math3() raises:
    print("# test math3")
    var test1 = math3(3, 5)
    assert_true(test1 == 27000.0, "Test failed for math3(3, 5)")

    var test2 = math3(4, 2)
    assert_true(test2 == 8.0, "Test failed for math3(4, 2)")

    var test3 = math3(0, 0)
    assert_true(test3 == 0.0, "Test failed for math3(0, 0)")

    var test4 = math3(-5, 3)
    assert_true(test4 == -15.0, "Test failed for math3(-5, 3)")

    var test5 = math3(3, 0)
    assert_true(test5 == 27000.0, "Test failed for math3(3, 0)")

fn test_math4() raises:
    print("# test math4")
    var test1 = math4(6, 2)
    assert_true(test1 == 3.0, "Test failed for math4(6, 2)")

    var test2 = math4(4, 0)
    assert_true(test2 == 0.0, "Test failed for math4(4, 0)")

    var test3 = math4(0, 5)
    assert_true(test3 == 0.0, "Test failed for math4(0, 5)")

    var test4 = math4(-3, 2)
    assert_true(test4 == -0.3333333333333333, "Test failed for math4(-3, 2)")

    var test5 = math4(2, -3)
    assert_true(test5 == 0.22222222222222221, "Test failed for math4(2, -3)")

fn test_math5() raises:
    print("# test math5")
    var test1 = math5(3, 2)
    assert_true(test1 == 27, "Test failed for math5(3, 2)")

    var test2 = math5(4, 3)
    assert_true(test2 == 64, "Test failed for math5(4, 3)")

    var test3 = math5(0, 0)
    assert_true(test3 == 1, "Test failed for math5(0, 0)")

    var test4 = math5(5, 3)
    assert_true(test4 == 125, "Test failed for math5(5, 3)")

    var test5 = math5(-2, 3)
    assert_true(test5 == -8, "Test failed for math5(-2, 3)")

fn test_math6() raises:
    print("# test math6")
    var test1 = math6(3, 2)
    assert_true(test1 == 1, "Test failed for math6(3, 2)")

    var test2 = math6(4, 9)
    assert_true(test2 == 1, "Test failed for math6(4, 9)")

    var test3 = math6(0, 0)
    assert_true(test3 == 0, "Test failed for math6(0, 0)")

    var test4 = math6(5, 3)
    assert_true(test4 == 1, "Test failed for math6(5, 3)")

    var test5 = math6(-2, 3)
    assert_true(test5 == -1, "Test failed for math6(-2, 3)")

fn test_math7() raises:
    print("# test math7")
    var test1 = math7(3, 2)
    assert_true(test1 == 3.0, "Test failed for math7(3, 2)")

    var test2 = math7(5, 4)
    assert_true(test2 == 15.0, "Test failed for math7(5, 4)")

    var test3 = math7(0, 0)
    assert_true(test3 == 3.0, "Test failed for math7(0, 0)")

    var test4 = math7(5, 2)
    assert_true(test4 == -3.0, "Test failed for math7(5, 2)")

    var test5 = math7(2, 5)
    assert_true(test5 == 3.0, "Test failed for math7(2, 5)")

fn test_math8() raises:
    print("# test math8")
    var test1 = math8(7, 9)
    assert_true(test1 == 0, "Test failed for math8(7, 9)")

    var test2 = math8(5, 21)
    assert_true(test2 == 0, "Test failed for math8(5, 21)")

    var test3 = math8(0, 0)
    assert_true(test3 == 0, "Test failed for math8(0, 0)")

    var test4 = math8(5, 9)
    assert_true(test4 == 0, "Test failed for math8(5, 9)")

    var test5 = math8(2, 3)
    assert_true(test5 == 0, "Test failed for math8(2, 3)")

fn test_math9() raises:
    print("# test math9")
    var test1 = math9(8, 8)
    assert_true(test1 == True, "Test failed for math9(8, 8)")

    var test2 = math9(8, 9)
    assert_true(test2 == False, "Test failed for math9(8, 9)")

    var test3 = math9(8, 7)
    assert_true(test3 == False, "Test failed for math9(8, 7)")

    var test4 = math9("hello", "hello")
    assert_true(test4 == True, "Test failed for math9('hello', 'hello')")

    var test5 = math9("hello", "world")
    assert_true(test5 == True, "Test failed for math9('hello', 'world')")
