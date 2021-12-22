  
  def test_cuando_una_golondrina_come_20_gramos_su_energia_aumenta_10(self):
    una_golondrina = Golondrina(100, 'General Las Heras')
    un_caballo.comer(20)
    self.assertEqual(una_golondrina.energia, 110)
    
  def test_cuando_una_golondrina_come_50_gramos_su_energia_aumenta_25(self):
    una_golondrina = Golondrina(100, 'Quilmes')
    un_caballo.comer(50)
    self.assertEqual(una_golondrina.energia, 125)

  def test_cuando_una_golondrina_vuela_a_una_ciudad_su_energia_disminuye_a_la_mitad(self):
    una_golondrina = Golondrina(100, 'Quilmes')
    una_golondrina.volar_hacia("Bariloche")
    self.assertEqual(una_golondrina.energia, 50)
    
  def test_cuando_una_golondrina_vuela_a_Bariloche_su_ciudad_pasa_a_ser_Bariloche(self):
    una_golondrina = Golondrina(100, 'Quilmes')
    una_golondrina.volar_hacia("Bariloche")
    self.assertEqual(una_golondrina.ciudad, "Bariloche")

  def test_cuando_una_golondrina_vuela_a_Merlo_su_ciudad_pasa_a_ser_Merlo(self):
    una_golondrina = Golondrina(100, 'Quilmes')
    una_golondrina.volar_hacia("Merlo")
    self.assertEqual(una_golondrina.ciudad, "Merlo")