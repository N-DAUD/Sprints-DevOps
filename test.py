import sprints as sp


def Testcase1():
    List1  = [4, 5, 6, 7, 8, 9]
    List2 = [4.1, 5.2, 6.3, 7.5, 9.7]
    output = sp.myFunc(List1, List2)
    assert output[0] == (6+4+8) / 3, f"Should be {(8+4+6) / 3}"
    assert output[1] == 10.1, "Should be 9.7"


def Testcase2():
    List1  = [1, 2, 3, 4, 5]
    List2  = [-100.0, -120.0, 10.0, -500.0]
     output = sp.myFunc(List1, List2)
    assert output[0] == (1+2+3+4+5) / 5, f"Should be {(1+2+3+4+5) / 5}"
    assert output[1] == 10.0, "Should be 10.0"


def Testcase3():
    List1  = [1, 2, 3, "sprint", "sppp", 'pp', 1.0, 2.0, 4, 5, 6]
    List2 = [1.5, "sprint", 1, 2.5, 300, 2.7, 7.5, 8.5]
     output = sp.myFunc(List1, List2)
    assert output[0] == (2+4+6) / 3, f"Should be {(2+4+6) / 3}"
    assert output[1] == 8.5, "Should be 8.5"


if __name__ == "__main__":
    
    Testcase1()
    
    Testcase2()
    
    Testcase3()
    
  print("Task 02: Tests Passed")