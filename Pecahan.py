class bilpecahan:
  def __init__(self, pembilang, penyebut):
      self.pembilang = pembilang
      self.penyebut = penyebut
  def dikalikan(self,bilpecahan2):
    hasilpembilang=self.pembilang*bilpecahan2.pembilang
    hasilpenyebut = self.penyebut*bilpecahan2.penyebut
    hasil = bilpecahan(hasilpembilang,hasilpenyebut)
    return hasil
    
 peca= bilpecahan(4 2)
 pecb = bilpecahan(2 3)
 pecc = peca.dikalikan(pecb)
 pecd = pecb.dikalikan(peca)
 print(str(pecc.pembilang)+'/'+str(pecc.penyebut))
 print(str(pecd.pembilang)+'/'+str(pecd.penyebut))