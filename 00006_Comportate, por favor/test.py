
  def test_un_celular_vuelve_a_tener_100_de_bateria_si_lo_cargo_a_tope(self):
    celular = Celular(100, 0)
    celular.utilizar(200)
    celular.cargar_a_tope()
    self.assertEqual(celular.bateria,100)
    
    
  def test_un_celular_necesita_saldo_si_tiene_$0(self):
    celular = Celular(100, 0)
    self.assertTrue(celular.necesita_saldo())