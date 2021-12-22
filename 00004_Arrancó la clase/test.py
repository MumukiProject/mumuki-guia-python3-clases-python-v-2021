
  def test_Si_creo_un_nuevo_Celular_le_puedo_especificar_su_saldo_inicial(self):
    celular_aristimuño = Celular(44)
    self.assertEqual(celular_aristimuño.saldo,44)
    
  def test_Si_creo_un_nuevo_Celular_le_puedo_especificar_su_bateria_inicial(self):
    celular_aristimuño = Celular(100)
    self.assertEqual(celular_aristimuño.bateria,100)