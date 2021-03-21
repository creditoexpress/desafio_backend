import sys, os
import pymongo
from pymongo import MongoClient

BASE_PATH = os.path.abspath(__file__+ '/../../../../')
sys.path.append(BASE_PATH)

from src.consts.consts import *
from src.classes.db.Db import DbLib

class Users:

	def __init__(self, conn=None):
		if conn:
			self.conn = conn
		else:
			try:
				db   = DbLib()
				conn = db.connect(db="desafio")
				self.conn = conn
			except:
				self.conn = False
	
	def criar(self, input):
		
		data = {
			'ok': False,
			'errors': {},
			'data': 0
		}

		# Input
		nome       = ''
		cpf        = ''
		celular    = ''
		score      = 0
		negativado = False

		# Params
		if input:
			nome       = str(input['nome']) if 'nome' in input else ''
			cpf        = str(input['cpf']) if 'cpf' in input else ''                
			celular    = str(input['celular']) if 'celular' in input else ''    
			score      = int(input['score']) if 'score' in input else 0 
			negativado = bool(input['negativado']) if 'negativado' in input else False 
		
		# Validation
		if not nome:
			data['errors']['nome'] = 'Nome não indicado.'
		
		if not cpf:
			data['errors']['cpf'] = 'Cpf não indicado.'            

		if not celular:
			data['errors']['celular'] = 'Celular não indicado.'
		
		if score < 0 or score > 1000 :
			data['errors']['score'] = 'Score inválido.'
		
		if not self.conn:
			data['errors']['conn'] = 'Erro de comunicação com o banco de dados.'

		# verfica se cpf e celular ja foram cadastrados
		resp = self._verificar_cpf_celular(cpf, celular)
		if not resp["ok"] or not resp["data"]:
			
			# junta erros se houver algum
			data["errors"] = {**data["errors"], **resp["errors"]}

		if not data['errors']:
			try:
				
				row = {
					"nome": nome,
					"cpf": cpf,
					"celular": celular,
					"score": score,
					"negativado": negativado
				}
				resp = self.conn.users.insert_one(row)

				if not str(resp.inserted_id):
					data["errors"]["insert"] = "Erro ao inserir usuario."
				
				if not data['errors']:
					data['ok']   = True
					data['data'] = str(resp.inserted_id)

			except Exception as error:
				data['errors']['conn'] = 'Erro na conexão com o banco de dados: ' + str(error)
			
			finally:
				if type(self.conn)==MongoClient:
					self.conn.close()

		return data
	
	def criar_multiplos(self, inputs):
		
		data = {
			'ok': False,
			'errors': {},
			'data': False
		}

		# Input
		nome       = ''
		cpf        = ''
		celular    = ''
		score      = 0
		negativado = False

		# Params
		for input in inputs:
			if input:
				nome       = str(input['nome']) if 'nome' in input else ''
				cpf        = str(input['cpf']) if 'cpf' in input else ''                
				celular    = str(input['celular']) if 'celular' in input else ''    
				score      = int(input['score']) if 'score' in input else 0 
				negativado = bool(input['negativado']) if 'negativado' in input else False 
				
				# verfica se cpf e celular ja foram cadastrados
				resp = self._verificar_cpf_celular(cpf, celular)
				if not resp["ok"] or not resp["data"]:
					
					# junta erros se houver algum
					data["errors"] = {**data["errors"], **resp["errors"]}

		
			# Validation
			if not nome:
				data['errors']['nome'] = 'Nome não indicado.'
			
			if not cpf:
				data['errors']['cpf'] = 'Cpf não indicado.'            

			if not celular:
				data['errors']['celular'] = 'Celular não indicado.'
			
			if score < 0 or score > 1000 :
				data['errors']['score'] = 'Score inválido.'
			
		if not self.conn:
			data['errors']['conn'] = 'Erro de comunicação com o banco de dados.'

		if not data['errors']:
			try:

				resp = self.conn.users.insert_many(inputs)

				if not data['errors']:
					data['ok']   = True
					data['data'] = True

			except Exception as error:
				data['errors']['conn'] = 'Erro na conexão com o banco de dados: ' + str(error)
			
			finally:
				if type(self.conn)==MongoClient:
					self.conn.close()

		return data
	
	def verificar(self, input):
		
		data = {
			'ok': False,
			'errors': {},
			'data': 0
		}

		# Input
		cpf     = ''
		celular = ''

		# Params
		if input:
			cpf     = str(input['cpf']) if 'cpf' in input else ''                
			celular = str(input['celular']) if 'celular' in input else ''    
	
		# Validation
		if not cpf:
			data['errors']['cpf'] = 'Cpf não indicado.'            

		if not celular:
			data['errors']['celular'] = 'Celular não indicado.'
		
		if not self.conn:
			data['errors']['conn'] = 'Erro de comunicação com o banco de dados.'

		if not data['errors']:
			try:
				
				resp = self.conn.users.find_one({'cpf' : cpf, 'celular': celular})

				if resp:
					if not str(resp['_id']):
						data["errors"]["user"] = "Usuario não encontrado."
				else:
					data["errors"]["user"] = "Usuario não encontrado."

				if not data['errors']:
					data['ok']   = True
					data['data'] = str(resp['_id'])

			except Exception as error:
				data['errors']['conn'] = 'Erro na conexão com o banco de dados: ' + str(error)
			
			finally:
				if type(self.conn)==MongoClient:
					self.conn.close()

		return data
	
	def calcular_juros(self, input):
		
		data = {
			'ok': False,
			'errors': {},
			'data': 0
		}

		# Input
		id_user      = 0
		valor        = 0
		parcelas     = ""
		sem_cadastro = False
		negativado   = False

		# Params
		if input:
			id_user  = str(input['id']) if 'id' in input else 0                
			valor    = str(input['valor']) if 'valor' in input else 0    
			parcelas = str(input['numeroParcelas']) if 'numeroParcelas' in input else ""  
	
		# Validation
		if not id_user:
			data['errors']['user'] = 'Usuario não indicado.'            

		if not valor:
			data['errors']['valor'] = 'Valor não indicado.'
		
		if not parcelas in PARCELAS:
			data['errors']['parcelas'] = 'Parcela não indicada ou inválida.'
		
		if not self.conn:
			data['errors']['conn'] = 'Erro de comunicação com o banco de dados.'

		if not data['errors']:
			try:
				
				resp = self.conn.users.find_one({'_id': id_user})
	
				if resp:
					if not "negativado" in resp or not "score" in resp:
						data["errors"]["user"] = "Usuario inválido."
				else:
					sem_cadastro = True

				if not data['errors']:
					taxa_aplicada = ""
					if sem_cadastro :
						taxa_aplicada = "SCORE_BAIXO"
					else:
						if resp["negativado"]:
							taxa_aplicada = "negativado"
						else:
							if int(resp["score"]) > 500:
								taxa_aplicada = "SCORE_ALTO"
							else:
								taxa_aplicada = "SCORE_BAIXO"

					try:
						valor = int(valor)
						valor += valor * TAXAS[taxa_aplicada][parcelas]
						data['data'] = valor
					except:
						data['errors']['valor'] = 'Valor inválido.'

					data['ok'] = True

			except Exception as error:
				data['errors']['conn'] = 'Erro na conexão com o banco de dados: ' + str(error)
			
			finally:
				if type(self.conn)==MongoClient:
					self.conn.close()

		return data
	
	def _verificar_cpf_celular(self, cpf, celular):
		
		data = {
			'ok': False,
			'errors': {},
			'data': False
		}  
	
		# Validation
		if not cpf:
			data['errors']['cpf'] = 'Cpf não indicado.'            

		if not celular:
			data['errors']['celular'] = 'Celular não indicado.'
		
		if not self.conn:
			data['errors']['conn'] = 'Erro de comunicação com o banco de dados.'

		if not data['errors']:
			try:
				
				resp = self.conn.users.find({'cpf' : cpf, 'celular': celular}).count()

				if resp > 0:
					data["errors"]["input"] = "Cpf e celular ja cadastrado."
				

				if not data['errors']:
					data['ok']   = True
					data['data'] = True

			except Exception as error:
				data['errors']['conn'] = 'Erro na conexão com o banco de dados: ' + str(error)
			
			finally:
				if type(self.conn)==MongoClient:
					self.conn.close()

		return data