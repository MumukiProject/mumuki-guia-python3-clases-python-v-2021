
  def test_Si_creo_un_nuevo_Celular_le_puedo_especificar_su_sistema_opertivo(self):
    celular_aristimuño = Celular(0,0,'Humanoid 1.0')
    self.assertEqual(celular_aristimuño.sistema_operativo,'Humanoid 1.0')