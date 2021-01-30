import db_exceptions
import sinhvien_db
import sinhvien_model, sinhvien_view, sinhvien_controller

def start():
    #Khởi tạo đối tượng model
    model = sinhvien_model.SinhVienModel("localhost", "root", "1234az", "quanlysvpxu")
    #Khởi tạo đối tượng view
    view = sinhvien_view.SinhVienView()
    #Khởi tạo controller
    controller = sinhvien_controller.SinhVienController(model, view)
    item = menu()
    while item in ["1", "2", "3", "4"]:
        if item == "1":
            controller.show_all_sinhvien()
        elif item == "2":
            hoten = input("Nhập họ tên: ")
            tuoi = int(input("Nhập năm sinh: "))
            sdt = int(input("Nhập sdt: "))
            controller.them_sinhvien(hoten, tuoi,sdt)
        elif item == "3":
            idsinhvien = input("Nhập id: ")
            hoten = input("Nhập họ tên: ")
            tuoi = int(input("Nhập năm sinh: "))
            sdt = int(input("Nhập sdt: "))
            controller.them_sinhvien(idsinhvien,hoten, tuoi, sdt)
        elif item == "4":
            idsinhvien = input("Nhập id: ")
            controller.them_sinhvien(idsinhvien)

        item = menu()

    except db_exceptions.DatabaseConnection as err:
        print(err)


def menu():
    print("1: Hiển thị tất cả sinh viên")
    print("2: Thêm mới sinh viên")
    print("3: Cập nhật sinh viên")
    print("4: Xóa P")
    choice = input("Bạn hãy chọn các số từ 1 đến 4. Ngược lại là thoát khỏi chương trình.")
    return choice

if __name__ == "__main__":
    start()