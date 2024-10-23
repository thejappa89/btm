import jappalib.interface
from time import sleep


company_energia = []
company_saneamento = []
company_gas = []

print('AVISO! Script em construção...')
sleep(2)

resp = jappalib.interface.menu(['Dashboard', 'Áreas Técnicas','Equatorial', 'Saneago', 'Ultragás', 'Reservatórios', 'VRPs', 'Lixeiras', 'Extintores', 'Hidrantes', 'Check list', 'Manuais', 'Configurações', 'Sair...'], 'MAPEAMENTO TÉCNICO PREDIAL')

if resp == 1:
    jappalib.interface.titulo('BTM > Dashboard')
elif resp == 2:
    jappalib.interface.titulo('BTM > Áreas Técnicas')
elif resp == 3:
    jappalib.interface.titulo('BTM > Equatorial')
elif resp == 4:
    jappalib.interface.titulo('BTM > Saneago')
elif resp == 5:
    jappalib.interface.titulo('BTM > Ultragás')
elif resp == 6:
    jappalib.interface.titulo('BTM > Reservatórios')
elif resp == 7:
    jappalib.interface.titulo('BTM > VRPs')
elif resp == 8:
    jappalib.interface.titulo('BTM > Lixeiras')
elif resp == 9:
    jappalib.interface.titulo('BTM > Extintores')
elif resp == 10:
    jappalib.interface.titulo('BTM > Hidrantes')
elif resp == 11:
    jappalib.interface.titulo('BTM > Check list')
elif resp == 12:
    jappalib.interface.titulo('BTM > Manuais')
elif resp == 13:
    jappalib.interface.titulo('BTM > Configurações')
elif resp == 14:
    print('Finalizando programa...')
    sleep(2)
    print('Finalizado com sucesso!')
