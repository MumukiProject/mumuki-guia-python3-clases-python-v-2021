  
  def test_Si_le_cargamos_$50_a_un_celular_su_saldo_aumenta_en_50(self):
    celular = Celular(0,0,'Humanoid 10')
    celular.cargar_saldo(50)
    self.assertEqual(celular.saldo,50)
    
  def test_Si_le_cargamos_$100_a_un_celular_su_saldo_aumenta_en_100(self):
    celular = Celular(0,0,'Humanoid 10')
    celular.cargar_saldo(100)
    self.assertEqual(celular.saldo,100)