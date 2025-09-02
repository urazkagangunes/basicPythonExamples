while True:
    try:
        x = int(input("x = "))
        y = int(input("y = "))
        print(x / y)
    # except (ZeroDivisionError, ValueError) as ex:
    #     print("x ve y sayı olmalıdır. y sıfır olamaz.")
    #     print(ex)
    except Exception as e:
        print("bilinmeyen bir hata oluştu.")
        print(e)
    else:
        print("her şey yolunda.")
        break
    finally:
        print("finally blogu her halukarda çalıştı.")