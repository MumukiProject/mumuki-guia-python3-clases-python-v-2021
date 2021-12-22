
  def test_un_celular_vuelve_a_tener_100_de_bateria_si_lo_cargo_a_tope(self):
    celular = Celular(100)
    celular.utilizar(200)
    celular.cargar_a_tope()
    self.assertEqual(celular.bateria,100)