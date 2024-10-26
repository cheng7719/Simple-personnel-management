records = []

while True:
    print("\n--- 人事資料管理系統 ---")
    print("1. 新增資料")
    print("2. 查詢資料")
    print("3. 修改資料")
    print("4. 刪除資料")
    print("5. 顯示所有資料")
    print("6. 退出系統")
    print("------------------------")


    choice = input("請選擇功能: ")

    if choice == '1':
        while True:
            department = input("輸入部門: ")
            name = input("輸入姓名: ")
            age = input("輸入年齡: ")
            phone = input("輸入手機: ")

            record = {"部門": department, "姓名": name, "年齡": age, "手機": phone}
            records.append(record)
            print("資料已新增！")

            cont = input("是否繼續新增資料? (y/n): ").lower()
            if cont != 'y':
                break

    elif choice == '2':
        name = input("輸入要查詢的姓名: ")
        found = False
        for record in records:
            if record["姓名"] == name:
                print("\n--- 查詢結果 ---")
                print(f"{'部門':<8}{'姓名':<8}{'年齡':<4}{'手機':<10}")
                print(f"{'-'*45}")
                print(f"{record['部門']:<8}{record['姓名']:<8}{record['年齡']:<4}{record['手機']:<10}")
                found = True
                break
        if not found:
            print("查無此人")

    elif choice == '3':
            name = input("請輸入要修改的姓名: ")
            for record in records:
                if record["姓名"] == name:
                    print("\n當前資料:")
                    print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機':<15}")
                    print(f"{'-'*45}")
                    print(f"{record['部門']:<10}{record['姓名']:<10}{record['年齡']:<10}{record['手機']:<15}")

                    print("\n1. 修改部門")
                    print("2. 修改姓名")
                    print("3. 修改年齡")
                    print("4. 修改手機")

                    field_choice = input("請選擇要修改的欄位: ")

                    if field_choice == '1':
                        record["部門"] = input("請輸入新的部門: ")
                    elif field_choice == '2':
                        record["姓名"] = input("請輸入新的姓名: ")
                    elif field_choice == '3':
                        record["年齡"] = input("請輸入新的年齡: ")
                    elif field_choice == '4':
                        record["手機"] = input("請輸入新的手機: ")
                    else:
                        print("無效的選擇")

                    print("\n--- 更新後的資料 ---")
                    print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機':<15}")
                    print(f"{'-'*45}")
                    print(f"{record['部門']:<10}{record['姓名']:<10}{record['年齡']:<10}{record['手機']:<15}")
                    break
            else:
                print("查無此人")


    elif choice == '4':
        name = input("輸入要刪除的姓名: ")
        for i, record in enumerate(records):
            if record["姓名"] == name:
                print("\n找到的資料:")
                print(f"{'部門':<8}{'姓名':<8}{'年齡':<4}{'手機':<10}")
                print(f"{record['部門']:<8}{record['姓名']:<8}{record['年齡']:<4}{record['手機']:<10}")
                confirm = input("確定要"+name+"刪除資料嗎? (y/n):").lower()
                if confirm == 'y':
                    records.pop(i)
                    print(name+"資料已刪除！")

                    # 顯示剩餘資料
                    if records:
                        print("\n--- 剩餘的所有資料 ---")
                        print(f"{'部門':<8}{'姓名':<8}{'年齡':<4}{'手機':<10}")
                        for rec in records:
                            print(f"{'-'*45}")
                            print(f"{rec['部門']:<8}{rec['姓名']:<8}{rec['年齡']:<4}{rec['手機']:<10}")
                    else:
                        print("目前沒有任何資料")
                else:
                    print("操作已取消")
                break
        else:
            print("查無此人")

    elif choice == '5':
        if records:
            print("\n所有人員資料:")
            print(f"{'部門':<8}{'姓名':<8}{'年齡':<4}{'手機':<10}")
            print(f"{'-'*45}")
            for record in records:
                print(f"{record['部門']:<8}{record['姓名']:<8}{record['年齡']:<4}{record['手機']:<10}")
        else:
            print("目前沒有任何資料")

    elif choice == '6':
        print("系統已退出。")
        break

    else:
        print("輸入錯誤，請重新輸入。")
