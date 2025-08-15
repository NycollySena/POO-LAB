from catalogo import CatalogoCDs

class main:
    teste1 = CatalogoCDs()
  
    teste1.AdicionarCD("legiao urbana", 1, "renato russo", True, "muito bom")
    teste1.AdicionarCD("engenheiros do havai", 1, "humberto gessingner", True, "bom")
    teste1.ListarCDs()
    teste1.Buscar("engenheiros do havai")
    teste1.PossuoCD("engenheiros do havai")
    teste1.CdPosssuo()
    teste1.esta_vazio()
   