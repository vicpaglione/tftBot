import win32api, win32con
import pynput
import pywintypes
import pyautogui as pg, sys, PIL.ImageGrab, win32gui
from time import sleep
from pynput.keyboard import Key, Controller

keyboard = Controller()

print("TFT Token Farm BOT")
print("Criado por Victor Paglione")
sleep(2)
print("Iniciando")

#Botão de esc
xESC = 1140
yESC = 589

#Botão de FF
xFF = 535
yFF = 558

#Botão de procurar partida
xProcurarPartida = 553
yProcurarPartida = 592

#Botão de aceitar partida
xAceitarPartida = 636
yAceitarPartida = 495

#Coordenadas do primeiro campeão na loja
xCampeoes = 386
yCampeoes = 638

#Distancia lateral entre os campeões da loja
distanciaCampeoes = 132

#Botão de upar o level
xSubirNivel = 248
ySubirNivel = 637

#Posição aleatoria no tabuleiro
xMoverMiniLenda1 = 484
yMoverMiniLenda1 = 344

#Outra posição aleatoria no tabuleiro
xMoverMiniLenda2 = 641
yMoverMiniLenda2 = 446

#Qualquer pixel que a tela do jogo cubra e que a tela do client não cubra
xPixelDesktop = 136
yPixelDesktop = 660

#Botao de aceitar a recompensa das missões
xAceitarMissao = 640
yAceitarMissao = 593

#Botão de sair do jogo
xClicarSair = 554
yClicarSair = 320

#Botao de aceitar a recompensa das missões
xAceitarMissao = 640
yAceitarMissao = 593

partidas = 0
def clicarProcurarPartida():
	pg.moveTo(xProcurarPartida, yProcurarPartida, 1)
	pg.click()
#
def clicarESC():
	pg.moveTo(xESC, yESC)
	pg.mouseDown()
	sleep(0.2)
	pg.mouseUp()
#

def clicarFF():
	pg.moveTo(xFF, yFF)
	pg.mouseDown()
	sleep(0.2)
	pg.mouseUp()
#

def clicarAceitarPartida():
	pg.moveTo(xAceitarPartida, yAceitarPartida)
	pg.click()
#

def clicarJogarNovamente():
	clicarProcurarPartida()
#

def subirNivel(quantidadeCliques=0):
	j = 0
	pg.moveTo(xSubirNivel, ySubirNivel, 0.5)

	while(j < quantidadeCliques):
		j = j + 1
		
		pg.mouseDown()
		sleep(0.2)
		pg.mouseUp()
	#
#	

def moverMiniLenda(caminho=0):
	#Posição random 1
	if(caminho == 0):
		pg.moveTo(xMoverMiniLenda1, yMoverMiniLenda1, 0.5)
		pg.mouseDown(button='right')
		sleep(0.5)
		pg.mouseUp(button='right')
		return
	#

	#Posição random 2
	if(caminho==1):
		pg.moveTo(xMoverMiniLenda2, yMoverMiniLenda2, 0.5)
		pg.mouseDown(button='right')
		sleep(0.5)
		pg.mouseUp(button='right')
		return
	#
#

def clicarSairJogo():
	pg.moveTo(xClicarSair, yClicarSair)
	pg.mouseDown()
	sleep(0.2)
	pg.mouseUp()
#

def clicarAceitarMissao(nVezes=1):
        j = 0

        while(j < nVezes):
                pg.moveTo(xAceitarMissao, yAceitarMissao)
                pg.click()
                sleep(10)
                j = j + 1
        #
#

def comprarCampeoes(quantidade=0):
	j = 0
	xInicial = xCampeoes

	while(j < quantidade):
		pg.moveTo(xInicial + (j*distanciaCampeoes), yCampeoes, 0.5)
		pg.mouseDown()
		sleep(0.2)
		pg.mouseUp()

		j = j + 1
	#
#

#Salva instancia do client para que seja trazido para o foreground apos o fim do game
leagueClient = win32gui.FindWindow(0, "League of Legends")

pixelDesktop = PIL.ImageGrab.grab().load()[xPixelDesktop,yPixelDesktop]
sleep(5)

try:
	while True:
		sleep(7)
		
		#Traz o client para o foreground (topo) após o jogo acabar
		win32gui.SetForegroundWindow(leagueClient)
		win32gui.BringWindowToTop(leagueClient)
		sleep(1)
		sleep(2)
		

		#Entra na fila
		print("Na fila...")
		clicarProcurarPartida()

		#Enquanto a janela do jogo não abrir, continua clicando pra aceitar partida
		while (PIL.ImageGrab.grab().load()[xPixelDesktop,yPixelDesktop] == pixelDesktop):
			clicarAceitarPartida()
			sleep(1)
		#

		print("Partida encontrada")

		#Espera 10s antes de começar, pois a tela de load pode ficar bugada no começo
		sleep(20)

		#Grava um pixel da tela de load
		pixelTelaLoad = PIL.ImageGrab.grab().load()[xPixelDesktop,yPixelDesktop]

		#Compara o pixel gravado da tela de load com o pixel atual smo lugar, para detectar quando o jogo começar
		while (PIL.ImageGrab.grab().load()[xPixelDesktop,yPixelDesktop] == pixelTelaLoad):
			pass
		#

		#Traz o jogo para o foreground
		leagueGame = win32gui.FindWindow(0, "League of Legends (TM) Client")
		win32gui.SetForegroundWindow(leagueGame)
		win32gui.BringWindowToTop(leagueGame)

		print("Jogo iniciado")

                #Nesse ponto, a partida começou, e é iniciado um timer de 15 minutos
		x = 600
		while (x > 0):
			x = x - 1
			sleep(1)

			if(x == 530):
				comprarCampeoes(1)
				moverMiniLenda(0)
				moverMiniLenda(1)
				moverMiniLenda(1)
				moverMiniLenda(1)
				moverMiniLenda(0)
			#

			if(x == 475):
				comprarCampeoes(1)
			#

			if(x == 409):
				moverMiniLenda(1)
				subirNivel(1)
			#

			if(x == 360):
				
				subirNivel(1)
				moverMiniLenda(0)
				moverMiniLenda(1)
			#

			if(x == 290):
				moverMiniLenda(1)
				comprarCampeoes(1)
				moverMiniLenda(0)
			#

			if(x == 220):
				comprarCampeoes(1)
				subirNivel(1)
			#

			if(x == 260):
				subirNivel(1)
				comprarCampeoes(1)
				moverMiniLenda(1)
			#

			if(x == 60):
				subirNivel(1)
				moverMiniLenda(0)
				moverMiniLenda(1)
			#
		#

		timer = 0
		print("Aguardando surrender")
		clicarESC()
		sleep(2)
		
		clicarFF()
		

                #Após acabar os 15 minutos, espera pra morrer, clicando no botão de sair até detectar que o jogo fechou
		while (PIL.ImageGrab.grab().load()[xPixelDesktop,yPixelDesktop] != pixelDesktop):
			clicarSairJogo()
			sleep(3)

			#
			if(timer%60 == 0):
				subirNivel(1)
				comprarCampeoes(1)
			#

			timer = timer + 3
		#

		print("Iniciando nova Partida")
		partidas = partidas + 1
		print(partidas)
		print("")

		# do Client
		sleep(10)
		win32gui.SetForegroundWindow(leagueClient)
		win32gui.BringWindowToTop(leagueClient)
		sleep(5)
		
		#
		#
		clicarAceitarMissao(2)

		#
		clicarJogarNovamente()
                

except KeyboardInterrupt:
	print('\n')
#

		













		
