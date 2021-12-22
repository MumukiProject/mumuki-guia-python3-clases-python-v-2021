  
  def test_cuando_un_gato_come_20_gramos_su_energia_aumenta_20(self):
    un_gato = Gato(100, 4)
    un_gato.comer(20)
    self.assertEqual(un_gato.energia, 120)
    
  def test_cuando_un_gato_come_50_gramos_su_energia_aumenta_50(self):
    un_gato = Gato(150, 8)
    un_gato.comer(50)
    self.assertEqual(un_gato.energia, 200)

  def test_cuando_un_gato_cumple_anios_su_edad_aumenta_en_uno(self):
    un_gato = Gato(120, 4)
    un_gato.cumplir_anios()
    self.assertEqual(un_gato.edad, 5)