from main import Add, Multiply

def TestAdd():
        assert Add(2,3) == 5
        assert Add(5, 5) == 10
        print("Add Function works correctly")

def TestMultiply():
    assert Multiply(5, 5) == 25
    print("Multiply function works properly")

if __name__ == '__main__':
        TestAdd()