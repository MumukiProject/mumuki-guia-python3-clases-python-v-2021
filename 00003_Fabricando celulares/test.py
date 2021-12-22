
  def test_el_celular_de_lu_tiene_inicialmente_50%_de_batería(self):
    self.assertEqual(celular_de_lu.bateria, 50)
    
  def test_el_celular_de_lu_tiene_inicialmente_$80_de_saldo(self):
    self.assertEqual(celular_de_lu.saldo, 80)