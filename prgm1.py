value = "42"
match value:
    case "one":
        result = 1
    case "two":
        result = 2
    case "three" | "four":
        result = (3,4)
    case _ :
        result = -1
        print(result)