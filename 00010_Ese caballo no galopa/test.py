  
  def test_cuando_un_caballo_come_100_gramos_su_energia_aumenta_200(self):
    un_caballo = Caballo(100, 'Frisón')
    un_caballo.comer(100)
    self.assertEqual(un_caballo.energia, 300)
    
  def test_cuando_un_caballo_come_300_gramos_su_energia_aumenta_600(self):
    un_caballo = Caballo(100, 'Mustang')
    un_caballo.comer(300)
    self.assertEqual(un_caballo.energia, 700)

  def test_cuando_un_caballo_galopa_10_kms_su_energia_disminuye_en_10(self):
    un_caballo = Caballo(100, 'Frisón')
    un_caballo.galopar(10)
    self.assertEqual(un_caballo.energia, 90)
    
  def test_cuando_un_caballo_galopa_20_kms_su_energia_disminuye_en_20(self):
    un_caballo = Caballo(100, 'Mustang')
    un_caballo.galopar(20)
    self.assertEqual(un_caballo.energia, 80)