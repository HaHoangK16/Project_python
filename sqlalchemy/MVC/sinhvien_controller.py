import db_exceptions
import sinhvien_db

class SinhVienController(object):
    #Phương thức khởi tạo
    def __init__(self, model, view):
        self.model = model
        self.view = view

    #Phương thức hiển thị tất cả dữ liệu của bảng sinhvien
    def show_all_sinhvien(self):
      try:
        items = self.model.get_all_sinhvien()
        self.view.display_all_sinhvien(items)
      except db_exceptions.SelectError as err_msg:
          self.view.thong_bao_loi(err_msg)

    #Phương thức insert
    def them_sinhvien(self, hoten, namsinh,sdt):
      try:
            resultID = self.model.them_sinhvien(hoten, namsinh, sdt)
            self.view.ket_qua_insert(resultID)
      except db_exceptions.InsertError as err:
            self.view.thong_bao_loi(err)

    #Phương thức update

    def sua_sinhvien(self,idsinhvien, hoten,namsinh,sdt ):
      try:
        self.model.sua_sinhvien(idsinhvien,hoten,namsinh,sdt)
        self.view.ket_qua_update()
      except db_exceptions.UpdateError as err:
        self.view.thong_bao_loi(err)
    #Phương thức delete

    def xoa_sinhvien(self, idsinhvien):
      try:
        self.model.xoa_sinhvien(idsinhvien)
        self.view.ket_qua_delete()
      except db_exceptions.DeleteError as err:
        self.view.thong_bao_loi(err)