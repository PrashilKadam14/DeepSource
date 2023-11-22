import cProfile

def inefficient_function():
    result = 0
    for i in range(1000000):
        result += i
    return result

def main():
    # Profile the inefficient function
    cProfile.run('inefficient_function()', sort='cumulative')

if __name__ == "__main__":
    main()
