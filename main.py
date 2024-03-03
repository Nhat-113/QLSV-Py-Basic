import Students as st

print("CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
action = 1

while action != 0:
    print("------------------------")
    print("|- Nhập 1: Danh sách ---")
    print("|- Nhập 2: Thêm      ---")
    print("|- Nhập 3: Xóa       ---")
    print("|- Nhập 4: Sửa       ---")
    print("|- Nhập 0: Thoát     ---")
    print("------------------------")

    action = int(input())
    s = st.Students()

    if action == 1:
        print('DANH SÁCH SINH VIÊN')
        s.show()
    elif action == 2:
        print('THÊM SINH VIÊN')
        print("Nhập Tên sinh viên: ", end='')
        name = input()
        s.insert(name)
    elif action == 3:
        print('XÓA SINH VIÊN')
        print("Nhập ID sinh viên cần xóa: ", end='')
        id = input()
        s.delete(id)
    elif action == 4:
        print('CẬP NHẬT SINH VIÊN')
        print("Nhập ID sinh viên cần cập nhật: ", end='')
        id = input()
        print("Nhập tên sinh viên mới: ", end="")
        name = input()
        s.update(id, name)
    else:
        break